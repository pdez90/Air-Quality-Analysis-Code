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

ftp=FTP(host='model510.atmosphericsensors.co.uk', user= 'u40709730-Model510', passwd='kL;219,tY')
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
    os.chdir('..')
    ftp.cwd('..')
    print(ctr)
    
for i in range (0, len(node)):
    os.chdir(str(node[i])+'/')
    fileList=glob.glob("*.csv")
    dfList=[]
    for file in fileList:
        print file
        df=pandas.read_csv(file, header=None)
        dfList.append(df)
    concatDf= pandas.concat(dfList, axis=0)
    with open((str(node[i])+'Concat'), 'wb') as fhandle:
        concatDf.to_csv(fhandle, index=None)
        

        

    
    
    
    
    


    
    
   
    
    
    
    
    
    