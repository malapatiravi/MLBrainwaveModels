# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 07:07:01 2016

@author: malz
"""

from dateutil.parser import parse
import ReadLib as rl
from numpy import array
import numpy as np
import csv
import os.path as path
import ReadRangeandStore as rraS
import ActivityPerUserStore as apuS
import featurevectorgenerator
import FeatureStore as fS
from collections import defaultdict
import Algos as alg
import rocPlot as roc
from sklearn.feature_selection import chi2

pathStatus=False

actDict1=[{'Act':'blink','t0':parse('2015-05-09 23:32:36.911+00'),'t1':parse('2015-05-09 23:32:47.371+00')},
         {'Act':'relax','t0':parse('2015-05-09 23:32:48.872+00'),'t1':parse('2015-05-09 23:33:23.875+00')},
         {'Act':'math','t0':parse('2015-05-09 23:33:23.875+00'),'t1':parse('2015-05-09 23:33:58.875+00')},
         {'Act':'music','t0':parse('2015-05-09 23:33:58.875+00'),'t1':parse('2015-05-09 23:34:33.875+00')},
         {'Act':'video','t0':parse('2015-05-09 23:34:33.875+00'),'t1':parse('2015-05-09 23:35:08.878+00')},
         {'Act':'think','t0':parse('2015-05-09 23:35:08.878+00'),'t1':parse('2015-05-09 23:35:58.879+00')},
         {'Act':'color','t0':parse('2015-05-09 23:36:08.88+00'),'t1':parse('2015-05-09 23:38:09.889+00')}]

actDict2=[{'Act':'blink','t0':parse('2015-05-09 23:43:34.405+00'),'t1':parse('2015-05-09 23:43:46.308+00')},
         {'Act':'relax','t0':parse('2015-05-09 23:43:46.308+00'),'t1':parse('2015-05-09 23:44:21.309+00')},
         {'Act':'math','t0':parse('2015-05-09 23:44:21.309+00'),'t1':parse('2015-05-09 23:44:56.343+00')},
         {'Act':'music','t0':parse('2015-05-09 23:44:56.343+00'),'t1':parse('2015-05-09 23:45:31.342+00')},
         {'Act':'video','t0':parse('2015-05-09 23:45:31.342+00'),'t1':parse('2015-05-09 23:46:06.35+00')},
         {'Act':'think','t0':parse('2015-05-09 23:46:06.35+00'),'t1':parse('2015-05-09 23:46:56.345+00')},
         {'Act':'color','t0':parse('2015-05-09 23:47:06.344+00'),'t1':parse('2015-05-09 23:48:56.35+00')}]

def data_path_generator(fol,user_path,file1): 
    temp='User'+str(fol)
    return path.join(user_path, temp, str(file1) + '.csv')
def FirstStep():
    for k in range(0,7):
        actData=[]
        for i in range(1,31):
            pathTem= data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[k]['Act']+"_Fea")
            print pathTem
            with open(pathTem,'r') as fin:
                rd=csv.reader(fin,delimiter=',')
                for item in rd:
                    item.append(i)
                    item.append(k+1)
                    actData.append(item)
    #print actData

        pathTem1=data_path_generator("Label","/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[k]['Act']+"_Fea")
        print pathTem1
        with open(pathTem1, 'w') as csvoutput:
            wr=csv.writer(csvoutput)        
            wr.writerows(actData)
            print pathTem


pathWrite=data_path_generator("Label","/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","FinalLabel")
print pathWrite
actData=[]
for j in range(0,7):
    pathRead=data_path_generator("Label","/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[j]['Act']+"_Fea")
    print pathRead
    with open(pathRead,'r') as fin:
      rd=csv.reader(fin,delimiter=',')
      for item in rd:
          actData.append(item)
with open(pathWrite, 'w') as csvoutput:
    wr=csv.writer(csvoutput)        
    wr.writerows(actData)
    print pathWrite