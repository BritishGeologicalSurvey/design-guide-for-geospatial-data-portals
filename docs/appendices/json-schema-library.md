# JSON Schema Library


User specified fields should be surrounded by quotations and are done so to differentiate between given OpenAPI fields for readability.
Sometimes it is logical to inherit schemas. allOf allows schemas to embed another schema as a subschema using the $ref syntax e.g. HierarchicalDictionaryItem contains the fields present in a DictionaryItem. 



## BGS Dictionary references (Lexicon, RCS, Map Sheets...)

* DictionaryItem:
      type: object
      properties:
        "id":
          type: string
        "translation":
          type: string
        "description":
          type: string
          
* HierarchicalDictionaryItem:
      type: object
      allOf:
      - $ref: '#/components/schemas/DictionaryItem'
      properties:
        "narrower":
          type: array
          items:
            $ref: '#/components/schemas/HierarchicalDictionaryItem'
                    
## Spatial properties (point, polygon, bbox, ...)
                      
* GeoJsonFeature:
      type: "object"
      required:
        - "type"
        - "geometry"
        - "properties"
      properties:
        "type":
          type: string
          enum:
          - Feature
        "geometry":
          description: "geojson geometry"
          externalDocs:
            description: "geometryGeoJSON schema defined by OGC"
            url: "https://raw.githubusercontent.com/opengeospatial/WFS_FES/master/core/openapi/schemas/geometryGeoJSON.yaml"
        "properties":
          type: object
          nullable: true
        "id":
          oneOf:
          - type: string
          - type: integer
      externalDocs:
        description: "featureGeoJSON schema defined by OGC"
        url: "https://raw.githubusercontent.com/opengeospatial/WFS_FES/master/core/openapi/schemas/featureGeoJSON.yaml"
        
* GeoJsonFeatureBoundingBox:
      type: "object"
      description: "GeoJson Feature object containing Polygon with 4 vertices"
      required:
        - "type"
        - "geometry"
        - "properties"
      properties:
        "type":
          type: string
          enum:
          - Feature
        "geometry":
          allOf:
          - $ref: '#/components/schemas/PolygonGeoJsonBoundingBox'
        "properties":
          type: object
          nullable: true
        "id":
          oneOf:
          - type: string
          - type: integer
      externalDocs:
        description: "based on featureGeoJSON schema defined by OGC"
        url: "https://raw.githubusercontent.com/opengeospatial/WFS_FES/master/core/openapi/schemas/featureGeoJSON.yaml"
        
        
* PolygonGeoJsonBoundingBox:
      type: object
      description: "GeoJson Polygon geometry with exactly 4 vertices"
      required:
        - type
        - coordinates
      properties:
        "type":
          type: string
          enum:
            - Polygon
        "coordinates":
          type: array
          items:
            type: array
            minItems: 4
            maxItems: 4
            items:
              type: array
              minItems: 2
              items:
                type: number
      externalDocs:
        description: "Based on PolygonGeoJson schema defined by OGC"
        url: "https://raw.githubusercontent.com/opengeospatial/WFS_FES/master/core/openapi/schemas/polygonGeoJSON.yaml"

### WGS84 >> GeoJSON

### BNG

## Metadata properties (title, description, author, ...)

### Paging

* PagingItem:
      type: object
      description: "object containing data related to linking large sets of response data"
      required: 
        - next
      properties:
        "next":
          type: string
          description: "url pointing to the next set of items returned"
        "previous":
          type: string
          description: "url pointing to the previous set of items returned"
        "total":
          type: integer
          description: "total number of items returned"
        "limit":
          type: integer
          maximum: 1000
          description: "the maximum number of items returned"
    #### More schema detail required for retreiving documents returning html and self data

## Dates and times (ISO xxxx)