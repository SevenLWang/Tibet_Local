import subprocess
from glob import glob
import os
import pandas as pd
from obspy import UTCDateTime

datadir = '/work/wang_li/Program/Tibet/'

events = pd.read_table('/work/wang_li/Program/LOCAL_X1_YOUYIMS/IRIS_local_catalogue.txt',names=['Date','Longitude','Latitude','Magnitude','Depth'],encoding='gb2312',sep=' ')
#stations = stations[stations['State']=='Harvested']
#print(events)

for d in glob(datadir + '2012*'):
    datetime = os.path.basename(d)
    print(datetime)
    for f in glob(d + '/*.SAC'):
        print(f)
        #sacname = os.path.basename(f)
        #temp = sacname.split('.')
        cmd = "saclst kzdate kztime f %s" % (f)
        junk, kzdate, kztime = os.popen(cmd).read().split()
        #kzdate = float(kzdate)
        #kztime = float(kztime)
        #netname, staname, chaname = temp[0], temp[1], temp[3]
        #print(netname, staname)
        #temp = stations[(stations['Line #']==line) &  (stations['Point #']==point)]
        for i in range(len(events)):         #遍历每一行
          Datetime = events['Date'][i].split(' ') #分开第i行，x列的数据。split()默认是以空格等符号来分割，返回一个列表
          Datetime = Datetime[0]      
          Date = Datetime.split(',')[0]
          Time = Datetime.split(',')[1]
          #print(Date,Time)
          yy=datetime[0:4];mon=datetime[4:6];dd=datetime[6:8];hh=datetime[8:10];mm=datetime[10:12];ss=datetime[12:14];
          kzyy=kzdate.split('/')[0];kzmon=kzdate.split('/')[1];kzdd=kzdate.split('/')[2];kzhh=kztime.split(':')[0];kzmm=kztime.split(':')[1];kzs=kztime.split(':')[2];kzss=kzs.split('.')[0];
          YY=Date.split('/')[0];MON=Date.split('/')[1];DD=Date.split('/')[2];HH=Time.split(':')[0];MM=Time.split(':')[1];S=Time.split(':')[2];SS=S.split('.')[0];
          tt = UTCDateTime(int(yy),int(mon),int(dd),int(hh),int(mm),int(ss))
          TT = UTCDateTime(int(YY),int(MON),int(DD),int(HH),int(MM),int(SS))
          kztt = UTCDateTime(int(kzyy),int(kzmon),int(kzdd),int(kzhh),int(kzmm),int(kzss))
          #print(tt,TT)
          if (tt == TT): 
            #temp = temp.iloc[0]
            lat, lon = events['Latitude'][i], events['Longitude'][i]
            mag, dep = events['Magnitude'][i], events['Depth'][i] 
            otime = tt-kztt
            print(lat,lon,mag,dep,otime)
            p = subprocess.Popen(['sac'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            s = ""
            s += "r %s\n" % f
            s += "ch evla %.6f\n" % float(lat)
            s += "ch evlo %.6f\n" % float(lon)
            s += "ch mag  %.2f\n" % float(mag)
            s += "ch evdp %.3f\n" % float(dep)
            s += "ch o %.6f\n" % float(otime)  
            s += "wh\n"
            s += "q\n"
            p.communicate(s.encode())
          else:
            continue
            #print('skip %s' % f)
