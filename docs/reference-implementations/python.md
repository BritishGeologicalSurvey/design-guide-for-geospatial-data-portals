# Python Implementations

## BGS Index and Meta data API template 

(LINK to GIT REPOSITRY)

For simple APIs serving BGS data where:
* Data is in a DB Query Layer (with maybe a couple of dictionaries)
* The Query Layer is an index of maps/reports/rocks/fossils/...
* Each item has relatively few simple properties
* Each item optionally has a link to an external resource (e.g. large image viewer or PDF download)
* API provides only "search", "full details" and "dictionary (dropdown)" endpoints

## Time series and Sensor data

(LINK to GIT REPOSITRY)

TODO


## OpenAPI schema definition for specimen/{specimen_id}

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
        "SAMPLE_NUMBER": {
            "title": "Sample Number",
            "type": "integer",
            "example": 1278
        },
        "SAMPLE_SUFFIX": {
            "title": "Sample Suffix",
            "type": "string",
            "example": "."
        },
        "REG_NO_UPP": {
            "title": "Reg No Upp",
            "type": "string",
            "example": "11E1278."
        },
        "LOCALITY_NAME": {
            "title": "Locality Name",
            "type": "string",
            "example": "Loup of Kilfeddar, New Luce"
        },
        "TAXON_CODE": {
            "title": "Taxon Code",
            "type": "string",
            "example": "GRAPTOLITHINA"
        },
        "TAXON_DESC": {
            "title": "Taxon Desc",
            "type": "string",
            "example": "Graptolithina"
        },
        "GENUS": {
            "title": "Genus",
            "type": "string",
            "example": "Thamnograptus"
        },
        "SUBGENUS": {
            "title": "Subgenus",
            "type": "string",
            "example": " "
        },
        "SPECIES": {
            "title": "Species",
            "type": "string",
            "example": "capillaris"
        },
        "SUBSPECIES": {
            "title": "Subspecies",
            "type": "string",
            "example": " "
        },
        "TYPE_STATUS_CODE": {
            "title": "Type Status Code",
            "type": "string",
            "example": "NA"
        },
        "TYPE_STATUS_DECODE": {
            "title": "Type Status Decode",
            "type": "string",
            "example": "Not Designated a Type"
        },
        "AGE_CODE": {
            "title": "Age Code",
            "type": "string",
            "example": "O4"
        },
        "AGE_DECODE": {
            "title": "Age Decode",
            "type": "string",
            "example": "Caradoc Series"
        },
        "AUTHOR_UPP": {
            "title": "Author Upp",
            "type": "string",
            "example": " "
        },
        "REFERENCE": {
            "title": "Reference",
            "type": "string",
            "example": "   "
        },
        "COLLECTOR_DECODE_UPP": {
            "title": "Collector Decode Upp",
            "type": "string",
            "example": "RUSHTON & TUNNICLIFF"
        },
        "COLLECTOR_WWW_DISPLAY": {
            "title": "Collector Www Display",
            "type": "string",
            "example": "NO"
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
    SAMPLE_NUMBER: int = Field(..., example=1278)
    SAMPLE_SUFFIX: str = Field(..., example=".")
    REG_NO_UPP: str = Field(..., example="11E1278.")
    LOCALITY_NAME: str = Field(..., example="Loup of Kilfeddar, New Luce")
    TAXON_CODE: str = Field(None, example="GRAPTOLITHINA")
    TAXON_DESC: str = Field(None, example="Graptolithina")
    GENUS: str = Field(None, example="Thamnograptus")
    SUBGENUS: str = Field(None, example=" ")
    SPECIES: str = Field(None, example="capillaris")
    SUBSPECIES: str = Field(None, example=" ")
    TYPE_STATUS_CODE: str = Field(..., example="NA")
    TYPE_STATUS_DECODE: str = Field(..., example="Not Designated a Type")
    AGE_CODE: str = Field(..., example="O4")
    AGE_DECODE: str = Field(..., example="Caradoc Series")
    AUTHOR_UPP: str = Field(None, example=" ")
    REFERENCE: str = Field(..., example="   ")
    COLLECTOR_DECODE_UPP: str = Field(None, example="RUSHTON & TUNNICLIFF")
    COLLECTOR_WWW_DISPLAY: str = Field(..., example="NO")
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