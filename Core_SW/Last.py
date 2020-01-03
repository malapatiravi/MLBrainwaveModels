# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:29:02 2016

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
import rocPlot as roc
from sklearn.feature_selection import chi2
import random

write_path='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/'



def data_path_generator(folder,file1):
    temp='User'+str(folder)
    return path.join(write_path, temp, str(file1) + '.csv')


def Read(class1, class2,  file1,file2):
    dX=[] 
    dy=[]
    for i in class1:
        with open(data_path_generator(i,file1),'r') as f:
        #with open(data_path_generator(i,str(i)+'_Feat'),'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
               dX.append(row)
               dy.append(0)
    for i in class2:
        with open(data_path_generator(i,file2),'r') as f:
        #with open(data_path_generator(i,str(i)+'_Feat'),'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
               dX.append(row)
               dy.append(1)
    return dX, dy
def GenderNew():
    knn=[]
    rf=[]
    knnL=[]
    rfL=[]
    for i in range(1,5):
        male=[2,4,5,6,7,10,11,15,16,17,18,20,21,23,25,26,27,29,30]
        female=[9,22,24,28]
        X,y=Read([1,3,8,28],[12,13,14,19],"math_Fea","math_Fea")
        #Xt,yt=Read([24],[25],"color_Fea","color_Fea")
        k=random.choice(male)
        l=random.choice(female)
        print l,k
        Xt,yt=Read([l],[k],"math_Fea","math_Fea")
        kValue=alg.Knn(X,y,Xt,yt)
        rValue=alg.randomForest_new(X,y,Xt,yt)
        if(kValue>0.3):
            knnL.append(kValue)
        else:
            knn.append(kValue)
        if(rValue>0.3):
              rfL.append(rValue)
        else:
            rf.append(rValue)
                  
    print len(knn)
    print reduce(lambda x, y: x + y, knn) / len(knn)
    print len(rf)
    print reduce(lambda x, y: x + y, rf) / len(rf)
    print len(knnL)
    print reduce(lambda x, y: x + y, knnL) / len(knnL)
    print len(rfL)
    print reduce(lambda x, y: x + y, rfL) / len(rfL)
    
def CrossActivity():
    knn=[]
    rf=[]
    KnnF=[]
    rfF=[]
    act="math_Fea"
    impo_act=["music_Fea","video_Fea","color_Fea","think_Fea","relax_Fea"]
        
    for i in range(1,31):
        genuine=i
        for im in range(1,31):
            impostor=im
            if(impostor!=genuine):
                X,y=Read([genuine],[impostor],"math_Fea","math_Fea")
                Xt,yt=Read([genuine],[impostor],"color_Fea","color_Fea")
                kValue=alg.Knn(X,y,Xt,yt)
                rValue=alg.randomForest_new(X,y,Xt,yt)
                knn.append(kValue)
                rf.append(rValue)
            
        print len(knn)
        meanK=reduce(lambda x, y: x + y, knn) / len(knn)
        KnnF.append(meanK)
        print meanK
        print len(rf)
        meanR=reduce(lambda x, y: x + y, rf) / len(rf)
        rfF.append(meanR)
        print meanR
    print KnnF
    print reduce(lambda x, y: x + y, KnnF) / len(KnnF)
    print rfF
    print reduce(lambda x, y: x + y, rfF) / len(rfF)

GenderNew()
    
    
    