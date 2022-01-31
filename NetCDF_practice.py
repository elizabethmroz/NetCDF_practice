# libraries
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import cartopy

# loading netCDF file
bfp = "C:\\Users\\gy16e3m\\Documents\\Python\\NetCDF\\pr_day_GFDL-ESM2M_historical_r1i1p1_EWEMBI_20010101-20051231.nc4" 
bfp_dataset = nc.Dataset(bfp)

# accessing metadata
print(bfp_dataset)

# accessing metadata by its key
print(bfp_dataset.__dict__['project'])

# accessing dimensions
for dim in bfp_dataset.dimensions.values():
    print(dim)
    
print(bfp_dataset['time']) # accessing an individual dimension

# accessing variable metadata
for var in bfp_dataset.variables.values():
    print(var)
    
print(bfp_dataset['lat']) # accessing an individual variable's metadata



# access data values
''' data values are accessed by array indexing and a numpy array is returned'''

# time
bfp_time = bfp_dataset['time'][:]
print(bfp_time)

bfp_time_subset = (bfp_time[100:120]) # 1-dimensional array
print(bfp_time_subset)

# precipitation
bfp_precipitation = bfp_dataset['pr'][:]
print(bfp_precipitation)

bfp_precip_subset = (bfp_precipitation[0, 100:120, 100:120]) # 3-dimensional array
print(bfp_precip_subset)


# randomly selecting latitudes and longitudes to sample
random_lat = np.random.choice(bfp_dataset['lat'])
random_lon = np.random.choice(bfp_dataset['lon'])


# writing NetCDF file
location = {'name': 'location', 'lat': random_lat, 'lon': random_lon} # selected a location


