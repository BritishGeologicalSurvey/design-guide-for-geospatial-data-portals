```javascript
{
  "openapi": "3.0.2",
  "info": {
    "description": "Open API specification for Dummy API",
    "version": "1.0.0",
    "title": "Dummy",
    "termsOfService": "https://www.bgs.ac.uk/help/terms_of_use.html",
    "contact": {
      "email": "enquiries@bgs.ac.uk"
    }
  },
  "servers": [
    {
      "url": "http://localhost:8080",
      "description": "Local desktop"
    }
  ],
  "paths": {
    "/getDepos": {
      "get": {
        "summary": "Returns list of deposits",
        "description": "Returns list of deposits with title as title",
        "responses": {
          "200": {
            "description": "A JSON array of summary metadata for deposits",
            "content": {
              "application/json": {
                "schema": {
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
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Deposit"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid search parameters"
          }
        },
        "parameters": [
          {
            "name": "simpleText",
            "in": "query",
            "description": "Free text that searches within many (but not all) fields of the item to filter the items returned. Uses boolean operators to search on all words in any order or on exact phrase if enclosed in double quotes",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "$ref": "#/components/parameters/Limit"
          },
          {
            "$ref": "#/components/parameters/Offset"
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PagingItem": {
        "type": "object",
        "description": "object containing data related to linking large sets of response data",
        "required": [
          "limit, total, offset"
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
      },
      "Deposit": {
        "type": "object",
        "required": [
          "id, title"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "description": "the unique key to the stored deposit"
          },
          "title": {
            "type": "string",
            "description": "the title of the stored deposit"
          }
        }
      }
    },
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
  },
  "externalDocs": {
    "description": "Find out more about Swagger",
    "url": "http://swagger.io"
  }
}
```