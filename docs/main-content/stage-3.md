#### Guidance
# Help users to: Make sense of search results

Search results should allow users to sort, filter and refine results quickly in a format that they can understand.

## Pain points

- Poor or invalid descriptions
- Overwhelming amount of results / data returned
- Multiple results contain the same data
- Ranking by "best match" did not match user expectations
- Frequency of search term per record is a bad descriptor of rank
- Misinformation within data sets
- Off the shelf search / sort and filter algorithms are often inadequate
- Acronyms are difficult to interpret and understand

## Design patterns
### Overview


![Results page overview](../_media/results-overview.png)

1. Number of returned results
2. Faceted search / refine options
   -  a. Sort by
   -  b. Applied filters
   -  c. Spatial search / filtering
   -  d. Filter by ...
  
3. Result 
   -  a. title 
   -  b. description
   -  c. meta tags
   -  d. publisher
   -  e. licence type
   -  f. last update date
   -  g. data quality
   -  h. feedback

### Component by component 


1. Number of returned results

![Number of returned results](../_media/results-component-number_of_results.png)

2. Faceted search / refine options

![Sort by](../_media/results-component-sort.png)

![Filtered by](../_media/results-component-filter.png)

![Spatial search](../_media/results-component-spatial_search.png)

3. Result

![Returned result](../_media/results-component-result.png)

## Design principles and recommendations
### When to use this pattern

Use this pattern when users are expecting returned search queries to be formatted as a list of results with further options to sort / filter and refine results. Keeping this page scannable will save users from being overwhelmed with too much content.


## Related research for this pattern

Read the blog post about *testing and iterating this pattern*.

