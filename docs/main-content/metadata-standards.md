# Metadata standards

> Metadata helps users understand data by providing a description for what the data represents. This information gives greater context and helps your users to find and understand datasets. Metadata standards encourage consistency and ensure best practice across and between data portals. This is achieved by providing an organisational scheme with which to structure and define data. Metadata standards are also relevant for providing data portals with information to index, search and sort their data records.

There are a number of metadata standards that relate to geospatial data. The UK government recommends GEMINI as the standard for organising geospatial information as metadata and many public and private sector organisations have found value in using this standard. GEMINI is based on international geographic ISO standards that are widely supported by software vendors and organisations. Standards ensure that datasets are web-friendly and follow well-defined descriptions such as Vocabulary (DCAT) and Schema.org. You can find more information about the GEMINI standard at [https://www.agi.org.uk/gemini](https://www.agi.org.uk/gemini).

## Metadata standards to address user needs
Metadata standards are an important invisible pillar to support users through their journey to discover, evaluate and use data. By incorporating metadata standards as part of your data portal, benefits include:
+ Users recognise and prefer data that has a well defined metadata standard
+ Organised data is perceived as more trustworthy
+ Interoperability of data between many applications and metadata catalogues
+ Satisfying the obligation many organisations may have with conforming to a metadata ISO standard

## Implemention
<!--
Is it worth including the relevant components where metadata standards are relevant
-->

Many pages within your data portal containing information about a dataset can largely be created from the metadata. This table suggests whcih GEMINI elements are relevant to which aspect of your portal:

| Page | Section | relevant GEMINI element(s) |
| ---- | ------- | -------------------------- |
| [Discover your portal](https://pautva.github.io/dd3-wireframes/#/main-content/steps/discover-your-portal?id=discover-your-portal) | [Dataset title](https://pautva.github.io/dd3-wireframes/#/main-content/steps/discover-your-portal?id=_1-dataset-title) | Title, Responsible organisation, Dataset reference date |
| [Discover your portal](https://pautva.github.io/dd3-wireframes/#/main-content/steps/discover-your-portal?id=discover-your-portal) | [Dataset description](https://pautva.github.io/dd3-wireframes/#/main-content/steps/discover-your-portal?id=_2-dataset-description) | Abstract |
| [Check if portal is relevant](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant) | [Purpose of data portal - topics covered](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant?id=_1-purpose-of-data-portal) | Keyword (1) |
| [Check if portal is relevant](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant) | [Organisation managing this portal/metadata](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant?id=_2-organisation-managing-this-portal) | |
| [Check if portal is relevant](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant) | [Licencing](https://pautva.github.io/dd3-wireframes/#/main-content/steps/check-a-portal-is-relevant?id=_3-licencing) | Use constraints |
| [Navigate the portal](https://pautva.github.io/dd3-wireframes/#/main-content/steps/navigate-the-portal) | [Page title](https://pautva.github.io/dd3-wireframes/#/main-content/steps/navigate-the-portal?id=_2-page-title) | Title |
| [Navigate the portal](https://pautva.github.io/dd3-wireframes/#/main-content/steps/navigate-the-portal) | [Related datasets](https://pautva.github.io/dd3-wireframes/#/main-content/steps/navigate-the-portal?id=_6-related-datasets) | Lineage source; Resource specific usage |
| [Make sense of search results](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results) | [Faceted search](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results?id=_2-faceted-search-by-parent-child-categories) | Topic category, Keywords, Dataset format, Extent, Use constraints |
| [Make sense of search results](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results) | [Apply filters](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results?id=_5-apply-filters) | |
| [Make sense of search results](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results) | [Geospatial filter](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results?id=_6-geospatial-filter) | Bounding box |
| [Make sense of search results](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results) | [Results list](https://pautva.github.io/dd3-wireframes/#/main-content/steps/make-sense-of-search-results?id=_7-results-list) | Title, Abstract (2), Data format, Dataset reference date |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Clear dataset title](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_1-clear-dataset-title) | Title |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Short description](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_2-short-description) | Abstract | 
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Topics](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_3-topics) | Keyword |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Publisher name](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_4-publisher-name) | Responsible organisation |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Licence details](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_5-licence-details) | Use constraints |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Created on date and period it relates to](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_6-created-on-date-and-period-it-relates-to) | Temporal extent |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Update frequency and last updated date](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_7-update-frequency-and-last-updated-date) | Maintenance information and Dataset reference date |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Download link](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_8-download-link) | Resource locator |
| [Assess dataset relevance](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance) | [Location preview](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-dataset-relevance?id=_9-location-preview) | Browse graphic (3) | 
| [Assess dataset quality](https://pautva.github.io/dd3-wireframes/#/main-content/steps/assess-data-quality) | | see also Data quality |

**Important considerations for GEMINI**
+ Some GEMINI elements can be repeated and/or have sub-elements, see [GEMINI](https://www.agi.org.uk/gemini) for further details
+ If the purpose of your portal is not pre-defined, you may be able to aggregate it from the keywords in the records in the portal
+ Search engines and search result pages often have limited space to display metadata such as a title and the description. Therefore, it is important to recognise that the first 150 characters of the abstract are the most valued for SEO and GEMINI.
+ Although "Browse graphic" is not described in GEMINI, it is a commonly used element in the underlying ISO standard

<!-- The geo6 will publish a report on metadata standards and can be found by visiting ( -- PLACEHOLDER TEXT - LINK TO GC-DD 3/2 --) -->

## Find out more
+ [GEMINI metadata standard](https://www.agi.org.uk/agi-groups/standards-committee/uk-gemini/40-gemini/1052-metadata-guidelines-for-geospatial-data-resources-part-1)
+ [AGI metadata](https://www.agi.org.uk/agi-groups/standards-committee/uk-gemini)
<!-- + [Geo6 metadata report / TBC ](#) -->
