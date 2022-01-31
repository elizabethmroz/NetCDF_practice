'''
NAME
    NetCDF in Python
PURPOSE
    Reading and writing data with a NetCDF file
    Plotting using MatPlotLib and Basemap
PROGRAMMER
    Elizabeth Mroz
PROGRAMME DEVELOPED FROM TUTORIAL:
    http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html
    By Chris Slocum 
'''

# Libraries
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import datetime as dt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid