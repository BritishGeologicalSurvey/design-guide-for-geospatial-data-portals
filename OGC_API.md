# OGC Features API

**"OGC API - Features - Part 1: Core" published also by ISO as "Geographic Information - Geospatial API for Features - Part 1: Core"**

Summary of the requirements/recommendations in OGC Features API https://www.ogc.org/standards/ogcapi-features that are relevant to BGS API guidance documentation.


OpenAPI schema http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/ogcapi-features-1.yaml  (contains links to modular .yaml for schemas, parameters etc including GeoJSON response schemas)

The Features API fits is one of a modular set of API standards, and implements the modules API Core (applicable to all Web APIs)
and API Collections. API Tiles is another module which is in development. 

The intention is that the combination of the OGC Features API and the OpenAPI spec can be used to meet two use cases:
1. Consumers who know the OGC standards and by knowing the conformance of an API are able to interact with the resources without necessarily reading the OpenAPI spec
2. Consumers who do not know the OGC standard but are able to use the provided OpenAPI spec to interact with the resources 

## Endpoints 

|Resource|Path|HTTP method|OGC module|Notes|
|---|---|---|---|---|
|Landing Page | `/` |GET | Core | Landing page is required, returns http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/landingPage.yaml|
|Conformance declaration|/conformance	    |GET	|Core|Provides links to which standards this API conforms to (eg oas30, core, html, geojson, gmlsf0, tiles). NB OGC API standards are modular so this can be more than one.|
||`/links`	    |GET|   Core|Must contain  `service-doc` and `service-desc` links to the OpenAPI spec document **[TODO - is there a standard path this should be provided at e.g. /api or /doc ?]** Must contain a `conformance` link to  `/conformance`. Must contain a `data` link to `/collections`. May contain other relative links from RFC 8288 (Web Linking)|
||`/collections` | GET |Collection|Array of all collections, see Collections schema. |
||`/collections/{collectionId}`|GET|Collection|Metadata about one feature dataset, see Collection schema|
||`/collections/{collectionId}/items`|GET|Feature|Array of features, filtered by query parameters|
||``/collections/{collectionId}/items/{featureId}`|GET|Feature|Detail of one Feature, see Feature schema|

## Collections schema

Array of collections

See http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/collections.yaml

## Collection schema

A collection is a dataset with attributes:

- required: collectionId
- required: list of CRS, the first being the default which is WGS 84 with axis order longitude/latitude
- optional title and description
- optional spatiotemporal extent (can also be used for extents in other dimensions e.g. pressure). Single bounding box, single time interval only.
- optional: indicator of the type of items, default='feature'
- recommended :describedBy linking to a document with structure or semantics of the e.g. xml schema, RDF schema, OWL
- recommended: links property includes a relation of type `license`

See http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/schemas/collection.yaml


## collections/{collectionId}/items query parameters

 - bbox : NB matches all features in the collection that are not associated with a location
 - datetime : NB matches all features in the collection that are not associated with a timestamp or interval
 - limit : the page size for paged access, in which case there should be prev/next page links. 
 - FeatureId
 
If multiple query parameters are used, only features matching all the criteria are in the result set, i.e. the logical operator between the predicates is 'AND'

See http://schemas.opengis.net/ogcapi/features/part1/1.0/openapi/parameters/

## collections/{collectionId}/items response

May include

 - numberMatched
 - numberReturned
 
## Feature schema
 
A feature is an item in a dataaset

Attributes:
  
  [geometry] - NB unless client specifically requests a different CRS, all spatial geometries shall be returned in WGS 84 longitude/latitude for geometries without height information, and WGS 84 longitude/latitude plus ellipsoidal height for geometries with height information

## Link relations beyond RFC 8288

items: refers to a resource providing members of the collection

conformance: refers to a resource that identifies the specifications that the context conforms to

data: indicates that the links context is a distribution of a dataset that is an api and refers to the root resource of the dataset in the API
**[TODO - explain better what the difference between items and data is !]**

## Response codes

Server must respond with 400 if request url includes a query parameter that is not specified in the API definition or has an invalid value, e.g. if limit is not an integer, bbox does not have 4 or 6 numbers or does not form a bounding box, datetime is not a value timestamp or time interval

## Encodings

HTML recommended

GeoJSON recommended where applicable

GML supported for other CRS or more complex geometry

200-response for media type text/html should include schema.org annotations

## Security considerations

Useful section, not copied here; references http://cwe.mitre.org/data/index.html

## Not yet covered

 - Features with geometries in CRS other than that handled by geojson
 - Collection hierarchies
 - Creating/modifying features
 - More complex data models
 - Additional conformance classes to enable safe paging (ie same response from repeat request with same paging parameters


