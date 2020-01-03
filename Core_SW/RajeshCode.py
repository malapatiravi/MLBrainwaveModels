# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:25:31 2016

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
#import featurevectorgenerator
import FeatureStore as fS
from collections import defaultdict
import Algos as alg
import rocPlot as roc
from sklearn.feature_selection import chi2
import random

def EERCalc(X,y_test,clf):
    #print y_test,y_pred
    #print X,clf
    thr=[]
    diff_arr = []
    FPR=[]
    FNR=[]
    for i in range(0,101):
        threshold = float(i)/float(100)
#        print threshold
#threshold=0.999
        y_predNew=[]
        thr.append(threshold)
        for i in range(0,len(X)):
            #print X[i]
            if(X[i]>threshold):
                y_predNew.append(1)
            else:
                y_predNew.append(0)
        FP, FN, diff=perf_measure_new(y_test,y_predNew,"color")
#        print "--------------------"       
#        print FP, FN, diff
#        print X, y_test, y_predNew
#        print "--------------------"       
        FPR.append(FP)
        FNR.append(FN)
        diff_arr.append(diff)
    a=FPR[diff_arr.index(min(diff_arr))]
    b=FNR[diff_arr.index(min(diff_arr))]
    t=thr[diff_arr.index(min(diff_arr))]
    #print t
#    print "Minimum"    
#    print a, b, min(diff_arr)
    with open("/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/"+clf+".csv", 'w') as w:
        dwri=csv.writer(w)
        #print FPR.typeof()

        for i in range(0,100):
            #x= str(FPR[i])+","+ str(FNR[i]
                                
            dwri.writerow([FPR[i],FNR[i]])
            #dwri.writerow(FNR[i])
#    print "EER:"
#    print (float(a)+float(b))/float(2)
    return (float(a)+float(b))/float(2), t
    
    
def perf_measure_new(y_test, y_score,Act):   
    
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    
    for i in range(len(y_score)): 
        if y_test[i]==y_score[i]==1:
           TP += 1
    for i in range(len(y_score)): 
        if y_test[i]==1:
            if y_test[i]!=y_score[i]:
                FN += 1
    for i in range(len(y_score)): 
        if y_test[i]==y_score[i]==0:
           TN += 1
    for i in range(len(y_score)): 
        if y_test[i]==0:
            if y_test[i]!=y_score[i]:
                FP += 1
    #print len(y_test), FP, FN
    
    FPR=float(FP)/float(len(y_test))
    FNR=float(FN)/float(len(y_test))
    #print FNR
    result=abs(FPR-FNR)
    #print result
    return FPR, FNR, result
def data_path_generator(folder,file1):
    temp='User'+str(folder)
    return path.join(folder, str(file1) + '.txt')
    
#input="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TRAIN_SCORE_FOLDER/kNN-Euclidean/"
#input="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TRAIN_SCORE_FOLDER/RandomForest/"
#input="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDER/kNN-Euclidean/"
#input="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDER/RandomForest/"
#input="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDERAllSwipes/TEST_SCORE_FOLDER/kNN-Euclidean/"
input ="/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDERAllSwipes/TEST_SCORE_FOLDER/RandomForest/"
inputx=["/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDER/kNN-Euclidean", "/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TEST_SCORE_FOLDER/RandomForest", "/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllBMs/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSW_BM_FUSED/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSW_BM_FUSED/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSW_BM_FUSED/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSW_BM_FUSED/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSwipes/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSwipes/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSwipes/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/AllSwipes/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Left_SW_BM_Fused/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Left_SW_BM_Fused/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Left_SW_BM_Fused/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Left_SW_BM_Fused/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftSwipes/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftSwipes/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftSwipes/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftSwipes/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Right_SW_BM_Fused/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Right_SW_BM_Fused/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Right_SW_BM_Fused/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/Right_SW_BM_Fused/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightBMs/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightBMs/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightBMs/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightBMs/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightSwipes/TEST_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightSwipes/TEST_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightSwipes/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/RightSwipes/TRAIN_SCORE_FOLDER/RandomForest","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftBMs/TEST_SCORE_FOLDER/kNN-Euclidean", "/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftBMs/TEST_SCORE_FOLDER/RandomForest", "/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftBMs/TRAIN_SCORE_FOLDER/kNN-Euclidean","/media/malz/01D0E9654C2905F0/IntermediateFilesAndResults/LeftBMs/TRAIN_SCORE_FOLDER/RandomForest"]
#write_path=input+str("result.csv")

X=defaultdict(list)
y=defaultdict(list)

execlude=[6,7 , 22,17,23 ,32]
for fp in inputx:
    mean=[]
    EERvalue=[]
    ip=fp
    write_path=ip+str("result.csv")
    for i in range(1,34):
        
        file1="User"+str(i)+"Impostor"
        file2="User"+str(i)+"Genuine"
        #file3=
        if i not in execlude:
            print data_path_generator(ip,file1)
            with open(data_path_generator(ip,file1),'r') as f:
                dwr=csv.reader(f,delimiter='\t')
                for row in dwr:
                    row1=float(row[0])
                    y[i].append(0)
                    X[i].append(row1)
            with open(data_path_generator(ip,file2),'r') as f:
                dwr=csv.reader(f,delimiter='\t')
                for row in dwr:
                    row1=float(row[0])
                    y[i].append(1)
                    X[i].append(row1)
            #print X[i]
            #print y[i]
            EERvalue.append(EERCalc(X[i],y[i],"test"))
    print EERvalue
    #print reduce(lambda x, y: x + y, EERvalue) / len(EERvalue)
    for val in EERvalue:
        mean.append(val[0])
    meanFinal=(reduce(lambda x, y: x + y, mean) / len(mean), "Mean is")
    EERvalue.append(meanFinal)
    print type(EERvalue)
    with open(write_path,'w') as testOut:
        wr=csv.writer(testOut)
        for i in EERvalue:        
            wr.writerow(i)
        
            
