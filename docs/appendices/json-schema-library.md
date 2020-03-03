# JSON Schema Library

This is a list of common properties between projects and to provide guidance on how to structure your schemas. 
Your project specific OpenAPI specification can be viewed using the [**Swagger Editor**](https://editor.swagger.io/) 
for easy readability and will expand on what is below. In the editor when creating a schema 
with user specified fields those fields should be surrounded by quotations to differentiate between 
given OpenAPI fields:

```
DictionaryItem:
      type: object
      properties:
        "id":
          type: string
        "translation":
          type: string
        "description":
          type: string
```

Sometimes it is logical to inherit schemas and OpenAPI allow schemas to embed another schema as a 
subschema using the allOf keyword. $ref is used to make reference to sections in the API, for 
example a HierarchicalDictionaryItem contains a nested HierarchicalDictionaryItem:

```
HierarchicalDictionaryItem:
      allOf:
      - $ref: '#/components/schemas/DictionaryItem'
      type: object
      properties:
        "narrower":
          type: array
          items:
            $ref: '#/components/schemas/HierarchicalDictionaryItem'
```

## BGS Dictionary references (Lexicon, RCS, Map Sheets...)

```
A heirarchical dictionary item contains an array of one other heirarchical dictionary item.

HierarchicalDictionaryItem{
    id              string
    translation     string
    description     string
    narrower        Array<HierarchicalDictionaryItem>
}
```

## Spatial properties (point, polygon, bbox, ...)
                      
```
GeoJsonFeature{
    id              string or integer
    type*           string
                    enum[Feature]
    geometry*       
    properties*     nullable
}
```

```
GeoJsonFeatureCollection{
    type*           string
                    enum[FeatureCollection]
    features*       GeoJsonFeature
    timeStamp       string($date-time)
    numberMatched   integer
                    minimum: 0
    numberReturned  integer
                    minimum: 0
}
```

```
GeoJson Feature object containing Polygon with 4 vertices. 

GeoJsonFeatureBoundingBox{
    id              string or integer
    type*           string
                    enum[Feature]
    geometry*       PolygonGeoJsonBoundingBox
    properties*     nullable
}
```

```
GeoJson Polygon geometry with exactly 4 vertices.

PolygonGeoJsonBoundingBox{
    type*           string
                    enum[Polygon]
    coordinates*	Array< Array< param1:integer,param2:integer>, ... >
                    minItems: 4
                    maxItems: 4
                    A 2d-array with 4 arrays containing a maximum of 2 integers to represent the cooradinates of the 4 vertices of the polygon.

}
```

### WGS84 >> GeoJSON

### BNG

## Metadata properties (title, description, author, ...)

``` 
Object containing data related to linking large sets of response data.

PagingItem{
    next*       string
                url pointing to the next set of items returned
    previous    string
                url pointing to the previous set of items returned
    total       integer
                total number of items returned
    limit       integer
                maximum: 1000
                the maximum number of items returned    
}
```

## Dates and times (ISO xxxx)