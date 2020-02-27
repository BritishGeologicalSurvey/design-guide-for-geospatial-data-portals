# URL endpoints

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

[Read more about API versioning here](main-content/versioning-apis)



