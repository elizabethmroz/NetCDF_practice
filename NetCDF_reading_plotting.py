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


def ncdump(nc_fid, verb=True):
    '''
    ncdump outputs dimensions, variables, and their attribute information.
    ncdump requires a valid instance of Dataset

    Parameters
    ----------
    nc_fid : NetCDF4.dataset
        DESCRIPTION.
    verb : Boolean
        whether or not nc_attrs, nc_dims, and nc_vars are printed

    Returns
    -------
    nc_attrs : list
        A Python list of the NetCDF file global attributes
    nc_dims : list
        A Python list of the NetCDF file dimensions
    nc_vars : list
        A python list of the NetCDF file variables
    '''
    def print_ncattr(key):
    '''
    Prints the NetCDF file attributes for a given key
    
        Parameters
        ----------
        key : unicode
            a valid netCDF4.dataset.variables key

        Returns
        -------
        Print of the NetCDF file attributes for a given key

        '''   
        try:
            print "\t\"