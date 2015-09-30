# Converts a feature class into a shapefile using arcpy's FeatureClassToShapefile tool
# For GSCPC purposes, this particularly useful for converting SDE data into shapefiles without the need to open ArcGIS
# More info: http://resources.arcgis.com/EN/HELP/MAIN/10.1/index.html#//00120000003m000000

import arcpy

inFeatures = ["<path to feature class>","<path to another feature class if you have one>"]
outLocation = "<path to where you want your output to go>"
# For example "C:/output-folder"

arcpy.FeatureClassToShapefile_conversion(inFeatures, outLocation)
