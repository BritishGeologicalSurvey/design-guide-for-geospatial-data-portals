# Designing APIs

## Design process

("Design process overview" see [comments from Chris on issue #20](https://kwvmxgit.ad.nerc.ac.uk/apis/api-guidance-docs/issues/20))

TODO

## Design considerations

The following constraints are the ideal for web API development from a functional perspective but not always from a business one. For example, if a feature is implemented that is never used then the resources spent on that feature can often be considered as wasted resources. For this reason, it is recommended that developers focus on a few quality endpoints that are 'Good Enough!' to satisfy the requirements.

The primary focus of development should be on design. A design developed solely to satisfy a set of requirements yet is not coupled with any particular consumer. A good design will be easily extendable with nice to have features later; when a more refined understanding of the different stakeholdings are known and appropriate resources are available. The design allows to iterate more easily and to perform what-if analysis. Also, making changes to the API in the design stage is much easier.

As an example, a web API designed with to service a single or multi page web service (SPA/MPA) where a user explores data, much like a set of HTML pages with hyperlinks to other pages, may find adhering to HATEOAS by providing a range of hyperlinks. An embedded web API for a very specific purpose will probably have little use for additional links; only implementing if a clear need arises.

![API Design Process by Postman](../_media/api-design-process.png "API Design Process by Postman")

## Naming APIs

A new name for the new web API will need to be considered but it shouldn't be too much hassle. As an example, here are some alternative names for the _'/gtf'_ (Geochronology and tracers facility) web API:
* _'/gtf2'_
* _'/geotf'_
* _'/geotrace'_
* _'/gtf-next-generation'_
* _'/gtf9000'_

_'/gtf2'_ suggests to users that it is the second version, which is absolutely fine and after considering the way people refer to popular software this is possible the best way forward. The _'2'_ is part of the name and does not have the same semantic meaning that a major version number has. Big software companies use this approach and you often find the number on the front of the box doesn't match the actual product version. For example, Windows 8 has the official version number 6.2. Perhaps they are coming at it from a marketing perspective but the idea is the same, to distinctly separate products.

## Best Practice

* [W3C - Data Access guidelines](https://www.w3.org/TR/dwbp/#dataAccess)
* [W3C - Data Access APIs guidelines](https://www.w3.org/TR/dwbp/#accessAPIs)
* [W3C - API example *as used in guidelines*](https://www.w3.org/TR/dwbp/dwbp-api-example.html)

## User research

In order to design an API that is useful and easy to use, it is important to understand the context in which it will be used and who will use it.

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

