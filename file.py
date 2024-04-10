#1.从nc文件中读取南京市的数据，然后进行数据处理
#2.将处理后的数据绘制成图
#分辨率：0.25*0.25
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
Tmin_dir    =   'data/CN05.1_Tmin_1961_2022_daily_025x025.nc' #文件路径
Tmax_dir    =   'data/CN05.1_Tmax_1961_2022_daily_025x025.nc' #文件路径
Tm_dir      =   'data/CN05.1_Tm_1961_2022_daily_025x025.nc' #文件路径
#------导入nc文件，读取对应的时间--------
def read_nc(nc_dir):
    data = xr.open_dataset(nc_dir)
    time = data['time']
    lat = data['lat']
    lon = data['lon']
    return data,time,lat,lon

Tmin,Tmin_time,Tmin_lat,Tmin_lon    = read_nc(Tmin_dir)
Tmax,Tmax_time,Tmax_lat,Tmax_lon    = read_nc(Tmax_dir)
Tm,Tm_time,Tm_lat,Tm_lon            = read_nc(Tm_dir)

print(Tmin)
#------读取特定地区mask掩码区域的数据--------
