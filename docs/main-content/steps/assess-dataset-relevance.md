<div class="small-heading" style="margin-top: 45px; font-size: 32px;">Help users to...</div>
<h1 id="assess-dataset-relevance" style="margin-top: 0px">Assess dataset relevance</h1>

> Ensure datasets are represented accurately with essential metadata. Users often base their decision on whether to use a dataset by how clearly this information is presented to them.

Users may often first arrive at a [dataset details page](https://pautva.github.io/dd3-wireframes/#/main-content/pages/dataset-details) after performing a search from a search engine. Thus, it should be instantly clear whether a dataset is available for download or not, what license it is shared under and anything else that may affect how this dataset is used. Make sure users are also provided with a route to understand the data portal in which this dataset record is described. This can be achieved through well-designed [navigation](/main-content/steps/navigate-the-portal). 

## What it looks like

!> A user's perception of dataset quality is driven by several different factors, such as publisher, publication date, frequency of updates, well-described metadata, how complete the data is and a clear visual presentation within the portal itself.<br>
<br>
For more information read how to help users to... [assess data quality](main-content/steps/assess-data-quality).

### 1. Clear dataset title

Dataset titles should be clearly visible as the first heading users are presented with.

<div class="image-container">

![Dataset heading on dataset details page](../../_media/assess-dataset-relevance/dataset-heading.png)

*Heading section for dataset details*

</div>

### 2. Short description

A short summary describing the main properties of a dataset will provide users with a quick understanding of how relevant a dataset is.

### 3. Topics

Grouping datasets under parent topics can help users understand the relevancy of a dataset and act as navigation for potentially related datasets.

<div class="image-container">

![Dataset heading on dataset details page. It highlights the topics for this example dataset.](../../_media/assess-dataset-relevance/dataset-heading-topics.png)

*Dataset topics*

</div>

### 4. Publisher details

Publisher details such as publisher name, and logo could help users recognise the quality of a dataset and promote trust with reputable dataset sources. Users may want to see a contact point in order to find out more about the data.

### 5. Licence details

Help users assess whether data is compatible with their needs by providing licence details, an explanation of what it means to them including any relevant links to terms of use.

### 6. Created on date and period it relates to

Provide users with information about when a dataset was created and the period of time the data relates to.

### 7. Update frequency and last updated date

Indicate how current datasets are by providing users with information about when a dataset was last updated and the frequency of updates.

<div class="image-container">

![Additional information for dataset showing the dataset creation time and frequency of updates](../../_media/assess-dataset-relevance/update-information.png)

*Dataset details relating to creation time and updates*

</div>

### 8. Download link

If the data is available for download, the download link should be easy to find and access on the dataset details page. Ideally, it should always stay visible on the screen as the users are exploring the dataset details page. If the dataset is not available for download, it should indicate why or when it would become available.

If there are multiple ways to access data, e.g. API access, instructions should be provided on how to do that.

<div class="image-container">

![Download link, file details and license information](../../_media/assess-dataset-relevance/download-panel.png)

*Download link*

</div>

### 9. Location preview

Clearly show the geographical extent using, for example a pin on the map or a polygon of area covered. If coordinates are included, provide information about the coordinate reference system used. If the terrain elevation is known it should be displayed together with the geographical extent.

<div class="image-container">

![Location preview for the datasets on dataset details page. ](../../_media/assess-dataset-relevance/quick-overview.png)

*Location preview. Map source: [OpenStreetMap](https://www.openstreetmap.org)*

</div>

### 10. Spatial data file format

Geospatial data can be formatted in several different data types, users may require a speific [GIS format](https://en.wikipedia.org/wiki/GIS_file_formats). Clearly presenting whether a dataset is a raster or vector format will help users to make an informed decision on the suitability of the data.
<div class="image-container">

![Data format information next to download link](../../_media/assess-dataset-relevance/vector-raster.png)

*Data format information next to download link*

</div>

### 11. Additional metadata

Additional metadata can have less visibility in order to reduce the visual clutter on the screen. The exact details of which attributes your users consider 'additional' may vary. This inforation can be displayed in a less promenant location such as different tabs or dropdown menus.

<div class="image-container">

![Additional info](../../_media/assess-dataset-relevance/additional-information.png)

*Extra metadata items in human-readable format*

</div>

### 12. Related datasets

Related datasets can help users to discover and explore similar datasets. They can be displayed in a list or map view. 

A few possible ways to group and identify related datasets include:

* Nearby datasets
* By topics and keywords
* By provider or publisher

<div class="image-container">

List view             |  Map view
:-------------------------:|:-------------------------:
![Related datasets shown as a list](../../_media/assess-dataset-relevance/similar-datasets.png) | ![Datasets nearby shown on a map](../../_media/assess-dataset-relevance/nearby-datasets.png)

*Related datasets in list and map view. Map source: [OpenStreetMap](https://www.openstreetmap.org)*

</div>

<!-- ## Related

* [Help users to explore data online](main-content/steps/explore-data-online)
* [Best practice guidance and tools for geospatial data managers](https://www.gov.uk/government/collections/best-practice-guidance-and-tools-for-geospatial-data-managers) -->

