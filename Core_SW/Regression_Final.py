# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:06:48 2016

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
import Algos_RModel as alg
#import rocPlot as roc
from sklearn.feature_selection import chi2
#from mlp1 import MLPClassifier
from sklearn.linear_model import LinearRegression
import pandas as pd
from itertools import islice
import pandas as pd
pathStatus=True

def data_path_generator(fol,user_path,file1): 
    temp='User'+str(fol)
    return path.join(user_path, temp, str(file1) + '.csv')

def vectorsAndLabels(arrayOfGenerators):
  '''Takes an array of generators and produces two lists X and y
  where len(X) = len(y),
  X is the vectors, y is their (numerical) labels.'''
  X = []
  y = []
  currentLabel = 0
  for generator in arrayOfGenerators:
    
  	for vector in generator:
  		X.append(vector)
  		y.append(currentLabel)
  	currentLabel+=1
  return X, y
  
def GetXandyfromFile(readPath,writePathX,writePathy,write):
    X=[] 
    y=[]
    
    with open(readPath,'r') as f:
        dwr=list(csv.reader(f,delimiter=','))
        column1= len(dwr[0])
        for row in dwr:
            r=[]
            c=[]
            for column in range(0,len(dwr[0])-1):
                r.append(row[column])
            c.append(row[column1-1])
            
            X.append(r)
            y.append(c)
    if write==1:
        with open(writePathX,'w') as w:
            dwri=csv.writer(w)
            dwri.writerows(X)
        with open(writePathy,'w') as wy:
            dwri=csv.writer(wy)
            dwri.writerows(y)
    
    return X,y
def readAndWrite(read1Female, read2Male, write):
    X=[]
    if read1Female!=0:
        with open(read1Female,'r') as r1:
            dwr=csv.reader(r1,delimiter=',')
            for row in dwr:
                row.append(1)
                X.append(row)
    if read2Male!=0:
        
        with open(read2Male,'r') as r2:
            dwr=csv.reader(r2,delimiter=',')
            for row in dwr:
                row.append(0)
                X.append(row)
            
    with open(write,'w') as w:
        dwr=csv.writer(w)
        dwr.writerows(X)
        
def MFGenAut(maleList,femaleList,pathin,feat):
    '''This function reads the male and female list and loads the feature passed as parameter
    The authentication of male or female is done based on the activity that is passed as parameter'''
    d=defaultdict(list)
    for m in maleList:
        #tempPath = data_path_generator(m,pathin,feat)
        tempPath = data_path_generator(m,pathin,str(m)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[0].append(row)
        if pathStatus==True:
            print tempPath
    for f in femaleList:
        #tempPath=data_path_generator(f,pathin,feat)
        tempPath=data_path_generator(f,pathin,str(f)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[1].append(row)
        if pathStatus==True:
            print tempPath
    return d[0], d[1]
    #X,y=vectorsAndLabels([d[0],d[1]])
    #roc.plotRoc(np.array(X),np.array(y),'Gender using '+feat)
    #return X,y
    
rPathTrain="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/Train.csv"
wPathTainX="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/Xtrain.csv"
wPathTrainy="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/ytrain.csv"
rPathTest="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/Test.csv"
wPathTestX="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/Xtest.csv"
wPathTesty="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/ytest.csv"

read1Female="/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/User25/25_Feat.csv"
read2Male="/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/User4/4_Feat.csv"
writeFemaleAndMale="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/User1/11Test.csv"
readAndWrite(0,read2Male,writeFemaleAndMale)

Xtrain,ytrain=GetXandyfromFile(rPathTrain,wPathTainX,wPathTrainy, 0)
Xtest,ytest=GetXandyfromFile(writeFemaleAndMale,wPathTestX,wPathTesty,0)
alg.randomForest_new(Xtrain,ytrain,Xtest,ytest)

