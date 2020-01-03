# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:10:50 2016

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
#from mlp1 import MLPClassifier
from sklearn.linear_model import LinearRegression
import pandas as pd
from itertools import islice
pathStatus=True

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
def RowCount(filePath):
    with open(filePath, 'r') as fin:
        gRead=csv.reader(fin,delimiter=',')        
        row_count = sum(1 for row in gRead)
        print row_count
    return row_count
    
def FirstUser():
    sl=5
    for genuine in range(1,31):
        genuinePath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(genuine)+"_Feat")
        trainPath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","Train")
        testPath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","Test")
        Train=[]
        Test=[]
        with open(genuinePath,'r') as gin:
            gRead=csv.reader(gin,delimiter=',')
            for item in islice(gRead,0,80):
                item.append(1)
                Train.append(item)
            rowCount=RowCount(genuinePath)
            
            for item in islice(gRead,0,40):
                item.append(1)
                Test.append(item)
        
        
        #print trainPath
        #print testPath                
        #print genuinePath
        sl=3
        for imposter in range(1,31):
            if(imposter!=genuine):
                print imposter,genuine
                print sl
                imposterPath=data_path_generator(str(imposter),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(imposter)+"_Feat")
                print imposterPath
                with open(imposterPath,'r') as iin:
                    iRead=csv.reader(iin,delimiter=',')
                    for item in islice(iRead,sl,sl+3):
                        print item
                        item.append(0)
                        Train.append(item)
                    sl=sl+3
        
        sl=6
        for imposter in range(1,31):
            if(imposter!=genuine):
                print imposter, genuine
                print sl
                imposterPath=data_path_generator(str(imposter),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(imposter)+"_Feat")
                print imposterPath
                with open(imposterPath,'r') as iin:
                    iRead=csv.reader(iin,delimiter=',')
                    for item in islice(iRead,sl,sl+1):
                        print item
                        item.append(0)
                        Test.append(item)
                    sl=sl+3

        with open(trainPath, 'w') as trainOut:
            wr=csv.writer(trainOut)        
            wr.writerows(Train)
        with open(testPath,'w') as testOut:
            wr=csv.writer(testOut)        
            wr.writerows(Test)
        print "Done"

def SecondUserPython():
    sl=5
    
    for genuine in range(1,31):
        genuinePath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(genuine)+"_Feat")
        trainPath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(genuine)+"_Genuine")
        testPath=data_path_generator(str(genuine),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(genuine)+"_Imposter")
        Train=[]
        Test=[]
        Gen=[]
        Imp=[]
        with open(genuinePath,'r') as gin:
            gRead=csv.reader(gin,delimiter=',')
            for item in gRead:
                #item.append(1)
                #Train.append(item)
                Gen.append(item)
        with open(trainPath, 'w') as trainOut:
            wr=csv.writer(trainOut)        
            wr.writerows(Gen)
        
        
        #print trainPath
        #print testPath                
        #print genuinePath
        sl=3
        if(genuine>15):
            for imposter in range(1,15):
                if(imposter!=genuine):
                    print imposter,genuine
                    print sl
                    imposterPath=data_path_generator(str(imposter),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(imposter)+"_Feat")
                    print imposterPath
                    with open(imposterPath,'r') as iin:
                        iRead=csv.reader(iin,delimiter=',')
                        for item in islice(iRead,sl,sl+7):
                            
                            #item.append(0)
                            Imp.append(item)
                        sl=sl+3
            with open(testPath,'w') as testOut:
                 wr=csv.writer(testOut)        
                 wr.writerows(Imp)
        if(genuine<=15):
             for imposter in range(15,31):
                if(imposter!=genuine):
                    print imposter,genuine
                    print sl
                    imposterPath=data_path_generator(str(imposter),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(imposter)+"_Feat")
                    print imposterPath
                    with open(imposterPath,'r') as iin:
                        iRead=csv.reader(iin,delimiter=',')
                        for item in islice(iRead,sl,sl+7):
                            
                            #item.append(0)
                            Imp.append(item)
                        sl=sl+3
             with open(testPath,'w') as testOut:
                 wr=csv.writer(testOut)        
                 wr.writerows(Imp)
             
        print "Done"

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

