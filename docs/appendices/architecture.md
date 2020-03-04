## Architectural patterns
These patterns/constraints restrict the ways that the server should process and respond to client requests so that, by operating within these patterns, the service gains desirable non-functional properties, such as performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

Source: all patterns are adaptation of [Representational state transfer REST](https://en.wikipedia.org/wiki/Representational_state_transfer)

### Client-server architecture
The client–server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

Source: [Client–server model](https://en.wikipedia.org/wiki/Client-server_model)

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

## External Links

*  [Representational state transfer REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
*  [Client–server model](https://en.wikipedia.org/wiki/Client-server_model)
*  [Internet Date/Time Format RFC3339 / ISO8601](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)
*  [Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content RFC7231](https://tools.ietf.org/html/draft-ietf-httpbis-p2-semantics-26)
*  [OpenAPI Specification 3.0.3](https://swagger.io/specification/)
*  [JSON Schema](https://json-schema.org/specification.html)