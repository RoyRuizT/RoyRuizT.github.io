#Importing necessary modules
import geopandas as gpd
import rasterio as rio
import skimage as ski
import scipy as sp
import numpy as np
import os

def delineate_watersheds(dem_file, percentile=5):
    """
    Delineates watersheds from a Digital Elevation Model (DEM).

    Arguments:
        dem_file (str): Path to the DEM file (the path must be raw string).
        percentile (int): The value of the percentile for the stream threshold. Default = 5 (Meaning the 5% lower
                                                                                             values are going to be 
                                                                                             considered as streams)
        
    Returns:
        geopandas GeoDataFrame containing the delineated watersheds.
        
    Outputs:
        Shapefile with the watersheds' polygons in the directory where the DEM file is
    """
    
    #Opening the DEM data
    dem = rio.open(dem_file)
    
    #Reading the first band (elevation data)
    dem_array = dem.read(1)
    
    #Getting the transformation and coordinate reference system
    transform = dem.transform
    crs = dem.crs
    
    #Creating a binary mask (0 for nodata, 1 for valid data)
    binary_mask = dem_array > 0
    
    #Removing small holes in the mask
    filled_mask = ski.morphology.remove_small_holes(binary_mask)
    
    #Obtaining a dem excluding nodata values
    filled_dem = filled_mask * dem_array
    
    #Calculating the 5th percentile threshold for stream delineation (lower values are the streams)
    threshold = np.percentile(filled_dem, percentile)
    
    #Creating a stream network based on the threshold
    stream_mask = dem_array < threshold
    
    #Generate markers for watershed segmentation
    markers = sp.ndimage.label(stream_mask)[1]
    
    #Performing watershed segmentation using the negative filled DEM (streams become ridges and ridges become streams)
    labels = ski.segmentation.watershed(filled_dem, markers)
    
    #Converting watershed labels to GeoDataFrame features
    from rasterio import features
    ws_geoms = features.shapes(labels, transform=transform)
    ws_features = []
    for geom, attr in ws_geoms:
        ws_features.append({'geometry': geom,'properties': None})
    watersheds = gpd.GeoDataFrame.from_features(ws_features, crs=crs)
    
    #Saving the watersheds as a shapefile in root directory
    root_dir = os.path.dirname(dem_file)
    shp_file = os.path.join(root_dir,'watersheds.shp')
    watersheds.to_file(shp_file)
    
    return watersheds