def XyGenImp(i):
    d=defaultdict(list)
    Genuine=data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(i)+"_Genuine")
    Imposter=data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",str(i)+"_Imposter")
    with open(Genuine,'r') as f:
        dwr=csv.reader(f,delimiter=',')
        for row in dwr:
            d[0].append(row)
    with open(Imposter,'r') as f:
        dwr=csv.reader(f,delimiter=',')
        for row in dwr:
            d[1].append(row)
    X,y=vectorsAndLabels([d[0],d[1]])
    return X,y
def GenerateMaleandFemaleVectors(path,actDict):
    '''This function is used to generate feature vectors for gender identification'''
     male=[2,4,5,6,7,10,11]
     female=[1,3,8,9,22,24,28]
     d=defaultdict(list)
     for i in range(1,31):
        for k in range(1,6):
            if i in male:
                tempPath = data_path_generator(str(i),path,actDict[k]['Act']+'_Fea')
                if pathStatus==True:
                    print tempPath
                with open(tempPath,'r') as f:
                    dwr=csv.reader(f,delimiter=',')
                    for row in dwr:
                        d[0].append(row)
            if i in female:
                tempPath = data_path_generator(str(i),path,actDict[k]['Act']+'_Fea')
                if pathStatus==True:
                    print tempPath
                with open(tempPath,'r') as f:
                    dwr=csv.reader(f,delimiter=',')
                    for row in dwr:
                        d[1].append(row)
def runAlgos(X,y,Act):
#    scores, pvalues = chi2(X, y)
#    print 'pvalues are------------'
#    print pvalues
    #alg.neural(X,y)
    #alg.knnExec(array(X),array(y),Act)
    #alg.svmExev(array(X),array(y),Act)
    #alg.naiveBayes(array(X),array(y),Act)
   
    return  alg.randomForest(array(X),array(y),Act)
    #alg.decisionTree(array(X),array(y),Act)
#FirstUser()
def crossAuth():
    arr=[]
    
    for i in range (2,30):
        d=defaultdict(list)
        Genuine=data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","think_Fea")
        Imposter=data_path_generator(str(i-1),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","think_Fea")
        with open(Genuine,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                d[0].append(row)
        with open(Imposter,'r') as f1:
            dwr=csv.reader(f1,delimiter=',')
            for row in dwr:
                d[1].append(row)
        trainX,trainy=vectorsAndLabels([d[0],d[1]])
        Genuine1=data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","color_Fea")
        Imposter1=data_path_generator(str(i-1),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/","color_Fea")
        with open(Genuine1,'r') as f2:
            dwr=csv.reader(f2,delimiter=',')
            for row in dwr:
                d[2].append(row)
        with open(Imposter1,'r') as f3:
            dwr=csv.reader(f3,delimiter=',')
            for row in dwr:
                d[3].append(row)
        testX,testy=vectorsAndLabels([d[2],d[3]])
        arr.append(alg.randomForest_new(trainX,trainy,testX,testy,"color"))
    print reduce(lambda x, y: x + y, arr) / len(arr)

crossAuth()
  
#SecondUserPython()
#arr=[]
#for i in range(1,31):
#   print '==========================================================================='
#   print 'The mean accuracy for human authentication is as follows for USer: ',i
#   X,Y=XyGenImp(i) 
#   arr.append(runAlgos(X,Y,'Human Authen'))
#print reduce(lambda x, y: x + y, arr) / len(arr)


       #         print imposterPath
#    for k in range(0,7):
#            actData=[]
#            for i in range(1,31):
#                pathTem= data_path_generator(str(i),"/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[k]['Act']+"_Fea")
#                writePath= data_path_generator("RData","/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[k]['Act']+"_Fea")
#                print pathTem
#                with open(pathTem,'r') as fin:
#                   rd=csv.reader(fin,delimiter=',')
#                   i=0
#                   for row in islice(rd,10,20):
#                        print i
#                        i=i+1
#                        print row
#                with open(writePath, 'w') as csvoutput:
#                    wr=csv.writer(csvoutput)        
                   
                
                    
#                    for item in rd:
#                        item.append(i)
#                        item.append(k+1)
#                        actData.append(item)
        #print actData
    
#            pathTem1=data_path_generator("Label","/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/",actDict1[k]['Act']+"_Fea")
#            print pathTem1
#            with open(pathTem1, 'w') as csvoutput:
#                wr=csv.writer(csvoutput)        
#                wr.writerows(actData)
#                print pathTem



