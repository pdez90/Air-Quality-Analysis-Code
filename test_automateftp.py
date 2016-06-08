# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:41:25 2016

@author: pdez
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:51:05 2016

@author: pdez
"""

import glob
import pandas
import os
from ftplib import FTP
import matplotlib.pyplot as plt

ftp=FTP(host='model510.atmosphericsensors.co.uk', user= 'u40709730-Model510', passwd='kL;219,tY')
ftp.set_pasv(False)
ftp.nlst()
os.chdir('Alphasense/')
node=["Node41","Node42", "Node43", "Node45", "Node46", "Node55", "Node68"]
for i in range(0,len(node)):
    ftp.cwd(node[i])
    os.chdir(str(node[i])+'/')
    files=ftp.nlst()
    existingFiles=glob.glob("*.csv")
    print(len(existingFiles))
    ctr=0
    for file in files:
        if file not in existingFiles:
            with open(file, 'wb') as fhandle:
                 ftp.retrbinary('RETR %s' % file, fhandle.write)
            print("New file written")
            ctr=ctr+1
            print(ctr)
        else:
            print("Continuing")
            continue
#    os.chdir('..')
#   ftp.cwd('..')
#    print(ctr)
    
#for i in range (0, len(node)):
    #os.chdir(str(node[i])+'/')
    fileList=glob.glob("*.csv")
    dfList=[]
    for file in fileList:
        try:
           df=pandas.read_csv(file, header=None, sep=',', encoding='utf-8')
           dfList.append(df)
        except:
              pass
        print("check")
    concatDf= pandas.concat(dfList, axis=0)
    concatDf.columns=["Indent-MD", "Node ID", "Date", "Time", "Sub Seq", "NO2 ppb", "O3 ppb", "NO ppb", "SO2 ppb", "NO2 ppb TC", "O3 ppb TC", "NO ppb TC", "SO2 ppb TC", "PID ppb", "CO2 ppm", "Ext Temp", "Ext RH", "PM1", "PM2.5", "PM10", "SFR", "PerCnt", "Ambient Sound", "EC1_WE_uV", "EC1_AE_uV", "EC2_WE_uV", "EC2_AE_uV", "EC3_WE_uV", "EC3_AE_uV", "EC4_WE_uV", "EC4_AE_uV","EC Temp", "PID uV", "Bin0", "Bin1", "Bin2", "Bin3", "Bin4", "Bin5", "Bin6", "Bin7", "Bin8", "Bin9", "Bin10", "Bin11", "Bin12", "Bin13", "Bin14", "Bin15", "GPRS Sig Lvl", "RadioCnt"]
    concatDf["Date"]=pandas.to_datetime(concatDf.Date)
    concatDf.sort(["Date", "Time"], ascending=[True, True], inplace='True')
   #concatDf=concatDf[concatDf["Time"]!=""]
   #concatDf= concatDf[(concatDf["Date"] != "0") | (concatDf["Date"] != "0/0/0")]
    #concatDf.plot(x="Time", y="PM2.5")
    #plt.show()
    with open("Concatenate_test.csv", "wb") as fhandle:
         concatDf.to_csv(fhandle, index=None)
         
    os.chdir('..')
    ftp.cwd('..')
    print(ctr)
    
         

        
        

        

    
    
    
    
    


    
    
   
    
    
    
    
    
    