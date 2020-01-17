# Introduction

* Purpose? Why?
* How?
* Where and where not to use?

## Goal

To make web APIs that are:
* Simple
* Intuitive
* Easy to explore
* Clearly defined
* Well documented
* Consistent
* Quick and easy to implement

## Good enough!

The following constraints are the ideal for web API development from a functional perspective but not always from a business one. For example, if a feature is implemented that is never used then the resources spent on that feature can often be considered as wasted resources. For this reason, it is recommended that developers focus on a few quality endpoints that are 'Good Enough!' to satisfy the requirements.

The primary focus of development should be on design. A design developed solely to satisfy a set of requirements yet is not coupled with any particular consumer. A good design will be easily extendable with nice to have features later; when a more refined understanding of the different stakeholdings are known and appropriate resources are available.

As an example, a web API designed with to service a single or multi page web service (SPA/MPA) where a user explores data, much like a set of HTML pages with hyperlinks to other pages, may find adhering to HATEOAS by providing a range of hyperlinks. An embedded web API for a very specific purpose will probably have little use for additional links; only implementing if a clear need arises.

## Architectural constraints
These constraints restrict the ways that the server should process and respond to client requests so that, by operating within these constraints, the service gains desirable non-functional properties, such as performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

Source: all constraints are adaptation of [Representational State Transfer][representational-state-transfer]

### Client-server architecture
The client–server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

Source: [Client server model][client-server-model]

### Statelessness
The client–server communication is constrained by no client context being stored on the server between requests. Each request from any client contains all the information necessary to service the request, and session state is held in the client.

### Cacheability
As on the World Wide Web, clients and intermediaries can cache responses. Responses must therefore, implicitly or explicitly, define themselves as cacheable or not to prevent clients from reusing stale or inappropriate data in response to further requests. Well-managed caching partially or completely eliminates some client–server interactions, further improving scalability and performance.

### Layered system
A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way. Intermediary servers may improve system scalability by enabling load balancing and by providing shared caches. They may also enforce security policies.

### Resource identification in requests
Individual resources are identified in requests. The resources themselves are conceptually separate from the representations that are returned to the client.

### Resource manipulation through representations
When a client holds a representation of a resource, including any metadata attached, it has enough information to modify or delete the resource (if it's a deletable resource).

### Self-descriptive messages
Each message includes enough information to describe how to process the message.

### HATEOAS: Hypermedia as the engine of application state
Having accessed an initial URI for the application a client should then be able to use server-provided links dynamically to discover all the available actions and resources it needs. As access proceeds, the server responds with text that includes hyper-links to other actions that are currently available. There is no need for the client to be hard-coded with information regarding the structure or dynamics of the service.

## Web API versioning
If there is a new version then consumers should expect that the whole API may have completely changed, from endpoint URLs to response formats. A new (major) version could, from another perspective, just be seen as a completely new web API. Thus a version 2 is no different from a new API which does the same thing.

There is the possibility that data versioning will be added to many datasets. From an end users perspective, multiple versions that need to provided together gives data navigation a lot more complex. This would also mean internal developers may have to support many different versions of an API where each is supporting different data versions. This will almost likely cause a lot of confusion and maintenance difficulties. For these reasons we thought best to only use minor versioning; for our web APIs at least.

### Majorless versioning
With majorless versioning the __major version number never changes or doesn't exist__. API breaking changes should be avoided at all costs, the majorless versioning approach helping to enforce this. When an API breaking change does occur it is usually because a new feature really can't fit due to bad initial API design or that the whole concept or purpose of the API has changed; both very suggestively point at the creation of a new API.

For many small changes and corrections new endpoints should be considered first, unless of course, almost all of the end points need to change; in which case a new web API might be appropriate. Adding a new endpoint and deprecating the previous one is also a common tactic to avoid going through the process of releasing a whole new version/API for just adding a new feature.

### Additions and bug fixes
Minor changes are those where the web API has been extended, perhaps with new endpoints or maybe new properties have been added to the responses. Patch changes are generally bug fixes. A change of either type should not break or change, in anyway, __correctly implemented__ front ends; if it does then its an API breaking change and thus a new API is required (or figure an alternative way to make the change).

### New web API name suggestions
A new name for the new web API will need to be considered but it shouldn't be too much hassle. As an example, here are some alternative names for the _'/gtf'_ (Geochronology and tracers facility) web API:
* _'/gtf2'_
* _'/geotf'_
* _'/geotrace'_
* _'/gtf-next-generation'_
* _'/gtf9000'_

_'/gtf2'_ suggests to users that it is the second version, which is absolutely fine and after considering the way people refer to popular software this is possible the best way forward. The _'2'_ is part of the name and does not have the same semantic meaning that a major version number has. Big software companies use this approach and you often find the number on the front of the box doesn't match the actual product version. For example, Windows 8 has the official version number 6.2. Perhaps they are coming at it from a marketing perspective but the idea is the same, to distinctly separate products.

## External Links

*  [representational-state-transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)
*  [client-server-model](https://en.wikipedia.org/wiki/Client-server_model)
*  [rfc3339](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)
*  [rfc7231](https://tools.ietf.org/html/draft-ietf-httpbis-p2-semantics-26)
*  [openapi-3-spec](https://swagger.io/specification/#dataTypes)
*  [openapi-3-json-schema](https://swagger.io/specification/#schema-object-98)  
*  [json-schema](http://json-schema.org/)

