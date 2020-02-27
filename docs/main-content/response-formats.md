# API Response formats

An API can return almost any type of data, but *usually* returns some sort of *standard* text format that is well understood by browsers e.g. JSON or XML.

- Time-Series Data Formats (e.g [SOS](https://en.wikipedia.org/wiki/Sensor_Observation_Service))
- OGC XML Formats ([WFS](https://en.wikipedia.org/wiki/Web_Feature_Service), [WMS](https://en.wikipedia.org/wiki/Web_Map_Service), [WCS](https://en.wikipedia.org/wiki/Web_Coverage_Service), ...)
- ISO XML Formats (METADATA)
- Linked Data Formats ([RDF-XML](https://www.w3.org/RDF/), LD-JSON)
- Arbitrary JSON (often only used to support a single application)
- HTML (used for client-side-includes and by some JavaScript templating libraries)

## Index and meta data response format

Within BGS we serve a large amount of index and meta data to users. This accounts for more than 80% of application activity on www.bgs.ac.uk.

We have many existing use cases that are all very similar:

- Data is in a DB Query Layer (with maybe a couple of dictionaries)
- The Query Layer is an just index of maps/reports/rocks/fossils/... 
- Each item has relatively few simple properties
- Each item optionally has a link to an external resource (e.g. large image viewer or PDF download)
- API provides only "search", "full details" and "dictionary (dropdown)" endpoints

For these very similar (and repetitive) use cases, we have a response template that should be used if at all possible:

- **[Index Data JSON Format](main-content/json-format)** specification

Hopefully this will speed up development and introduce more consistency across these APIs
