import numpy as np
import xarray as xr
import datetime as dt
import calendar

ds = xr.open_dataset("C:/Users/gy16e3m/Documents/Python/NetCDF/climate_data/Complete_TAVG_Daily_LatLong1_1980.nc")

ds['time'] = (
    ('time'), dt.datetime(1980,1,1) + np.arange(0, ds.dims['time']) *dt.timedelta(days=1))




clim_tmp=xr.DataArray(dims=('time','latitude','longitude'),
    coords={'time':ds.time,'latitude':ds.latitude,'longitude':ds.longitude},
    data=np.zeros((ds.dims['time'],ds.dims['latitude'],ds.dims['longitude']))*np.nan)
                        

for yr in np.unique(ds.time.dt.year):
    if calendar.isleap(yr):
        clim_tmp.loc[{'time': (clim_tmp.time.dt.year==yr)&clim_tmp.time.dt.dayofyear<=59}] = ds.climatology.values[0:59]
        clim_tmp.loc[{'time': (clim_tmp.time.dt.year==yr)&clim_tmp.time.dt.dayofyear==60}] = ds.climatology.values[59]
        clim_tmp.loc[{'time': (clim_tmp.time.dt.year==yr)&clim_tmp.time.dt.dayofyear>60}] = ds.climatology.values[59:365]
    else:
        clim_tmp.loc[{clim_tmp.time.dt.year==yr}] = ds.climatology.values
        
ds['climatology'] = clim_tmp

ds['tas'] = ds['temperature'] + ds['climatology']
ds = ds.drop(['temperature', 'climatology'])


geo_lims = {'lat':[23,51], 'lon':[-126, -65]}
ds = ds.sel(latitude=slice(*geo_lims['lat']), longitude=slice(*geo_lims['lon'])).load()

output_fn = "C:/Users/gy16e3m/Documents/Python/NetCDF/climate_data/tas_day_BEST_historical_station_1980.nc"
ds.attrs['origin_script']='preprocess_best.py'
ds = ds.rename({'latitude':'lat', 'longitude':'lon'})
ds.to_netcdf(output_fn)