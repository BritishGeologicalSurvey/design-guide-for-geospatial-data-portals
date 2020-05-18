# OGC Features API

Summary of the requirements/recommendations in OGC Features API that are relevant to BGS API guidance documentation.

"OGC API - Features - Part 1: Core" published also by ISO as "Geographic Information - Geospatial API for Features - Part 1: Core"

The Features API fits is one of a modular set of API standards, and implements the modules API Core and API Collections. API Tiles is another module which is in development.  

## Endpoints required by API Core

|--|--|--|--|
|Resource|Path|HTTP method|Notes|
|--|--|--|--|
|Landing Page | / |	 GET | Landing page is required |
| |/conformance	|GET	|Provides links to which standards this API conforms to (eg oas30, core, html, geojson, gmlsf0, tiles). NB OGC API standards are modular so this can be more than one.|
||/api	|GET	The OpenAPI3.0 spec (extendable for other api specification formats possible in future)|
||/links	|GET|	Relative links to other end points of the api|


## Endpoints required by API Collections 

/collections 

Feature collection metadata (equivalent to the list of layers available in a GIS, plus metadata about the collection of layers)

/collections/{collectionId}|{name}

Metadata about one feature dataset (equivalent to metadata about one layer/dataset in a GIS)

## Endpoints required by  API Features

/collections/{collectionId}/items

/collections/{collectionId}/items/{featureId}

### Not yet covered

 - Features with geometries in CRS other than that handled by geojson
 - Collection hierarchies
 - Creating/modifying features
 - More complex data models






