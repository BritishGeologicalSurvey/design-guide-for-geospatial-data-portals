### Help users to
# Search for data

> Help users search for data within the data portal. 

Some users prefer to search for data using keywords, some by specifying a location and seeing what datasets are available in the area, and some require a combination of both methods.

Ideally the data portal should support both of these methods - keywords search and map search. An exemption could be small data portals serving a limited amount of datasets. In such cases (for example portals with less than 20 datasets) search might not be required since all the datasets could be presented on a single page.

## What it looks like

## 1. Search field

Users should be able to search for data using keywords. Search field should be easily noticeable. Since search is one of the primary functions of data portal, it should be accessible from any page of portal. 
<!-- some confusion over the wording here -->

<div class="image-container">

![Simple search](../../_media/search-for-data/simple-search.png)

*Search bar*

</div>

## 2. Advanced search

Users should be able to specify more detailed search criteria

?> More details can be found in [*Make sense of search results*](main-content/steps/make-sense-of-search-results)

## 3. Spatial search

There are multiple ways to search for spatial data:

* Using post code / address
* Specifying coordinates
* Selecting an area on the map

Whichever way is used, it should be made clear to the user what will be included in the search results and what coordinate system is used.



<div class="image-container">

![Map View](../../_media/search-for-data/map-view.png)

*Map search*

</div>

The list of datasets matching the search criteria could also be displayed next to the map for easier browsing.

<div class="image-container">

![Google results](../../_media/search-for-data/navbar-search.png)

*Search in the navigation bar*

</div>

## 4. Provide tips on what users can search for

Include a sample query in the search bar to suggest to users what they can search for.

<div class="image-container">

![Simple search](../../_media/search-for-data/search-bar.png)

*Example search criteria*

</div>

## 5. Show search history

Show most recent or popular queries.

<div class="image-container">

![Search history](../../_media/search-for-data/search-history.png)

*Search history in the search bar*

</div>

## 5. Don't return no results

If the users query doesn't match any search results - provide an actionable message on what they could do differently.

If some datasets have a 'near' match to search criteria they can be displayed as well.

<div class="image-container">

![Search history](../../_media/search-for-data/no-results.png)

*Handling no results*

</div>

## 6. Sort by and filter options

if the initial search does not lead users to the dataset they are looking for, they should be able narrow down their search using filtering and sorting methods.

## 7. Show users' search query on the results page

Don't erase the search query in the search field so users can easily remember what they search for and alter their search keywords if required.

<div class="image-container">

![Detailed search](../../_media/search-for-data/search-terms.png)

*Search terms can be displayed on the results page, so that users don't have to remember what they searched for*

![Detailed search](../../_media/search-for-data/search-terms-2.png)

*Search terms should not get cleared from the search bar after search to make it easier to alter search terms if needed*

</div>

## When to use

When a user is searching for data to answer a specific research question

## Example page

* [Search / search results](main-content/pages/search-and-results)


---

<!-- Additional information can be presented in dropdown menus -->

<details>
<summary>Essential components</summary>
<br>

Below is a checklist of components/information that are relevant for this task.

These components can be arranged in many ways, but the ones with highest relevance should be the most visible/accessible.

?> 1 - high relevance, 2 - medium relevance, 3 - low relevance

<!-- Table of component start -->

| Component       | Description                                                               | Relevance |
|-----------------|---------------------------------------------------------------------------|:---------:|
| Homepage search | Simple search on data portals homepage                                    |     1     |
| Navbar search   | A search bar that's accessible from any page                              |     2     |
| Detailed search | A more detailed search page with additional filtering and sorting options |     1     |
| Data filtering  | An option to filter search results                                        |     2     |
| Data sorting    | An option to sort data search reults                                      |     1     |

</details>
