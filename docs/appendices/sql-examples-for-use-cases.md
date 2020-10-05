# SQL snippets for use cases

## Common requirements

### Database connections  

kwudb4.ad.nerc.ac.uk:1521:bgsdev  (beta/staging; schema will usually be BGS or PUBLISHED or could be application specific)
kwudb3.ad.nerc.ac.uk:1521:bgsprod  (internal production; scheme will usually)
192.171.148.149:1521:kwextrn    (external production)

### Scheme prefix
Examples below all use the BGS schema for testing on BGSPROD connections.
For kwextrn connectins this will need to be changed to either use the PUBLISHED schema, or an application specific schema.

# SQL examples

## Hello world use case

`select 'Hello world' from DUAL`


<pre id="use-case-1">
    1.    Request all items and return JSON array of data objects.
	
        Palaeosaurus example: select SAMPLE_ID,SAMPLE_PREFIX,SAMPLE_NUMBER,SAMPLE_SUFFIX FROM BGS.PAL_SAMPLE_WEB_VIEW
		
        Offshore Hydrocarbons example: select BOREHOLE_ID, WELLNAME from BGS.CSD_UKOFFSHOREHC_WELL_WEB       
</pre>

<pre id="use-case-2">
    2. Provide attributes within each data object in the array that includes
        2.1.    an integer attribute
        2.2.    a string attribute
        2.3.    a bounding box attribute in geojson 
        2.4.    a point geometry attribute in geojson
        2.5.    a dictionary object (code,translation,description)
        2.6.    a URL attribute to download or view the resource
        2.7.    date/time attribute
        
        Palaeosaurus example (incomplete): 
        
            SELECT
                    SAMPLE_ID,
                    SAMPLE_PREFIX,
                    SAMPLE_NUMBER,
                    SAMPLE_SUFFIX,
                    TAXON_CODE,
                    TAXON_DESC
              FROM
                    BGS.PAL_SAMPLE_WEB_VIEW
              
              
        Offshore Hydrocarbons example (incomplete): 
        
            SELECT
                    BOREHOLE_ID, 
                    WELLNAME, 
                    ORIG_SURFACE_LATITUDE, 
                    ORIG_SURFACE_LONGITUDE
            FROM 
                    BGS.CSD_UKOFFSHOREHC_WELL_WEB 
</pre>

<pre id="use-case-3">
    3. Request a single item of a particular resource type using its id, and return a JSON data ojbect containing all the attributes in 1.1 to 1.8.
    
        Palaeosaurus example, as for 2 and append: 
        
             WHERE SAMPLE_ID=
              
              
        Offshore Hydrocarbons example, as for 2 and append: 
        
            WHERE BOREHOLE_ID=
    
        
        3.1.    in addition, data object includes a hierarchical dictionary object (code,translation,description, array of child objects)
        3.2.    in addition, data object includes a full spatial footprint attribute in geojson (a feature collection)
</pre>

<pre id="use-case-4">
    4. Request all items where the description and label attributes contain a specified text string, returning the same response as 1.
        
        Palaeosaurus example, as for 2 and append: 
        
             WHERE UPPER(TAXON_DESC) like upper('%string%')
              
              
        Offshore Hydrocarbons example, as for 2 and append: 
        
             WHERE UPPER(WELLNAME) like upper('%string%')
            
        
        4.1. extended so that the specified search string is used in a google style search, where double quotes contain phrases to match exactly but
        otherwise the words are matched in any order
</pre>

<pre id="use-case-5">
    5. Request all items where the time/date stamp attribute is contained within a specified time interval, returning the same response as 1.
</pre>

<pre id="use-case-6">
    6. Request all items where the geometry is contained within a specified bounding box, returning the same response as 1.
</pre>

<pre id="use-case-7">
    7. Request all items where a dictionary object attribute matches a specified single value, returning the same response as 1
</pre>

<pre id="use-case-8">
    8. Request all items where a dictionary object attribute matches a list of specified values, returning the same response as 1
</pre>

<pre id="use-case-9">
    9. Return basic metadata about the API itself
</pre>

<pre id="use-case-10">
    10. Return a link to metadata about the collection of data items
</pre>