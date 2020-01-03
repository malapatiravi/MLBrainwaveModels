# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:30:26 2016

@author: malz
"""
from dateutil.parser import parse
import ReadLib as rl
from numpy import array
import numpy as np
import csv
import os.path as path
#defnitions to change for each execution

def WriteData_path_evaluation (result_path,subjectnum):
    temp='User'+str(subjectnum)
    return path.join(result_path,temp, str(subjectnum) + '.csv')
  
def ReadRangeandStore(subject,t0,t1,result_path,csv_columns,sq):
    write_path=WriteData_path_evaluation(result_path,subject)
    print write_path
    csv_header=csv_columns
    readings=rl.readings(subject,t0,t1,sq)
    aRead=array(readings)
    with open(write_path,"wb") as f:
        dwr=csv.DictWriter(f,csv_header)
        dwr.writeheader()
        dwr.writerows(aRead)
    
