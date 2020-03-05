# Common Patterns

Guidance is provided here ... consistency ... speed up developemnt ...

## Paging and Sorting

### Simple Paging - Nearly Static Data with Implicit Order

Assuming a dataset that changes slowly over time and that is of modest size. It is suitable to use a 'limit and offset' pattern to page through a list of items.
This involves allowing two parameters on the GET method for the list uri (see 'Limit and Offset Parameters' below) and including a paging node (see 'PagingItem Schema' below) in the response.

There are many other names used in API design for parameters that have the same purpose as 'limit and offset' but with a good description in the Openapi definition it is ok to use these short names.

The 'paging' node defined here tries to cover two ends of the API consumer spectrum, one end that can just wire up the discoverable urls to navigate the list, and the opposite end that would wish to derive a richer navigation.
So the 'next' and 'prev' give the bare minimum to navigate from the loaded page with 'first' and 'last' being generous additions. Whereas the 'total', 'limit' and 'offset' can be used to derive further navigation urls.


#### Openapi example

**[Example of simple paging](/docs/api-example-simple-pagination.json)**

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
  }``` 

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
            "description": "url to access the next page of items"
          },
          "prev": {
            "type": "string",
            "description": "url to access the previous page of items"
          },
          "first": {
            "type": "string",
            "description": "url to access the first page of items"
          },
          "last": {
            "type": "string",
            "description": "url to access the next page of items"
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
      }``` 

### Paging - Frequently Updated Data

TODO : See issue #33

## Caching

TODO : See issue #37

## SEO

TODO : See issue #20 (*right at the bottom!*)

## Dictionaries 

TODO : See issue #36

## Spatial Data

TODO : 

---

(LINK TO LIBRARY HERE)