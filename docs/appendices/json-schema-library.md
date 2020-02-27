# JSON Schema Library

OpenAPI specification for a project can be viewed using Swagger Editor for easy readability. 
When creating a schema user specified fields should be surrounded by quotations and are done so to differentiate 
between given OpenAPI fields. Sometimes it is logical to inherit schemas and allOf allows schemas to embed another 
schema as a subschema using the $ref syntax.

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