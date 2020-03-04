# API Response formats

An API can return almost any type of data, but *usually* returns some sort of *standard* text format that is well understood by browsers e.g. JSON or XML.

- Time-Series Data Formats (e.g [SOS](https://en.wikipedia.org/wiki/Sensor_Observation_Service))
- OGC XML Formats ([WFS](https://en.wikipedia.org/wiki/Web_Feature_Service), [WMS](https://en.wikipedia.org/wiki/Web_Map_Service), [WCS](https://en.wikipedia.org/wiki/Web_Coverage_Service), ...)
- ISO XML Formats (METADATA)
- Linked Data Formats ([RDF-XML](https://www.w3.org/RDF/), LD-JSON)
- Arbitrary JSON (often only used to support a single application)
- HTML (used for client-side-includes and by some JavaScript templating libraries)

## Template response formats

For APIs with the functionality outlined in [https://kwvmxgit.ad.nerc.ac.uk/apis/api-guidance-docs/blob/use-cases-update/docs/main-content/introduction.md#core-use-cases],
we have templates for all the expected response objects:

- **[Index Data JSON Format](main-content/json-format)** specification

Hopefully this will speed up development and introduce more consistency across these APIs
