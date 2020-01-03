# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:04:47 2016

@author: malz
"""

from dateutil.parser import parse
import ReadLib as rl
from numpy import array
import numpy as np
import csv
import os.path as path

def data_path_generator(fol,user_path,file1): 
    temp='User'+str(fol)
    return path.join(user_path, temp, str(file1) + '.csv')

def FeatureStore(pathS,arrayOfGen):
    list1=list(arrayOfGen)
    #print list1
    outFile=open(pathS,'wb')
    wr=csv.writer(outFile)
    wr.writerows(list1)
    
def ActivityFeatStore(r1,r2,r3,pathin,act,t0,t1):
    actData=[]
    x=1
    for user in range(r1,r2):
        
        tempPath = data_path_generator(str(user),pathin,act+'_Fea')
        print tempPath
        with open(tempPath,'r') as fin:
            rd=csv.reader(fin,delimiter=',')
            for row in rd:
                actData.append(row)
                x=x+1
                print x
    for user in range(r2,r3):
        
        tempPath = data_path_generator(str(user),pathin,act+'_Fea')
        print tempPath
        with open(tempPath,'r') as fin:
            rd=csv.reader(fin,delimiter=',')
            for row in rd:
                actData.append(row) 
                x=x+1
                print x
    #print actData
    tempWrite=data_path_generator('Activity',pathin,act)
    print tempWrite
    with open(tempWrite,'wb') as fOut:
        wr=csv.writer(fOut)        
        wr.writerows(actData)