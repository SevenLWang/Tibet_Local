import subprocess
from glob import glob
import os
import pandas as pd
from obspy import UTCDateTime

datadir = '/work/wang_li/Program/Tibet/'

stations = pd.read_table('/work/wang_li/Program/LOCAL_X1_YOUYIMS/X1.POS.WITH.LOCID.V20151213.txt',names=['Net','Station','Number','Longitude','Latitude','Num'],encoding='gb2312',sep=' ')
print(stations)

for d in glob(datadir + '2012*/'):
    for f in glob(d + '*.SAC'):
        #print(f)
        sacname = os.path.basename(f)
        temp = sacname.split('.')
        for i in range(len(stations)):
            net = stations['Net'][i]
            station = stations['Station'][i]
            number = stations['Number'][i]
            lon = stations['Longitude'][i]
            lat = stations['Latitude'][i]
            #print(net,station,number,lon,lat)
            #print(temp[0],temp[1],temp[2])
            if (net == temp[0] and int(station) == int(temp[1]) and int(number) ==int(temp[2])):
                print(lat,lon)
                p = subprocess.Popen(['sac'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                s = ""
                s += "r %s\n" % f
                s += "ch stla %.6f\n" % float(lat)
                s += "ch stlo %.6f\n" % float(lon)
                s += "wh\n"
                s += "q\n"
                p.communicate(s.encode())
            else:
                continue
