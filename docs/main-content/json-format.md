# JSON Format
While the JSON specification states keys are case-sensitive, the same key in different cases should not appear as this generates huge amounts of ambiguity. Due to their nature non-semantic keys such as hashes, encodings, etc are exceptions. JSON values follow the same rules as defined in the JSON specification.

Camel-case should be used to separate words in keys as this is the most common and understood convention, particularly in JavaScript where JSON is used a lot. Underscores are permissible as prefixes, postfixes or where more than an upper-case character is needed to separate part of a key, perhaps for semantic reasons. While use of hyphens (kebab-case) does provide a nice visual separation between words, some consumers do have issues parsing or converting keys with hyphens so their use is not recommended.

## JSON request payloads
For readonly requests a `application/json` payload should be used if possible, it should contain a single JSON object. That JSON object may contain any combination of `query`, `complex` and `base64` objects. The `query` object has a flat structure containing simple key:value parameters; no objects or arrays. This is the preferred place for properties as the contents can easily be parsed, moved or contained in map style structures such as a URL query string:
```json
{
	"query": {
		"xmin": -1,
		"ymin": 53,
		"xmax": 1,
		"ymax": 55,
		"sampleTypes": "rock;soil;bone;shell;hair;feather",
	}
}
```

The `complex` object may be used if the parameters are too complex to fit in a the flat `query` object, like arrays of items with multiple properties:
```json
{
	"complex": {
		"sampleTypes": [
			{
				"id": 1,
				"name": "rock"
			}
			{
				"id": 2,
				"name": "soil"
			}
			{
				"id": 3,
				"name": "bone"
			}
		]
	}
}
```


A `base64` array of objects can be used if data in other formats needs to be transferred. Note that this is the slowest performing approach so try to avoid using it for services that require high performance. Each array object must have the following properties:
* `mimeType`: so the data can be parsed and understood
* `title`: unique within the request so the item can be identified
* `value`: the data item encoded using __UTF-8 Base64__ encoding
```json
{
	"base64": [
		{
			"mimeType": "text/plain",
			"title": "Greeting",
			"value": "SGFwcHkgZGF5cyE="
		}
	]
}
```

## Response Body
Every JSON response should use the following object as its root. Not all properties are required and there is no mutual exclusion, despite how it may appear.
```json
{
	"msg": "",
	"type": "",
	"self": "",
	"props": {},
	"data": [],
	"meta": {},
	"errors": [],
	"links": []
}
```

Name/Key | Type | Description | Required
:--- | :---: | :--- | :---
msg | string | Human readable message about the response that may be displayed to the end user | Always
type | string | Represents the type of response: success, fail, etc... | Always
self | string | Link to the request that produced the response | Always
props | object | Map of labels, descriptions and data types to data properties |
\*data | array | Array of the requested data items as objects |
\*meta | object | Contains links, generic data and metadata about the response data |
errors | array | Contains any errors encountered while processing the request |
links | array | Contains links to related resources |

\*These elements have Web API specific properties.

Minimal dataless response:
```json
{
	"msg": "Sample 123 deleted OK",
	"type": "success",
	"self": "http://api.bgs.ac.uk/apis/sensor-portal/samples/987"
}
```

