# GIS Projects
## Watershed Delineation Script
Link to GitHub Repository: [invalid URL removed]

**Description**
This Python function provides a streamlined approach to delineate watersheds from a single Digital Elevation Model (DEM) raster file. Using libraries like GeoPandas, rasterio, scikit-image, scipy, and NumPy to ensure an open source approach.

**Key Features**
- Simplified Workflow: Requires only a DEM raster file as input.
- Stream Delineation: Explicitly identifies stream networks within watersheds.
- Customizable: The percentile threshold can be adjusted for specific needs.
- Open source: Relies on open source libraries for everyone´s usage.

**How it Works**
- Import Libraries: Necessary modules for spatial data handling and analysis are imported.
- Open DEM File: Reads DEM data, extracting elevation information.
- Preprocess DEM: Creates a binary mask to differentiate valid data from nodata values, then fills small holes for better processing.
- Identify Streams: Determines a suitable threshold and creates a stream network mask.
- Watershed Segmentation: Uses the negative filled DEM and stream network mask to segment the watersheds.
- GeoDataFrame Creation: Transforms watershed labels into a GeoDataFrame for GIS applications.
- Save Watersheds: Saves delineated watersheds as a shapefile.

**Installation and Usage**
- Install Dependencies: Install required Python libraries.
- Run the Script:
  1. Modify the DEM file path to match your file location.
  2. Define a percentile adequate to your case (optional)
  3. Replace the output file directory where desired
      
**Example Output**



## Other project
- Project description
- [Project repository]
