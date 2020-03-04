# List of external APIs currently used by BGS apps

---

This is not a comprehensive list of external APIs.

*  [OSPlaces](https://developer.ordnancesurvey.co.uk/os-places-api) (Shop and BackOffice) OS API for looking up addresses and their grid references (pay-per-click)

*  Undocumented API used between Shop and GIS to get up-to-date product lists for map sheets e.g. [map sheet S066](https://shop.bgs.ac.uk/Shop/search/mapSheet/S066.json) (the HTML search on the Shop uses the same API)

*  OpenStreetMap - Nominatim (we actually host this!)

*  Various map tile services (OSM,ESRI) for web maps across loads of apps

*  [Environmental Baseline Monitoring pages](https://www.bgs.ac.uk/research/groundwater/shaleGas/monitoring/vopDataSummary.html) API to get Air Quality data from WACL (key required)