Verbose data response:
```json
{
	"msg": "10 samples returned OK",
	"type": "success",
	"self": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings?page=2",
	"props": {
		"type": "object",
		"desc": "Readings from a single sensor",
		"props": {
			"ts": {
				"type": "date-time",
				"title": "Reading timestamp",
				"desc": "Date and time when the reading was made",
				"symDesc": "ISO 8601"
			},
			"r1": {
				"type": "float",
				"title": "Water temperature",
				"symPostfix": "°C",
				"symDesc": "degrees C"
			},
			"r2": {
				"type": "float",
				"title": "Water level",
				"symPostfix": "m",
				"symDesc": "meters"
			}
		}
	},
	"data": [
		{
			"id": "123",
			"analysis": [
				{
				  "ts": "99999991",
					"r1": "293.15",
					"r2": "2.1",
				},
				{
					"ts": "99999992",
					"r1": "291.60",
				},
			]
		},
		{
			"...": "...",
			"...": "..."
		},
		{
			"...": "...",
			"...": "..."
		}
	],
	"meta": {
		"dataVersion": "3",
		"totalResults": 10
	},
	"links": [
		{
			"title": "OpenAPI specification",
			"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/openapi.json",
			"dataType": "application/json"
		},
		{
			"title": "Previous page",
			"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings?page=1",
			"dataType": "application/json",
			"rel": "prev"
		},
		{
			"title": "Next page",
			"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings?page=3",
			"dataType": "application/json",
			"rel": "next"
		},
		{
			"title": "Recording sensor",
			"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123",
			"dataType": "application/json"
		},
		{
			"title": "Readings as CSV",
			"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings.csv?page=2",
			"dataType": "text/csv",
			"rel": "alternate"
		}
	]
}
```

Error response:
```json
{
	"msg": "'GG' is not a valid dictionary code within the rock type dictionary",
	"self": "http://api.bgs.ac.uk/apis/sensor-portal/samples?rockType=GG",
	"type": "bad-request",
	"errors": [
		{
			"error": "parameter",
			"propName": "dict-code",
			"desc": "Invalid dictionary code"
		}
	],
	"meta": {
		"contactEmail": "enquires@bgs.ac.uk"
	}
}
```

## "msg"
Not much in the way of restrictions about what the message should contain except that it needs to be in readable English and presentable enough for end users of any client application. Bare in mind that developers will be using the message as quick reference while developing.

Here are a few recommendations:
* Be concise
* Be clear
* Be as specific as possible
* Avoid in-depth jargon or long and complicated words
* Try to include the number of data elements when targeting a collection of items
* Try to include an ID if a specific resource item is being targeted

## "type"
`type` serves a very similar purpose as the first digit of HTTP response codes. More detailed information about the error or errors can be found within the `errors` array:
Value | Description | HTTP response code equivalent
:--- | :--- | :---:
`success` | The whole request was fulfilled | `2XX`
`part-success` | Only part of the request could be fulfilled | `2XX`
`bad-request` | The request could not be fulfilled due to an issue with the request | `4XX`
`server-error` | The request could not be fulfilled due to an issue with the server | `5XX`

## "props"
Describes the structure and properties of the items within the `data` array. This is allows the front end to be separated from the specifics of the web API. Generic front ends can then display data, with its metadata, regardless of which web API it's looking at. Each property can be described using the following properties:
Property | Description | Required
:--- | :--- | :---:
`type` | Property data type, see 'Data types and formats' section for a full list | Always
`title` | Human readable label of the property | Always
`desc` | Human readable description of the property |
`props` | The nested properties if an object |
`items` | The nested items if an array |
`symPrefix` | The symbol that precedes the value |
`symPostfix` | The symbol that follows the value |
`symDesc` | Human readable name of the property

These are the data types available for referencing by properties:
Type | Comments
:--- | :---
`int` | Signed 32 bits
`long` | Signed 64 bits
`float` |
`double` |
`string` |
`byte` | Base64 encoded characters
`binary` | Any sequence of octets
`boolean` |
`date` | As defined by full-date - [RFC3339][rfc3339]
`time` | As defined by full-time - [RFC3339][rfc3339]
`date-time` | As defined by date-time - [RFC3339][rfc3339]
`object` |
`array` |
`special` | Dynamic or complex property with no appropriate type or should not be presented by generic viewers

```json
"props": {
	"type": "object",
	"desc": "Readings from a single sensor",
	"props": {
		"ts": {
			"type": "date-time",
			"title": "Reading timestamp",
			"desc": "Date and time when the reading was made",
			"symDesc": "ISO 8601"
		},
		"r1": {
			"type": "float",
			"title": "Water temperature",
			"symPostfix": "°C",
			"symDesc": "degrees C"
		},
		"r2": {
			"type": "float",
			"title": "Water level",
			"symPostfix": "m",
			"symDesc": "meters"
		}
	}
}
```

