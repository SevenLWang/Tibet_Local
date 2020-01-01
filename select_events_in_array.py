from glob import glob
import os
import pandas as pd
from obspy import UTCDateTime
from tqdm import tqdm

datadir = '/data_1/njdataX1/LOCAL_X1_YOUYIMS/'

events = pd.read_table('/work/wang_li/Program/LOCAL_X1_YOUYIMS/IRIS_local_catalogue.txt',names=['Date','Longitude','Latitude','Magnitude','Depth'],encoding='gb2312',sep=' ')
#print(events)

ddir = '/work/wang_li/Project/Tibet/Data'

for d in tqdm(glob(datadir + '20*')):
    datetime = os.path.basename(d)
    #print(datetime)
    yy=datetime[0:4];mon=datetime[4:6];dd=datetime[6:8];hh=datetime[8:10];mm=datetime[10:12];ss=datetime[12:14];
    for i in range(len(events)):         #遍历每一行
        Datetime = events['Date'][i].split(' ') #分开第i行，x列的数据。split()默认是以空格等符号来分割，返回一个列表
        Datetime = Datetime[0]      
        Date = Datetime.split(',')[0]
        Time = Datetime.split(',')[1]
        #print(Date,Time)
        YY=Date.split('/')[0];MON=Date.split('/')[1];DD=Date.split('/')[2];HH=Time.split(':')[0];MM=Time.split(':')[1];S=Time.split(':')[2];SS=S.split('.')[0];
        tt = UTCDateTime(int(yy),int(mon),int(dd),int(hh),int(mm),int(ss))
        TT = UTCDateTime(int(YY),int(MON),int(DD),int(HH),int(MM),int(SS))
        #print(tt,TT)
        if (tt == TT): 
            #temp = temp.iloc[0]
            lat, lon = events['Latitude'][i], events['Longitude'][i]
            if (lat < 29 and lat >22 and lon < 107 and lon > 98):
                command = "cp -r %s %s" % (d, ddir)
                #print(command)
                os.system(command)
                #print('success')
            else:
                continue
        else:
            continue
            #print('skip %s' % f)
