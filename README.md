# GIS Projects
## Watershed Delineation Script
Link to GitHub Repository: [invalid URL removed]

**Description**

This Python function provides a streamlined approach to delineate watersheds from a single Digital Elevation Model (DEM) raster file. Using libraries like GeoPandas, rasterio, scikit-image, scipy, os and NumPy to ensure an open source approach.

**Key Features**
- Simplified Workflow: Requires only a DEM raster file as input.
- Stream Delineation: Explicitly identifies stream networks within watersheds.
- Customizable: The percentile threshold can be adjusted for specific needs.
- Open source: Relies on open source libraries for everyone´s usage.

**How it Works**
- Open DEM File: Reads DEM data, extracting elevation information.
- Preprocess DEM: Creates a binary mask to differentiate valid data from nodata values, then fills small holes for better processing.
- Identify Streams: Determines a suitable threshold and creates a stream network mask.
- Watershed Segmentation: Uses the filled DEM and stream network mask to segment the watersheds.
- GeoDataFrame Creation: Transforms watershed labels into a GeoDataFrame for GIS applications.
- Save Watersheds: Saves delineated watersheds as a shapefile.

**Usage**
- Install Dependencies: Install required Python libraries.
- Run the function:
  1. Arguments:
     - dem_file (str): Path to the DEM file (the path must be raw string)
     - (Optional) percentile (int): The value of the percentile for the stream threshold. Default = 5 (Meaning the 5% lower values are going to be considered as streams)    
  2. Returns:
        - geopandas GeoDataFrame containing the delineated watersheds.
  3. Outputs:
        - Shapefile with the watersheds' polygons in the directory where the DEM file is.
      
**Example Input**

`import geopandas as gpd`  
`import rasterio as rio`  
`import skimage as ski`  
`import scipy as sp`  
`import numpy as np`  
`import os`  
`WS = delineate_watersheds(r'C:\Users\rrztscno\Downloads\7950_3050.tif')`  

**Example Output**

![Image created with input DEM and output shapefile](https://github.com/user-attachments/assets/8fff706a-b4ef-4af5-a56b-9644936c8123)



## Other project
- Project description
- [Project repository]
