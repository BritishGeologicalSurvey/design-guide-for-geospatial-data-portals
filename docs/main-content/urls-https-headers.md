# URLs, HTTP and Headers

## URL endpoints
A consistent and intuitive URL design is critical for making web APIs usable. The templates for the endpoints were designed adhering as much as possible to the following principles:
* Short as possible
* Easy to read
* Unambiguous
* Consistent

With the following as guidelines for achieving them:
* Using a single segment where possible, e.g. `/samples`
* Appending a dynamic segment to the resource name to target a specific item, e.g. `/samples/123`
* Putting the resource name as the last non-dynamic segment of the resource path, e.g. `/sensors/123` _returns sensors_, `/sensors/123/measurements` _returns measurements_
* Declaring everything, including dynamic parameters, as lowercase
* Resource names should be plural
* Resource names should be as clearly defined as possible from a semantic perspective so it cannot misinterpreted or be confused with other resources

Separating words within segments of URLs with a common symbol is often done to introduce human readability. In the context of URLs, the current common trend is that underscores `_` are viewed as word joiners; where two words are being joined together to make one word but an underscore has been introduced between as a visual aid. Hyphens, are viewed as word separators, i.e. a replacement for spaces. Apparently, web document indexing systems parse URLs with hyphens into meaningful words better than those with underscores. This apparent advantage relates to web APIs very little and the systems that index web documents are advanced enough that the choice probably makes no difference. But as expected, web developers switched to using hyphens in an attempt to boost search engine hits. All that being said, hyphens are recommended as word separators in URLs, only to maintain consistency with current day conventions.

The following are common URL templates, with examples, that most endpoints should match:
```
/resource
/resource/item-id
/parent-resource/item-id/resource

/sites
/sites/123
/sites/123/sensors
```

Most resources are stored with a unique identifier so that they can be referenced out of context. However, there may be resources that do not have composite (compound?) IDs and some context is required, in these cases sub item IDs are permissible:
```
/parent-resource/parent-item-id/resource/item-id

/sites/123/sensors/456
```

Sometimes it might be difficult to give a single non-ambiguous name to a resource, especially if there are other similar resources. In these cases it's acceptable to prefix a segment to a group of related endpoints for clarity. Try to be consistent and avoid ambiguity, if a group prefix is required for one related group of endpoints then each related group should have a prefix.
```
/group/resource/123

/data-sources/sites/123
/processing-centres/sites/123
```

### API Versioning

