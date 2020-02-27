# API and Data versioning

## Data Versioning (provenance)

TODO

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

