# Python Implementations

This page contains information about implementing a BGS-style API service using Python.

## Reference implementation

The reference implementation for a Python-based API service is [Palaeosaurus](https://kwvmxgit.ad.nerc.ac.uk/apis/api-services/palaeosaurus-api).  It is built using the [FastAPI](https://fastapi.tiangolo.com/) framework and uses [Pydantic](https://pydantic-docs.helpmanual.io/) to validate and structure data.  FastAPI automatically generates a JSON OpenAPI specification and uses it to serve interactive documentation via Swagger.  The application runs in a Docker container.

Palaeosaurus demonstrates dictionary-style endpoints (e.g. [/vocab/geochrons](http://hwlapi01.bgslcdevops.test:8001/palaeosaurus/v1/docs#/default/get_vocab_geochrons_palaeosaurus_v1_vocab_geochrons_get)), using a path-parameter as an id (e.g. [/specimen/{specimen_id}](http://hwlapi01.bgslcdevops.test:8001/palaeosaurus/v1/docs#/default/get_specimens_by_id_palaeosaurus_v1_specimen__specimen_id__get)) and a multi-parameter query (e.g. [/specimens/?species=...](http://hwlapi01.bgslcdevops.test:8001/palaeosaurus/v1/docs#/default/get_specimens_palaeosaurus_v1_specimens_get)).

## Code structure of an API endpoint

Beneath is the tree of an API project.

```
.
├── app
│   ├── config.py
│   ├── database.py
│   ├── errors.py
│   ├── main.py
│   ├── models
│   │   ├── paths.py
│   │   ├── queries.py
│   │   └── schemas.py
│   ├── routes
│   │   ├── specimens.py
│   │   ├── vocab_geochrons.py
│   │   ├── ...
│   └── sql_common.py
├── deploy
└── test
    ├── integration
    └── unit
        └── routes
├── docker-compose-local.yml
├── Dockerfile
├── README.md
├── requirements.txt
```

Endpoints are defined in files in the `routes` directory.  They use classes imported from the `models` folder to provide data validation and metadata used to populate the OpenAPI specification (see below for details).  `config.py` contains general and environment-specific configuration settings and `database.py` has a function for connecting to the database depending on the config.  Endpoints are added to FastAPI by adding the router in `main.py`.

Each endpoint has unit tests (to confirm SQL query preparation and data serialisation) and integration tests to confirm the full end-to-end working of an API request.

See [Deploying APIs](http://apis.glpages.ad.nerc.ac.uk/api-guidance-docs/#/main-content/deploying-apis) for details on Docker files and the `deploy` folder.


### Example acceptance criteria

The following checklist can be applied as acceptance criteria to a new endpoint built to fit the specification.

*Layout*

+ [ ] Endpoint is single file in `routes` directory
+ [ ] Endpoint takes Config as dependency (so it has access to database parameters etc)
+ [ ] Endpoint function calls a `query_database`, `parse_results` and `prepare_response` functions within their own try/except blocks
+ [ ] If multiple parameters are used, these are validated and grouped together `request_params` dict.
+ [ ] `query_database` function takes `config` (+/- `request_params`) as arguments and calls `prepare_xxx_query` to get SQL query.
+ [ ] `prepare_xxx_query` takes `config` (+/- `request_params.keys()`) arguments and returns a SQL string with correct schema/table names for the environment.  If optional query filters are required, the string is constructed using named placeholders and `prettify`.

*OpenAPI*

+ [ ] Response model contains at least `msg`, `type`, `self` and `data` fields
+ [ ] Path and Query model definitions contain example values
+ [ ] Pydantic models for data contain example values
+ [ ] Response schemas are imported from `app.models.schemas`
+ [ ] Endpoint Query models are imported from `app.models.queries`
+ [ ] Endpoint Path models are imported from `app.models.paths`

*Tests*

+ [ ] `test/unit/routes/test_<endpoint>.py` contains (at least) tests for the `prepare_xxx_query`.
+ [ ] Tests on `prepare_xxx_query` confirm correct table is selected for each environment
+ [ ] Tests on `prepare_xxx_query` confirm queries contain placeholders for necessary parameters
+ [ ] `test/integration/test_<endpoint>.py` tests (at least) a representative query in both DEVELOP and PRODUCTION environments
+ [ ] If required, integration tests for parameters test: all the parameters present; no parameters present; misspelled parameters


## Generating OpenAPI schema definitions from Python data models

The Swagger pages for specimen/{specimen_id are at: http://hwlapi01.bgslcdevops.test:9001/palaeosaurus/v1/docs#/default/get_specimens_by_id_palaeosaurus_v1_specimen__specimen_id__get
Schema definitions are used in three locations in the OpenAPI specification:

* request parameters used in the query or the path
* response models that wrap data items with metadata
* data models for response items

In the section below, the OpenAPI JSON and the Pydantic/FastAPI models that are used to define them are shown.
#### Request parameters
```json
"/palaeosaurus/v1/specimen/{specimen_id}": {
            "get": {
                "summary": "Get Specimens By Id",
                "operationId": "get_specimens_by_id_palaeosaurus_v1_specimen__specimen_id__get",
                "parameters": [
                    {
                        "description": "The id for the specimen to return",
                        "required": true,
                        "schema": {
                            "title": "Specimen ID",
                            "type": "integer",
                            "description": "The id for the specimen to return",
                            "example": 7657
                        },
                        "name": "specimen_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/SpecimenResponse"
                                }
                            }
                        }
                    },

```

Below is the FastAPI Path model that corresponds to the parameter schema object in the above JSON and can be found at `app/models/paths.py`

```python
specimen_id_path = Path(
    ...,
    title='Specimen ID',
    description='The id for the specimen to return',
    example=7657
)

```
        
#### Response
```json
 "SpecimenResponse": {
                "title": "SpecimenResponse",
                "required": [
                    "msg",
                    "type",
                    "self"
                ],
                "type": "object",
                "properties": {
                    "msg": {
                        "title": "Msg",
                        "type": "string"
                    },
                    "type": {
                        "title": "Type",
                        "type": "string"
                    },
                    "self": {
                        "title": "Self",
                        "type": "string"
                    },
                    "data": {
                        "title": "Data",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Specimen"
                        },
                        "default": []
                    },
                    "meta": {
                        "$ref": "#/components/schemas/PagingItem"
                    }
                }
            },
```

The above JSON is generated from the Pydantic response model below found in `app/models/schemas.py`. The SpecimenResponse uses
pythons List structure to contain Specimen objects in its response.
```python
class MinimalResponse(BaseModel):
    msg: str
    type: str
    self: str


class SpecimenResponse(MinimalResponse):
    data: List[Specimen] = []
    meta: PagingItem = None
```

#### Data item model
```json 
"Specimen": {
    "title": "Specimen",
    "required": [
        "SAMPLE_ID",
        "SAMPLE_PREFIX",
        "SAMPLE_NUMBER",
        "SAMPLE_SUFFIX",
        "REG_NO_UPP",
        "LOCALITY_NAME",
        "TYPE_STATUS_CODE",
        "TYPE_STATUS_DECODE",
        "AGE_CODE",
        "AGE_DECODE",
        "REFERENCE",
        "COLLECTOR_WWW_DISPLAY",
        "DONOR_WWW_DISPLAY"
    ],
    "type": "object",
    "properties": {
        "SAMPLE_ID": {
            "title": "Sample Id",
            "type": "integer",
            "example": 7850
        },
        "SAMPLE_PREFIX": {
            "title": "Sample Prefix",
            "type": "string",
            "example": "11E"
        },
        {
            ...
        },
        "DONOR_DECODE_UPP": {
            "title": "Donor Decode Upp",
            "type": "string",
            "example": " "
        },
        "DONOR_WWW_DISPLAY": {
            "title": "Donor Www Display",
            "type": "string",
            "example": "NO"
        }
    }
},
```
      
The Pydantic model below found in `app/models/schemas.py` has a set of attribute names that correspond to the attributes of the rows returns.
Each attribute is set with a Pydantic `Field` object which can detail extra information in the OpenAPI schema above as can
FastAPI `Query`, `Path` objects. 
The `...` notation accepts the values assigned when creating a Specimen object while None allows for empty values. 

```python
class Specimen(BaseModel):
    SAMPLE_ID: int = Field(..., example=7850)
    SAMPLE_PREFIX: str = Field(..., example="11E")
        
        ...
    
    DONOR_DECODE_UPP: str = Field(None, example=" ")
    DONOR_WWW_DISPLAY: str = Field(..., example="NO")

```      

Using Pydantic when developing an API service that returns data in JSON format has several advantages. 
Python has made improvements with static type checking and Pydantic builds on this to enforce type checking dynamically. 
In the case of an API, when each endpoint is requested, the response will be validated against a Pydantic model. 
This effectively acts as a contract for the API responses.

Below is an example of an endpoint. Each endpoint has a parameter `response_model` and can assign a 
Pydantic model to convert and validate the endpoints output to its declared type in the model. 
Pydantic models must declare the expected value type and this is where the Pydantic model is specified in FastAPI to 
be shown in the OpenAPI JSON. Pydantic comes with a huge set of types see [here](https://pydantic-docs.helpmanual.io/usage/types/).

```python
@router.get(
    config.get_config().BASE_PATH + '/specimen/{specimen_id}',
    response_model=SpecimenResponse,
    responses={
        422: {"model": ErrorResponse},
    }
)
def get_specimens_by_id(request: Request, specimen_id: int = specimen_id_path,
                        conf: config.AppConfig = Depends(config.get_config)):
    """/specimen/{specimen_id} endpoint"""

   ...

    return response
```

After extracting data from a database the rows can be converted to a Pydantic model at 
the same time limiting the data to the attributes declared in the model by excluding those 
attributes/values in the row object not declared in the model. Below the `parse_results` function 
found in each endpoint file unpacks the values in each row into a TypeStatus model. 

```python
def parse_results(rows):
     return [Specimen(**row) for row in rows]
```

Note: In the case of `specimen/{specimen_id}` endpoint, it will only return 1 database object to be converted. In the case
of the `specimens` endpoints this will unpack numerous items.
