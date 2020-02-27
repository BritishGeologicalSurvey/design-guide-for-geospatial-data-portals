# Introduction


## Purpose

The goal of these guidelines is to help BGS application developers create web APIs that are:

* **Fit for purpose** -  by good design and understanding of user needs, and architecture that provides non-functional requirements
* **Sufficiently documented** - by using OpenAPI 
* **Consistent and predictable in behaviour**  - by re-using patterns for architecture, query parameters, response data schemas, versioning
* **Quick and easy to implement** - by providing the boiler plate code and libraries that handle the architecture and repeatable stuff so you only have to code the parts that are particular to you

## Scope

These guidelines are intended for use in making RESTful (or at least RESTish) APIs that return relatively simple data as JSON. 

They are primarily concerned with open public APIs that provide metadata about and access to online resources such as images and downloadable datasets.

There are alternative API approaches that may be better suited for other use cases e.g. [GraphQL](https://graphql.org/), [gRPC](https://grpc.io/), or [Linked Data](http://linkeddata.org/).

## Resources

- Get off to a running start with a Reference Implementation in [Java](reference-implementations/java.md), [Node](reference-implementations/node.md) or [Python](reference-implementations/python.md)
- [JSON Schema Library](appendices/json-schema-library.md) A cut-and-paste library of Schemas for commonly used parameters and properties. Use these to quickly generate consistent OpenAPI specifications.
 

## Use cases covered

These guidelines and implementation examples are included to enable you to provide any of the following functionality for an API 
that provides access to a catalogue of online resources: 

1. Request all items and return JSON array of data objects

 1.1. return the response array in pages of a configurable size

2. Provide attributes within each data object in the array

 2.2. an integer attribute

 2.2. a string attribute

 2.3. a bounding box attribute in geojson 

 2.4. a point geometry attribute in geojson

 2.6. a dictionary object (code,translation,description)

 2.7. a URL attribute to download or view the resource

 2.8. a date/time attribute

3. Request all items where the geometry is contained within a specified bounding box, returning the same response as 1

4. Request all items where the description and label attributes contain a specified text string, returning the same response as 1

 4.1. extended so that the specified search string is used in a google style search, where double quotes contain phrases to match exactly but otherwise the words are matched in any order

5. Request all items where the time/date stamp attribute is contained within a specified time interval, returning the same response as 1

6. Request all items where a dictionary object attribute matches a specified single value, returning the same response as 1

7. Request all items where a dictionary object attribute matches a list of specified values, returning the same response as 1

8. Request a single item of a particular resource type using its id, and return a JSON data ojbect containing all the attributes in 1.1 to 1.8

 8.1. in addition, data object includes a hierarchical dictionary object (code,translation,description, array of child objects)

 8.2. in addition, data object includesa full spatial footprint attribute in geojson (a feature collection)