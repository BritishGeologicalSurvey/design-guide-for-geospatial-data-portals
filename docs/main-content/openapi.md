# Using OpenAPI

## Why use OpenAPI?

OpenAPI is a broadly adopted industry standard for describing modern APIs, overseen by the OpenAPI Initiative, an open-source collaboration project of the Linux Foundation.
An [OpenAPI definition](https://swagger.io/specification/) is a JSON/YAML file that is stored in a web accessible location and describes how to use the API.

An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.
With a small amount of additional metadata (an index of APIs with pointers to their OpenAPI files) we can also auto-generate API discovery tools.

## What is this guidance for?

The OpenAPI Specification describes a very minimal set of required data, but allows for a lot of optional added detail (and complexity) if required.
This guidance aims to describe a level of detail that allows BGS users and automated tools to make full use of the specification - but without making it too complex.

## Creating and serving OpenAPI Documents

*  The OpenAPI specification should be created very early in a project as part of the design phase
*  All API source code should contain an OpenAPI document named **"openapi.json"**
*  OpenAPI documents should comply with **version 3.0.3** (latest as of 25th Feb 2020)
*  All APIs should support an endpoint **"{server}/openapi"** that returns the **"openapi.json"** definition

## Anatomy of a BGS OpenAPI Document

The root of an API document must contain the following keys:

| key | type | description |
| ------ | ------ | ------ |
| openapi | string | Open API Version - currently "3.0.3" |
| info | object |  API Description and terms  |
| servers | array |  API Server URL |
| components | object |  Reusable definitions to be used in "paths" object |
| paths | object | The available paths and operations for the API |

*NOTE: The optional "tags" and "security" keys are currently out-of-scope of this guidance*

### openapi (REQUIRED)

This indicates the version of OpenAPI used and will currently be 
```javascript
"openapi":"3.0.3",
```

### info (REQUIRED)

| key | type | description |
| ------ | ------ | ------ |
| title | string | Short API Title / Name |
| description | string |  Description of the API and what it does |
| version | string | Version of the API |
| termsOfService | string(url) | (usually bolier plate - see below) |
| contact | object | (usually bolier plate - see below) |
| license | object | (usually bolier plate - see below) |

The "termsOfService", "contact" and "license" keys for most BGS data will be the same as OpenGeoscience e.g.

```javascript
"info":{
	"title":"NewAPI title",
	"description":"NewAPI description",
	"version":"0.0.1",
	"termsOfService":"//www.bgs.ac.uk/help/terms_of_use.html",
	"contact":{"name":"BGS Webmaster","email":"www-bgs@bgs.ac.uk"},
	"license":{"name":"Open Government Licence","url":"//www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"}
	}
```

*NOTE: If the data or service being provided is not clearly part of BGS OpenGeoscience, the "termsOfService", "contact" and "license" MUST be double-checked and approved before an API can be released.*

### servers (REQUIRED)

For most external APIs all we need here is the root URL of the API service (so that full API urls can be assembled with the endpoint "paths" data)

```javascript
"servers":[
    {"url":"//apis.bgs.ac.uk/NewAPI/"}
    ]
```

For internal APIs we can add more options to cover the various stages of development:

```javascript
"servers":[
    {"url":"//apis.bgs.ac.uk/NewAPI/","description":"Production"},
    {"url":"//testApis.bgs.ac.uk/NewAPI/","description":"Testing"},
    {"url":"//RandomVM123/NewAPI/","description":"Development"}
    ]
```

### components (REQUIRED)

| key | type | description |
| ------ | ------ | ------ |
| schemas | object | JSON Schema definitions of all properties in API responses or requests - referenced by "responses" and/or "parameters"  |
| parameters | object | Definitions of request parameters - referenced by "paths" - references "schemas" for property details |
| responses | object | Definitions of response objects - referenced by "paths" - references "schemas" for property details |
| examples | object | TODO |

#### components.schemas

TODO 

*(LINK TO STORE OF PRE-GENERATED SCHEMA DEFINITIONS HERE)*

#### components.parameters

TODO

#### components.responses

TODO

#### components.examples

TODO

*NOTE: The optional components keys "requestBodies", "headers", "securitySchemes", "links" and "callbacks"  are currently out-of-scope of this guidance*

### paths (REQUIRED)

The paths section of the specification defines the resource endpoints the API provides. Each path should have one or more operations to access a endpoint (get,post,put,patch,delete).
Below is an example of a get operation to retrieve an JSON array of subject data objects along with an expected response and the schema the json will follow. 

```yaml 
/subjects:
    get:
      summary: "Returns nested array of subject terms"
      description: "Returns nested array of document subjects as id,translation,description values from a hierarchical keyphrase list"
      responses:
        '200':
          description: "A JSON array of key value value triples"
          content:
            application/json:
              schema:
                properties:
                  "items":
                    type: array
                    items:
                      $ref: '#/components/schemas/HierarchicalDictionaryItem'
```

### externalDocs (OPTIONAL)

Links to External Documents are optional but can be very useful for the API consumer e.g. if a link to a WWW page with futher information about a dataset (scope, limitations etc.) is available 

```javascript
"externalDocs":[
	{"name":"About this data","url":"//www.bgs.ac.uk/data/dataset/home.html"}
	]
```	
	
