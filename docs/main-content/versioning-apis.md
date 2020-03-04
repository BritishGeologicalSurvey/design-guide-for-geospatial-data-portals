# API and Data versioning


## Web API versioning

### Recommendation (BGS)

Follow the approach outlined by https://semver.org/

To summarise:

Given a version number MAJOR.MINOR.PATCH, increment the:

 * MAJOR version when you make incompatible API changes,
 * MINOR version when you add functionality in a backwards compatible manner, and
 * PATCH version when you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


Examples:


www.company.com/api/v0/blah (v0, anything goes this is initial development, maybe only visible internally)

www.company.com/api/v1/blah (v1, public API is locked in, any breaking changes result in a new major version)

www.company.com/api/v2/blah (v2, breaking changes, essentially a new public API)

Minor and Bug versions are not API breaking.

### Implementation in OpenAPI Specification

The API version label must be put in the OpenAPI **required** field:

 **"info.version"** 

NB not to be confused with another  **required** field:

 **"version"** which is to hold the "OpenAPI Specification Version"

**TODO - (extension) include links to previous/replacement/latest api versions ?**

## Data Versioning (provenance)

The source data provided by an API is usually not static.  The same API request submitted at a different time may return a different response. 
For some users it is important to know what version of the data is returned in the response.

The data versioning schedule and labelling system will be decided by the data managers rather than the API designers.
For any published datasets there should exist a published metadata record which includes an attribute giving a value for the
frequency of update of the data. 

The datasets used in our core use case for these guidelines are often:
 * "continually updated" (which in reality can mean sporadic periods of activity)
 * not assigned version labels
 * updated for external access on a regular basis, usually nightly
 * the database Query Layer should store the datetime stamp of the last update
 
For this sort of versioning regime, the datetime stamp of the database update should be used as the dataset version label.

Other datasets are periodically updated and assigned version labels by the data managers. 

### Recommendation (BGS)

The dataset version label should be published with each API response.

If there is no inherent dataset version then the datetime stamp of the latest database change should be used as the dataset version.

**TODO (extension) how to support requests for a specific version of the data, i.e. to duplicate the response they would have got on a particular date**

Check that each dataset used in an API has a published metadata record and the update frequency is declared in it. 

Publish a link to the metadata for each dataset in the openAPI document.

### Implemenation in OpenAPI Specification

There is no official place in the OpenAPI Specification to put the "Dataset Version(s)" but it does allow extensions ...

So we are allowed to put an array of dataset objects (name, version...) into the "info" section as long as we prefix the new key with "x-" e.g. "x-datasets"

```...
"version":"3.0.3",
"info":{
    "version":"1.0.0",
    "x-datasets":[
        {"name":"Lexicon","version":"3.0","licence":"XXX",...},
        {"name":"RCS","version":"3.2","licence":"XXX",...}
        {"name":"SOBI","version":"2020-02-28-22:00","licence":"XXX",...}
        ],   
    ...
    },
```




**TODO - how to link to the metadata record for each dataset used ? instead of array above ? as another property of the array ?**
