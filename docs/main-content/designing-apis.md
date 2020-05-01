# Designing APIs

## User research

In order to design an API that is useful and easy to use it is important to understand the context in which it will be used and who will use it.

To get more clarity on the use-cases and requirements you can ask the following questions:

* Who is your API audience?
* What do they want from the API?
* How will they use the API?

Following the principles outlined in this documentation will help you:

1. Design the **right thing**
2. Design the **thing right**

## API user experience

> In the API space, we build something on a machine for a machine to use and this is wrong because there are people on the other side 
> of API clients.
>
> *- Ronnie Mitra*

To help make the developer user experience better you can follow the usability rules defined by [Peter Morville](https://semanticstudios.com/about/) known as [UX Honeycomb](https://semanticstudios.com/user_experience_design/).

![UX Honeycomb](../_media/ux-honeycomb.png "UX Honeycomb")

1. **Useful**: Is the API useful from an end user’s point of view?
2. **Usable**: Can the API be quickly used by a developer and provide easy-to-use functionality?
3. **Desirable**: Is the functionality provided by the API something that generates desire in developers and end users?
4. **Findable**: Can the API documentation be found easily, and can developers start using it immediately?
5. **Accessible**: Can the API provide functionality for end users who have technical constraints/limitations in consuming it?
6. **Credible**: Is the data provided by the API trustworthy?
7. **Valuable**: Does the API contribute to the company’s bottom line and improve customer satisfaction?

## Standards and Best Practice

One of the ways of ensuring your API meets common user requirements is by using appropriate standards, such as published by 
W3C, OGC, ISO/BSI or domain specific standards bodies. Following these means your API can be easily consumed by the widest audience
and often makes it available for a range of third party client software.

These guidelines for BGS implement the following international recommendations, which we advise you to read.

* [W3C Data on the Web Best Practices](https://www.w3.org/TR/dwbp/#dataAccess), particularly
    * [Data Access guidelines](https://www.w3.org/TR/dwbp/#dataAccess)
    * [Data Access APIs guidelines](https://www.w3.org/TR/dwbp/#accessAPIs)
    * [API example](https://www.w3.org/TR/dwbp/dwbp-api-example.html)
* [W3C Spatial Data on the Web Best Practices](https://www.w3.org/TR/sdwbp)
* [OGC Feature API](https://github.com/opengeospatial/ogcapi-features)
    
Other domain specific standards may apply to certain data types e.g. Sensor data, metadata.
BGS has a dedicated spatial data standards expert (Edd Lewis) who you can seek advice from. 

## Other design considerations

 * Design for extensibility - good enough for now, add more backwards compatible functionality later
 * Do not necessarily mirror the database structure
 * Appropriate abstractions
 * Level of detail in payloads
 * Flexibility of payloads
 * How nested/hierarchical/graph data structures are handled:
   *  Are they flattened.
   *  Lists of child IDs, followed by requests for specific children.
   *  What if it's cyclic - how do we break the cycle.


Non-functional considerations (thought should be given to these - even if it turns out they are handled by infrastructure):

 * Security
 * Logging/monitoring/auditing
 * Deployment
 * Performance
 * Public/Private data
 * Caching (especially of common dictionary calls)
 * Paging - particulalry of hot data
 * Data versioning (provenance)
 * A well defined folder structure is indistinguishable from a read-only REST API (and far more reliable) and could be considered for samll collections of cold data.

## Naming conventions

### URLs

Each API should have a short but descriptive root name in camel case. 
The name chosen will be used as the root "folder" in all API calls, so it must be URL compatible string - for widest compatibility use [ASCII characters 040-255](https://en.wikipedia.org/wiki/ASCII) only.

** TODO ** Your API may also be assigned to a collection of APIs and be made accessible as a subfolder under one or more collection folders. This behaviour will be handled by the proxy 
** TODO - will it ? add link to proxy section **

See [URL endpoints](main-content/urls-https-headers) for guidelines on creating the API endpoint paths that will be available under this root URL. 

There is no requirement for the root folder or any URLs to be transparent to the user;
most of the time this will be coded once in a client application and the end user won't be aware of it.
However, provding a degree of intuitiveness and predictability with the urls does help developers and testers.

### Parameters and response objects

Names for some common query parameters and response objects are defined by the OGC Feaature API standard, the OpenAPI specification and further by
BGS in these guidelines. See the reference templates for more detail.



