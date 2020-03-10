# Common Patterns

The common patterns here cover all the core use cases supported by this guidance, and some additional use cases.

## Dictionary values

TODO : See issue #36

Dictionaries are lists of terms that are used to constrain attribute values in data. 
They are commonly used to populate selection lists for search forms and data entry forms, so your api will often need to support a request that
returns a sorted array of items. 
 * When used for a search form you may want to only include items that will result in a search hit.
 * When used for a data entry form you may want to exclude items that have been deprecated.

[DictionaryItem](appendices/schema-library.md#dic-item-1)

### Database implementation

BGS corporate database administrator (DBA) maintains a standard structure for simple dictionaries in the database, 
see http://bgsintranet/scripts/oracle/bgs_dic/ and the API guidelines follow on from this design.

Each table in the database is prefixed "DIC_", and must include the columns:

| | |
|---|---|
| CODE | short character or integer unique identifier; can be a mnemonic or abbreviation |
| TRANSLATION | a maximum 50 character label used as the display value for drop down lists |
| DESCRIPTION | a long character field providing the description or definition |
| STATUS | a single character code where C means current and O means obsolete


A hierarchical dictionary such as a taxonomy will commonly also have a link to a parent term or an associated table holding
many-to-many parent-child relations, but this is outside the scope of the dictionary database guidelines.

To select all items for a data entry option list, the table should be queried to get all items where `STATUS='C'`.

To select all items in use for a search criteria the distinct dictionary items need to be selected from a join between the dictionary and the table of items.
This table join should be done within the database, either in the creation of a de-normalised Query Layer object for all data needed by the API,
or in the creation of a dictionary subset table.


### OpenAPI specification 

**Request**
[/items](appendices/schema-library.md#items) endpoint meets [use case 1](main-content/introduction.md#use-case-1)

A request for dictionary items should use the plural name of the type of item in the dictionary as the request path.
e.g.
`/my-api-root/myDictionaryItems`

Use parameters to filter the reponse to get lists appropriate for a search form or a data entry form
e.g.

`my-api-root/exampleDictionaryItems?inUse=true`
`my-api-root/exampleDictionaryItems?status=CURRENT`

The values for these parameters can be set as defaults if your API only supports one of these implementations.


[/items/{itemID}](appendices/schema-library.md#itemid) endpoint meets [use case 3](main-content/introduction.md#use-case-3)

[/items?q=[string]](appendices/schema-library.md#q) endpoint meets [use case 4](main-content/introduction.md#use-case-4)

[/items?start_date=[date1]&end_date=[date2]](appendices/schema-library.md#start_date) endpoint meets [use case 5](main-content/introduction.md#use-case-5)

[/items?bbox=[int,int,int,int]](appendices/schema-library.md#bbox) endpoint meets [use case 6](main-content/introduction.md#use-case-6)

[/items?dic=[attribute,value]](appendices/schema-library.md#dic) endpoint meets [use case 7](main-content/introduction.md#use-case-7)

[/items?dic=[attribute1,value1,attribute2,value2]](appendices/schema-library.md#dic) endpoint meets [use case 8](main-content/introduction.md#use-case-8)

**TODO - extension**
These requests could be proxies to a common BGS vocabulary API  (not yet fully developed)

e.g. `my-api-root/exampleDictionaryItems -> dictionary-api-root/exampleDictionaryItems`
  
A request to a common dictionary service to get terms in use relevant for a particular search application would have to also pass 
through the name of the table or dataset that is the subject of the search, and consideration would need to be given to the database connection credentials used by the API implementation.

e.g. `dictionary-api-root/exampleDictionaryItems?inUseBy=my-api-query-layer`

**Used in request parameter**

**TODO - notes on how to specify single dictionary item as a search parameter, and multiple items**

**Response**
[Item](appendices/schema-library.md#item) endpoint meets [use case 2](main-content/introduction.md#use-case-2)


Standards exist for encoding dictionary data in linked data formats (SKOS-RDF), and there is an open project https://github.com/gbv/jskos that is defining a JSON schema for SKOS resources. 
Dublin Core metadata terms are well established can be applied to any resource.
**TODO agree this recommendation - NB not used like this in any APIs so far!**

| database column | Dublin Core like attribute names | SKOS like attribute names | comments |
| -- |  -- | |
| CODE |  identifier | notation |  | 
| TRANSLATION | name | prefLabel | can add @en for language labels |
| DESCRIPTION | description | definition | |
| STATUS | status | status | not directly mapped to SKOS or DCT |

For hierarchical dictionaries:
the array of child items should be put in property `narrower`
the array of parent items should be put in property `broader`

The full dictionary object should be returned in the response when it is an attribute of a data item.

See Schema library for the openAPI yaml and JSON for a [DictionaryEntity](appendices/json-schema-library.md#dictionary-entity-1) schema object.


### API Java implementation

The BGS Java restlet framework provides classes and interfaces to easily query and encode responses for standard database dictionaries. 
** TODO - extension Some dictionaries are used by multiple application so your API could service this request using a common BGS dictionary API or micro service**

### Python implementation

**TODO**

## Spatial Data

TODO : 
[here](https://github.com/opengeospatial/ogcapi-features/tree/master/core/openapi/schemas) is a series of OGC standard schemas
for presenting data including spatial data.


## Paging and Sorting

### Simple Paging - Nearly Static Data with Implicit Order

Assuming a dataset that changes slowly over time and that is of modest size. It is suitable to use a 'limit and offset' pattern to page through a list of items.
This involves allowing two parameters on the GET method for the list uri (see 'Limit and Offset Parameters' below) and including a paging node (see 'PagingItem Schema' below) in the response.

There are many other names used in API design for parameters that have the same purpose as 'limit and offset' but with a good description in the Openapi definition it is ok to use these short names.

The 'paging' node defined here tries to cover two ends of the API consumer spectrum, one end that can just wires up the discoverable urls to navigate the list, and the opposite end that would wish to derive a richer navigation.
So the 'next' and 'prev' give the bare minimum to navigate from the loaded page with 'first' and 'last' being generous additions. Whereas the 'total', 'limit' and 'offset' can be used to derive further navigation urls.


#### Openapi example

**[Example of simple paging](/appendices/api-example-simple-pagination)**

#### Openapi Snippets

In Openapi definition of the GET request for the list add this snippet

```javascript
        "parameters": [
          {
            "$ref": "#/components/parameters/Limit"
          },
          {
            "$ref": "#/components/parameters/Offset"
          }
``` 

And under its 'responses:200:content:application/json:schema' add this

```javascript
                  "properties": {
                    "rel": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "string"
                        }
                      }
                    },
                    "paging": {
                      "$ref": "#/components/schemas/PagingItem"
                    }
``` 


The components used in the snippets

Limit and Offset Parameters

```javascript
  "components": {
    "parameters": {
      "Limit": {
        "name": "limit",
        "in": "query",
        "description": "the number of items per page to return",
        "schema": {
          "type": "integer"
        }
      },
      "Offset": {
        "name": "offset",
        "in": "query",
        "description": "the number of items to ignore before including the items for this page",
        "schema": {
          "type": "integer"
        }
      }
    }
  }
``` 

PagingItem Schema

```javascript
  "components": {
    "schemas": {
      "PagingItem": {
        "type": "object",
        "description": "object containing data related to linking large sets of response data",
        "required": [
          "limit, total"
        ],
        "properties": {
          "next": {
            "type": "string",
            "description": "url to access the next page of items. Missing if there is no next page"
          },
          "prev": {
            "type": "string",
            "description": "url to access the previous page of items. Missing if there is no previous page"
          },
          "first": {
            "type": "string",
            "description": "url to access the first page of items. Missing if this is the first page"
          },
          "last": {
            "type": "string",
            "description": "url to access the next page of items. Missing if this is the last page"
          },
          "total": {
            "type": "integer",
            "description": "total number of items available"
          },
          "limit": {
            "type": "integer",
            "minimum": 1,
            "maximum": 1000,
            "description": "the maximum number of items returned for a page"
          },
          "offset": {
            "type": "integer",
            "description": "the number of items left out to give the first item on this page"
          },
          "all_items": {
            "type": "boolean",
            "description": "this page contains all available items"
          }
        }
      }
``` 

### Paging - Frequently Updated Data

TODO : See issue #33

## Caching

TODO : See issue #37

## SEO

TODO : See issue #20 (*right at the bottom!*)



---

(LINK TO LIBRARY HERE)