[Read more about API versioning here](/introduction#web-api-versioning)


## Readonly Methods

### GET
Get or search for data using only the URL to express parameters. Should exactly match JSON `query` object parameters for a POST request. Since it is not viable for a GET request to include JSON the parameters should be provided as a query string.

Notes and guidelines:
* Can be used via the browsers address bar (address bar friendly)
* Easy for users of all types to modify
* Easily sharable amongst non-technical stakeholders and social media
```
http://api.bgs.ac.uk/gtf?xmin=-1&ymin=53&xmax=1&ymax=53&sampletypes=rock;soil;bone;shell;hair;feather
```

### POST (GET by POST)
Get or search for data using the request body to express parameters. Should exactly match query parameters for a GET request (except for the complex ones). `query=true` must be added as the only query parameter to ensure the POST can be distinguished from a standard resource creation POST.

Notes and guidelines:
* Safely supports large request parameters
* Easily allows for hierarchical and complex parameters
* __No__ query string parameters, except `query=true`, should be placed in the URL and any found there should be ignored. Having to parse parameters from multiple locations raises awkward questions about priority, requires more implementation, makes it easier to introduce bugs and presents the user with unnecessary choices

### HEAD (Optional)
Same as a GET request except only the headers are returned. Avoids transferring, and in some cases processing, large datasets when only the header information is required by the user. Often used to check if an endpoint is alive so its best to set no caching in return headers.

## Writable Methods
For resource modification the following methods are available:

Method | Description
:---: | :---
POST | Used to create a new resource item. The `query` query parameter is used to distinguish between __GET by POST__ and **Create by POST** requests. It can be omitted but if set must not have the value `true`
PUT | Used to update a resource item
DELETE | Used to delete a resource item

## HTTP Headers
Useful request and response headers are usually provided automatically by most development frameworks and software systems. Here are a few important ones and a few that may need to be added manually such as those that control caching:

### Request headers
Key | Description | Example
:--- | :--- | :---
Accept | Content-Types that are acceptable for the response | `Accept: application/json`
Authorization | Authentication credentials for HTTP authentication | `Authorization: Basic abcdefghijklmnopqrstuvwxyz123456`
Cache-Control | Used to specify directives that must be obeyed by all caching mechanisms along the request-response chain | `Cache-Control: no-cache`
If-None-Match | Allows a 304 Not Modified to be returned if content is unchanged | `If-None-Match: "737060cd8c284d8af7ad3082f209582d"`

### Response headers
Key | Description | Example
:--- | :--- | :---
Content-Type | The MIME type of this content | `Content-Type: text/html; charset=utf-8`
Access-Control-Allow-Origin | Specifying which web sites can participate in cross-origin resource sharing | `Access-Control-Allow-Origin: http://www.example.com`
Access-Control-Allow-Methods | Specifying which HTTP methods can participate in cross-origin resource sharing | `Access-Control-Allow-Methods: GET, POST`
Access-Control-Allow-Headers | Specifying which HTTP headers can participate in cross-origin resource sharing (some headers are always allowed) | `Access-Control-Allow-Headers: Cache-Control`
Cache-Control | Tells all caching mechanisms from server to client whether they may cache this object. It is measured in seconds | `Cache-Control: max-age=3600`
Content-Length | The length of the response body in octets (8-bit bytes) | `Content-Length: 348`
Content-Disposition | An opportunity to raise a "File Download" dialogue box for a known MIME type with binary format or suggest a filename for dynamic content | `Content-Disposition: attachment; filename="fname.ext"`
Date | The date and time that the message was sent (format: [RFC7231][rfc7231]) | `Date: Tue, 15 Nov 1994 08:12:31 GMT`
Last-Modified | The last modified date for the requested object (format: [RFC7231][rfc7231]) | `Last-Modified: Tue, 15 Nov 1994 12:45:26 GMT`

## Response Codes
Most HTTP response codes are for fairly specific use cases and our web APIs are unlikely to require most. The number of HTTP response codes should be limited in order to avoid causing the consumer to handle lots of different eventualities. They will just implement a catch all in any case but its useful during development to have a few different ones. Only the following codes should be used unless there is good reason to use extra:

__Warning:__ The 'reason phrases' or short descriptions defined in the official HTTP specification can be highly misleading. Make sure to double check the meaning with our friend Google.

Code | Reason phrase | Description
:---: | :--- | :---
__200__ | OK | Successfully carried out the request
201 | Created | Successfully carried out the creation of a new resource
\*304 | Not Modified | Often handled by development frameworks but responses may need to be checked and code specifically by the developer
**400** | Bad Request | General request failure and its the clients fault
\*401 | Unauthorised | Called 'unauthorised' but officially defined as 'unauthenticated'. The user has not provided authentication credentials or the ones provided are not valid
\*403 | Forbidden | The server has __authenticated__ the client (knows who they are) but they are not **authorised** (don’t have permission) to access the requested resource
\*404 | Not Found | The requested resource could not be found. Should not be confused with not having any results to return; if there are no results matching the search criteria then a 200 response code should be returned but with no results. This code can also be used to hide endpoints that only authorised users should know exists
415 | Unsupported Media Type | The request entity has a media type which the server or resource does not support. E.g. they sent the request body as XML and not JSON
__500__ | Internal Server Error | General request failure and its the servers fault
501 | Not Implemented | The server either does not recognize the request method, or it lacks the ability to fulfill the request. Usually this implies future availability e.g. it has been defined in the public specification for the service but has not yet been implemented

\* Hopefully the API management systems and choice of frameworks remove the need to use these response codes in the actual web API.
