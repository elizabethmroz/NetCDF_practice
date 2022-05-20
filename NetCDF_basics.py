# important netcdf package
import netCDF4 as nc
import xarray as xf


# access netcdf file
fn = 'C:/Users/gy16e3m/Downloads/isimip-download-93e7d448403c7ed8f8925bcea9641d8e88f1ab55/ipsl-cm6a-lr_r1i1p1f1_w5e5_historical_pr_zmb_daily_2011_2014.nc'
ds = nc.Dataset(fn)

# print its metadata
print(ds)

# access metadata as a dictionary
print(ds.__dict__)
# then can access specific metadata items using its key
print(ds.__dict__['title'])

# loop through all available dimensions to obtain their metadata
for dim in ds.dimensions.values():
    print(dim)

# print individual dimensions to obtain its metadata    
print(ds.dimensions['lat'])

# loop through all variables to obtain their metadata

for var in ds.variables.values():
    print(var)
    
# print individual variables to obtain its metadata
print (ds.variables['pr'])

# access data values of a variable using array indexing, returning a numpy array (masked for precipitation)
prcp = ds['pr'][:]
print(prcp.data)

# create a subset of a variable, returning a numpy array
prcp_subset = ds['pr'][180,5:10, 5:10]
print(prcp_subset.data)


# same as above but using latitude
lat = ds['lat'][:]
print(lat)

lat_subset = ds['lat'][50:55]
print(lat_subset)





# plotting using xarray
import xarray as xr

ds = xr.open_dataset("C:/Users/gy16e3m/Downloads/isimip-download-93e7d448403c7ed8f8925bcea9641d8e88f1ab55/ipsl-cm6a-lr_r1i1p1f1_w5e5_historical_pr_zmb_daily_2011_2014.nc")
ds.var
ds.load()


ds = ds.pr[0:5, 0:5, 0:365]
print(ds)

# plot average time series across all lat/lon points
ds.pr.mean(('lat', 'lon')).plot()

print(ds)


# heatmap of 3-dimensional variable
# at first timestep
ds.pr.isel(time=0).plot()

# averaged across all timesteps
ds.pr.mean('time').plot()


import cartopy.crs as crs
from matplotlib import pyplot as plt

ax = plt.axes(projection=crs.EckertIV())
ds.pr.isel(time=0).plot()

