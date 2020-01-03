# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:25:08 2016

@author: malz
"""

from dateutil.parser import parse
import ReadLib as rl
from numpy import array
import numpy as np
import csv
import os.path as path

def WriteData_path_evaluation (result_path,subjectnum,ActName):
    temp='User'+str(subjectnum)
    return path.join(result_path,temp, str(ActName) + '.csv')
    
def ActReadStore(subject,t0,t1,result_path,csv_columns,sq,Act):
    write_path=WriteData_path_evaluation(result_path,subject,Act)
    print write_path
    csv_header=csv_columns
    readings=rl.readings(subject,t0,t1,sq)
    aRead=array(readings)
    with open(write_path,"wb") as f:
        dwr=csv.DictWriter(f,csv_header)
        dwr.writeheader()
        dwr.writerows(aRead)
    
def ActRead(subject,t0,t1,result_path,csv_columns,sq,Act):
    csv_header=csv_columns
    readings=rl.readings(subject,t0,t1,sq)
    aRead=array(readings)
    return aRead
