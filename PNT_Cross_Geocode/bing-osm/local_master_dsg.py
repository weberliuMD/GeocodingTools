import sys
sys.path.append('../..')
import datasetgeocode as dsg
dsg.OSM_batch_geocode("../../PNT_Formatted_Address/PNT_bing.csv")