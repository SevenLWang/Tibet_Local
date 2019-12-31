from glob import glob
import os
import pandas as pd

datadir = '/work/wang_li/Program/Tibet/'
stations = pd.read_table('/work/wang_li/Program/LOCAL_X1_YOUYIMS/X1.POS.WITH.LOCID.V20151213.txt',names=['Net','Station','Number','Longitude','Latitude','Num'],encoding='gb2312',sep=' ')
stlamax = max(stations['Latitude'])
stlomax = max(stations['Longitude'])
stlamin = min(stations['Latitude'])
stlomin = min(stations['Longitude'])
print(stlamax,stlomax,stlamin,stlomin)

for d in glob(datadir + '2012*'):
    for f in glob(d + '/*.SAC'):
        cmd = "saclst evla evlo f %s" % (f)
        junk, evla, evlo = os.popen(cmd).read().split()
        evla = float(evla); 
        evlo = float(evlo);
        if (evla < 29 and evla > 25 and evlo < 107 and evlo > 103):
            cmd = "cp -r %s Fault" % (d)
            print(cmd)
            os.system(cmd)
            break
        else:
            break
                
