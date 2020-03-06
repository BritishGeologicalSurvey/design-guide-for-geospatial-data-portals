# Schema Library

<div id="dictionary-entity-1" class="schema-container" data-name="DictionaryEntity">
    todo: DictionaryEntity schema
</div>

This is a list of common properties between projects and to provide guidance on how to structure your schemas. 
Your project specific OpenAPI specification can be viewed using the [**Swagger Editor**](https://editor.swagger.io/) 
for easy readability and will expand on what is below. In the editor when creating a YAML schema user
 specified fields should be surrounded by quotations to differentiate between 
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

## Paths

<div id="items" class="path-container" data-name="/items"></div>

<div id="itemid" class="path-container" data-name="/items/{itemID}"></div>

/items/{itemID} endpoint schema reference is located below:

<div id="item" class="schema-container" data-name="Item"></div>


## Parameters

<div id="bbox" class="param-container" data-name="bbox"></div>
<div id="q" class="param-container" data-name="q"></div>
<div id="start_date" class="param-container" data-name="start_date"></div>
<div id="end_date" class="param-container" data-name="end_date"></div>
<div id="dic" class="param-container" data-name="dic"></div>
<div id="itemId" class="param-container" data-name="itemId"></div>


## BGS Dictionary references (Lexicon, RCS, Map Sheets...)

<div id="dic-item-1" class="schema-container" data-name="DictionaryItem"></div>

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

<div id="id1" class="schema-container" data-name="HierarchicalDictionaryItem"></div>

## Spatial properties (point, polygon, bbox, ...)

<div class="schema-container" data-name="GeoJsonFeature"></div>
<div class="schema-container" data-name="GeoJsonFeatureCollection"></div>
<div class="schema-container" data-name="GeoJsonFeatureBoundingBox"></div>
<div class="schema-container" data-name="itemId"></div>

### WGS84 >> GeoJSON

### BNG

## Metadata properties (title, description, author, ...)

<div class="schema-container" data-name="PagingItem"></div>


## Dates and times (ISO xxxx)