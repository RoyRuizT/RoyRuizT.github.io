## Watershed Delineation Function

### Description
Delineates watersheds from a Digital Elevation Model (DEM).

**Arguments:**
- dem_file (str): Path to the DEM file (the path must be raw string).
- percentile (int): The value of the percentile for the stream threshold. Default = 5 (Meaning the 5% lower values are going to be considered as streams)

**Returns:**
- geopandas GeoDataFrame containing the delineated watersheds.
    
**Outputs:**
- Shapefile with the watersheds' polygons in the directory where the DEM file is
  
### Example Usage**
```import geopandas as gpd
import rasterio as rio
import skimage as ski
import scipy as sp
import numpy as np
import os
WS = delineate_watersheds(r'C:\Users\rrztscno\Downloads\7950_3050.tif')
```
