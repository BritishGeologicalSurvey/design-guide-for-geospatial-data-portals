# Good enough!

The following constraints are the ideal for web API development from a functional perspective but not always from a business one. For example, if a feature is implemented that is never used then the resources spent on that feature can often be considered as wasted resources. For this reason, it is recommended that developers focus on a few quality endpoints that are 'Good Enough!' to satisfy the requirements.

The primary focus of development should be on design. A design developed solely to satisfy a set of requirements yet is not coupled with any particular consumer. A good design will be easily extendable with nice to have features later; when a more refined understanding of the different stakeholdings are known and appropriate resources are available.

As an example, a web API designed with to service a single or multi page web service (SPA/MPA) where a user explores data, much like a set of HTML pages with hyperlinks to other pages, may find adhering to HATEOAS by providing a range of hyperlinks. An embedded web API for a very specific purpose will probably have little use for additional links; only implementing if a clear need arises.
