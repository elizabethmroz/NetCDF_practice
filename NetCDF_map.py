'''
TUTORIAL FOLLOWED:
    https://gradsaddict.blogspot.com/2019/12/python-tutorial-introduction-to-reading.html
'''

# install packages
import numpy as np
import netCDF4 as nc
from matplotlib import pyplot as plt
from cartopy import crs as ccrs
import datetime as dt

# set path to file
ncdata_path = "C:\\Users\\gy16e3m\\Documents\\Python\\NetCDF\\pr_day_GFDL-ESM2M_historical_r1i1p1_EWEMBI_20010101-20051231.nc4"
ncdata = nc.Dataset(ncdata_path, 'r')
print(ncdata)


'''
ACCESS FILE METADATA

    NetCDFs have global metadata attributes attached to them. 
    These can be accessed individually with the code:
        
            print(ncdata.description)
            
    However the code below is superior as it allows the extraction of all attributes
    without having to print the entire NetCDF file to see what attributes are 
    contained.
'''

for attri in ncdata.ncattrs():
    print(attri)
    print('>>',ncdata.getncattr(attri))
    print('')
    

'''
LOAD DIMENSIONS

    Dimensions structure includes the dimensions used in the file. In geographic
    datasets, these are typically: x, y, z, and time. 
    
    x and y are usually latitude and longitude 
    z is usually a vertical coordinate
    time is usually a floating point value referenced to a specific starting time 
    
    Dimensions are a dictionary.
'''

for dim in ncdata.dimensions:
    print(dim)


'''
LOAD VARIABLES

    Each variable will have dimensions that will be a combination of the dimensions
    within the dimensions dictionary. 
    
    Variables are a dictionary.
'''

for var in ncdata.variables:
    print(var)
    
    
'''
CONVERT TIME VALUES INTO A PYTHON DATETIME
'''

print(ncdata.variables['time'])

''' Information derived:
        
        Data stored at float64
        Data is in days (yyyy/mm/dd)
        Time is the only dimension
        
    As a result, datetime striptime and timedelta functions can convert the floating 
    point values to a list of datetime objects. 
'''

# set starting 'strp' time object
starttime = dt.datetime.strptime(ncdata.variables['time'].units,
                                 'days since %Y-%m-%d %H:%M:00')

# pull time data into numpy array, build a list of datetime objects
time_values = ncdata.variables['time'][:]
strptimes = [starttime + dt.timedelta(days=i) for i in time_values]

# obtain time index for a specific input time
choice = '2010-04-16 00:00:00' # if choice is beyond the index, the last index is printed
choice_strp = dt.datetime.strptime(choice,'%Y-%m-%d %H:%M:00')
tidx = np.argmin(np.abs(np.array(strptimes)-choice_strp))

print("Index:%i, time:"%tidx, strptimes[tidx])


'''
NOTES FOR SELF
        The file is from 1st Jan 2001 to 31st Dec 2005
'''