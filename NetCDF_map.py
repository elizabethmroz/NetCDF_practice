'''
TUTORIAL FOLLOWED:
    https://gradsaddict.blogspot.com/2019/12/python-tutorial-introduction-to-reading.html
'''

# install packages
import numpy as np
import netCDF4 as nc
from matplotlib import pyplot as plt
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


''' 
Information derived:
        
    Data stored at float64
    Data is in days (yyyy/mm/dd)
    Time is the only dimension
        
    As a result, datetime striptime and timedelta functions can convert the floating 
    point values to a list of datetime objects. 
'''


# set starting 'strp' time object
starttime = dt.datetime.strptime(ncdata.variables['time'].units,
                                 'hours since %Y-%m-%d %H:%M:0.0')


# pull time data into numpy array, build a list of datetime objects
time_values = ncdata.variables['time'][:]
strptimes = [starttime + dt.timedelta(days=i) for i in time_values]


# obtain time index for a specific input time
choice = '2001-01-30 00:00:0.0' # if choice is beyond the index, the last index is printed
choice_strp = dt.datetime.strptime(choice,'%Y-%m-%d %H:%M:0.0')
tidx = np.argmin(np.abs(np.array(strptimes)-choice_strp))


print("Index:%i, time:"%tidx, strptimes[tidx])


'''
PLOT THE DATA

    lat and lon are 1-dimensional variables
    time is a 1-dimensional variable
    precip is a 3-dimensional variable
'''


# access variable for each dimension
t2 = ncdata.variables['air'][tidx,:]
lon = ncdata.variables['lon'][:]
lat = ncdata.variables['lat'][:]


# simple plot
plt.figure(figsize=(10,7))
plt.pcolormesh(lon,lat,t2,cmap='jet')
plt.show()



'''
NOTES FOR SELF
        The file is from 1st Jan 2001 to 31st Dec 2005
        
        I have no idea what the units are in for precipitation 
     
MISC THINGS COULD BE FUN TO DO
        Could do a for-loop to create a plot for each day, figure out a way of merging them into a gif:
            Potential algorithm =
            (1) For-loop, for each day in time, create a plot
            (2) Save the plot to a folder, filename should be the date
            (3) Use some sort of image processing library in python to read all the files in a folder, 
                order them by date, write them to a video or gif
'''