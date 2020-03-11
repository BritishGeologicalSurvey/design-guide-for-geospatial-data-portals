# Using OpenAPI

## Why use OpenAPI?

OpenAPI is a broadly adopted industry standard for describing modern APIs, overseen by the OpenAPI Initiative, an open-source collaboration project of the Linux Foundation.
An [OpenAPI definition](http://spec.openapis.org/oas/v3.0.3) is a JSON/YAML file that is stored in a web accessible location and describes how to use the API.

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

## Online tools to help create, validate and convert OpenAPI Documents

*  [Swagger Editor](https://editor.swagger.io/) - paste in YAML or JSON to convert and validate + basic editing tools
*  [Swagger UI](https://petstore.swagger.io/) - enter URL of an OpenAPI Document to view auto-generated documentation


## Anatomy of a BGS OpenAPI Document

The root of an API document **must** contain the following keys:

| key | type | description |
| ------ | ------ | ------ |
| **openapi** | string | OpenAPI Version - currently "3.0.3" |
| **info** | object |  API Description and terms  |
| **servers** | array |  API Server URL |
| **components** | object |  Reusable definitions to be used in "paths" object |
| **paths** | object | The available paths and operations for the API |

*NOTE: The optional "tags" and "security" keys are currently out-of-scope of this guidance*

### openapi `(Required OpenAPI + BGS)`  [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#versions)

This indicates the version of OpenAPI used and will currently (FEB 2020) be:
```javascript
"openapi":"3.0.3",
```

### info `(Required OpenAPI + BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#info-object)

| key | type | description |
| ------ | ------ | ------ |
| **title** | string | Short API Title / Name |
| **description** | string |  Description of the API and what it does |
| **version** | string | Version of the API |
| **termsOfService** | string(url) | (usually bolier plate - see below) |
| **contact** | object | (usually bolier plate - see below) |
| **license** | object | (usually bolier plate - see below) |

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

If an API serves data from one or more referenceable datasets, then add a **"x-datasets"** extension key into "info" section.

The which is an array of dataset objects:

```javascript
"info":{
    ...
	"x-datasets":{
	    {"title":"Dataset One","link":"METADATALINK1",...},
	    {"title":"Dataset Two","link":"METADATALINK2",...}
	    }
	}
```
**TODO:** define required and optional properties of a dataset object

### servers `(Required BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#server-object)

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

### paths `(Required OpenAPI + BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#paths-object)

Holds the relative paths to the individual endpoints and their operations. The path is appended to a URL from the Server Object in order to construct the full URL.

Wherever possible a path description should use "$ref" pointers to response, parameter and schema definitions.

### externalDocs `(optional)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#external-documentation-object)

Links to External Documents are optional but can be very useful for the API consumer e.g. if a link to a WWW page with futher information about a dataset (scope, limitations etc.) is available 

```javascript
"externalDocs":[
	{"name":"About this data","url":"//www.bgs.ac.uk/data/dataset/home.html"}
	]
```	
	
### components `(Required OpenAPI + BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#components-object)

| key | type | description |
| ------ | ------ | ------ |
| **schemas** | object | JSON Schema definitions of all properties in API responses or requests - referenced by "responses" and/or "parameters"  |
| **parameters** | object | Definitions of request parameters - referenced by "paths" - references "schemas" for property details |
| **responses** | object | Definitions of response objects - referenced by "paths" - references "schemas" for property details |
| **examples** | object | Definitions of example objects - referenced by responses or requests|

All schema, parameter, response and example definitions should follow their OpenAPI specifications:

---

### components.schemas `(Required BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#schema-object)

These definitions should follow [JSONSchema](https://json-schema.org/specification.html) syntax - the following keys are required:

| key | type | required | notes |
| ------ | ------ | ------ | ------ |
| **type** | string | YES |  |
| **title** | string | YES | short label - could be used as a column heading |
| **description** | string | YES | full description e.g. with acronyms expanded and including units | 

Additional keys (e.g. maxLength, maxItems, enum) should be used as necessary to refine the required data type. 

```javascript
"schemas":[
    "Offset":{
        "type":"integer",
        "title":"offset",
        "description":"The number of items to skip over before the first item returned",
        "minimum":0,
        "maximum":1000
        },
    "id":{
        "type":"string",
        "title":"document id",
        "description":"Unique document ID within the dataset"
        },
	...
	]
```	

Pre-generated schema definitions for many common uses can be cut-and-pasted from the **[JSON Schema Library](/appendices/json-schema-library)** 

---

### components.parameters `(Required BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#parameter-object)

All parameter definitions **MUST** provide one or more valid test values using either the **"example"** *(one)* or **"examples"** *(many)* keys. 
This allows for the generation of auto-generated test pages to offer users and external developers **working** example values to try out. 
It may also be used for automated testing of APIs.

```javascript
"parameters":[
    "Offset":{
        "name":"offset",
        "description":"The number of items to skip over before the first item returned",
        "in":"query",
        "example":0,
        "schema":{"$ref":"#/components/schemas/Offset"}
        },
    "id":{
        "name":"id",
        "description":"Unique document ID within the dataset",
        "in":"query",
        "required":true,
        "example":"AGLA900041",
        "schema":{"$ref":"#/components/schemas/id"}
        },
	...
	]
```	

Pre-generated parameter definitions for many common uses can be cut-and-pasted from the **[JSON Schema Library](/appendices/json-schema-library)** 

---

### components.responses `(optional - recommended BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#responses-object)

Response definitions should follow the OpenAPI standard.

Pre-generated response definitions for many common uses can be cut-and-pasted from the **[JSON Schema Library](/appendices/json-schema-library)** 

---

### components.examples `(optional - recommended BGS)` [:page_facing_up: OpenAPI Spec](http://spec.openapis.org/oas/v3.0.3#example-object)

Example definitions should follow the OpenAPI standard.

Pre-generated example definitions for many common uses can be cut-and-pasted from the **[JSON Schema Library](/appendices/json-schema-library)** 
	
---
	
*NOTE: The optional components keys "requestBodies", "headers", "securitySchemes", "links" and "callbacks"  are currently out-of-scope of this guidance*