## "data"
Array of data items that were requested that are always objects. Once a version of a web API goes live the data structure must not change except for additions. This way any changes to the structure will not affect consumers that are not aware of them. The `props` object should contain all the information required to parse and present the data contained.

A response to a request for data with the `success` or `part-success` types must always contain a `data` property even if there is no data to return, i.e an empty array. An empty array signals that the intent was to return some data but it just so happens there was no appropriate data to return rather than there being an error. It may not be intuitive from the perspective of the web API developer but the existence of an empty array can instill clarity and confidence to a front end developer.

To avoid breaking changes web API changes must NOT:
* Rename keys
* Remove keys
* Move key/value pairs
* Change the type of a key/value pair
* Change the meaning of key/value pair

You can:
* Add new key/value pairs
* Clarify or rewrite descriptions providing the initial meaning does not change

```json
"data": [
	{
		"id": "123",
		"analysis": [
			{
			  "ts": "99999991",
				"r1": "293.15",
				"r2": "2.1",
			},
			{
				"ts": "99999992",
				"r1": "291.60",
			},
		]
	},
	{
		"...": "...",
		"...": "..."
	},
	{
		"...": "...",
		"...": "..."
	}
]
```

## "meta"
A place for generic information about the service, request or data items. The structure is Web API specific. This is a good place to add hints and useful information if the front end is web API specific.
```json
"meta": {
	"dataVersion": "3",
	"resultCount": 10
}
```

## "errors"
Any response, regardless of type, can contain errors or warnings in its `errors` array. Usually only a single item will be added but it may be useful to provide multiple items in some cases. For example, when submitting form data there may be multiple items in error, it is much more efficient and convenient to give clients all errors at once than make multiple failing requests; the client can then decide how to present them to the user.

It's up to the development teams to decide the best approach to errors and warnings for a particular web API. Errors can also be warnings, which shouldn't stop clients from continuing to use the service, in the short term at least.

Name/Key | Description | Required
:--- | :--- | :---:
`error` | Type of error | Always
`propName` | Usually only used with the `parameter` type. Property/parameter name or key that was in error so the error can be linked to it's source; such as an input field of a form |
`desc` | Human readable description of the error | Always

```json
"errors": [
	{
		"error": "parameter",
		"propName": "rocktype",
		"desc": "The 'rock type' parameter is missing but required to complete the request",
	},
	{
		"error": "warning",
		"propName": "depth",
		"desc": "The 'depth' parameter was provided but redundant for this particular request",
	}
]
```

Types of errors:
Type | description | HTTP response code equivalent
:--- | :--- | :---:
`warning` | General warning, should not be used to indicate the source of request failure although may be used to suggest where there might be an error |
`request` | Any error with a request that is __not__ a `parameter` error | `4XX`
`parameter` | A parameter is missing or invalid | `4XX`
`service` | Any service or server error | `5XX`

## "links"
An array of objects to related resources or alternative actions. Each object should contain enough information required to meaningfully describe and access the linked resource:
Type | description | required
:--- | :--- | :---:
`title` | Human readable label for the link | Always
`ref` | The link its self | Always
`type` | Data format of the returned response |
`rel` | How the link is related to the requested resource |

```json
"links": [
	{
		"title": "OpenAPI specification",
		"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/openapi.json",
		"dataType": "application/json"
	},
	{
		"title": "Previous page",
		"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings?page=1",
		"dataType": "application/json",
		"rel": "prev"
	},
	{
		"title": "Next page",
		"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings?page=3",
		"dataType": "application/json",
		"rel": "next"
	},
	{
		"title": "Recording sensor",
		"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123",
		"dataType": "application/json"
	},
	{
		"title": "CSV",
		"ref": "http://api.bgs.ac.uk/apis/sensor-portal/sensor/123/readings.csv?page=2",
		"dataType": "text/csv",
		"rel": "alternate"
	}
]
```
