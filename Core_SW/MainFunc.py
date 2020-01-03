# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:27:15 2016

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
import random
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
         
write_path='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/'
csv_columns = ['id','indra_time','browser_latency','reading_time','attention_esense','meditation_esense','eeg_power','raw_values','signal_quality','createdAt','updatedAt']
csv_col_Act=['id','raw_values','eeg_power']
sq=199;								

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

def data_path_generator(fol,user_path,file1): 
    temp='User'+str(fol)
    return path.join(user_path, temp, str(file1) + '.csv')

def UserFilter():
    for i in range(1,16):
        print i
        rraS.ReadRangeandStore(i,actDict1[0]['t0'],actDict1[6]['t1'],write_path,csv_columns,sq)
    for i in range(16,31):
        print i
        rraS.ReadRangeandStore(i,actDict2[0]['t0'],actDict2[6]['t1'],write_path,csv_columns,sq)

def ActSplit():
    for i in range(1,16):
        print i
        for a in range(0,7):
            apuS.ActReadStore(i,actDict1[a]['t0'],actDict1[a]['t1'],write_path,csv_columns,sq,actDict1[a]['Act'])
    for i in range(16,31):
        print i
        for a in range(0,7):
            apuS.ActReadStore(i,actDict2[a]['t0'],actDict2[a]['t1'],write_path,csv_columns,sq,actDict2[a]['Act'])

def FeatAct(user,actDict):
    
    for i in range(0,7):
        pathTem=data_path_generator(user,write_path,actDict[i]['Act'])
        #if pathStatus==True:
        print pathTem
        arrayOfGen=featurevectorgenerator.feature_vector_generator(user,actDict[i]['t0'],actDict[i]['t1'],sq,pathTem)
        newPath=data_path_generator(user,write_path,actDict[i]['Act']+'_Fea')
        print newPath
        fS.FeatureStore(newPath,arrayOfGen)
    
def FeatUser(r1,r2, actDict):
    
    for user in range(r1,r2):
        pathTem=data_path_generator(user,write_path,user)
        if pathStatus==True:
            print pathTem 
        arrayOfGen=featurevectorgenerator.feature_vector_generator(user,actDict[0]['t0'],actDict[6]['t1'],sq,pathTem)
        newPath=data_path_generator(user,write_path,str(user)+'_Feat')
        print newPath
        fS.FeatureStore(newPath,arrayOfGen)
    
    
def Prep1():
    UserFilter()
    ActSplit()
    for i in range(1,16):
        FeatAct(i,actDict1)
    for i in range(16,31):
        FeatAct(i,actDict2)
    FeatUser(1,16,actDict1)
    FeatUser(16,31,actDict2)
    
def XyGenUser301(path,k):
    '''Human authentication between two users'''
    d=defaultdict(list)
    #k=10
    for i in range(1,31):
        tempPath = data_path_generator(str(i),path,str(i)+'_Feat')
        #tempPath = data_path_generator(str(i),path,str(i)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                if i ==k:
                    d[0].append(row)
                if i==k+1:
                    d[1].append(row)
    X,y=vectorsAndLabels([d[0],d[1]])
    #if pathStatus==True:    
    #print y
    return X,y    
    
def XyGenUser30(path):
    '''User identification based on cross activity'''
    d=defaultdict(list)
    male=[2,4,5,11,13,12,14]
    female=[1,3,8,9,22,24,28]
    for i in range(1,31):
        if i in male:
            tempPath = data_path_generator(str(i),path,str(i)+'_Feat')
            with open(tempPath,'r') as f:
                dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                d[0].append(row)
        if i in female:
            tempPath = data_path_generator(str(i),path,str(i)+'_Feat')
            with open(tempPath,'r') as f:
                dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                d[0].append(row)
            
        
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                d[i-1].append(row)
    X,y=vectorsAndLabels([d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],
                          d[16],d[17],d[18],d[19],d[20],d[21],d[22],d[23],d[24],d[25],d[26],d[27],d[28],d[29]])
    if pathStatus==True:    
        print y
    return X,y

def XyGenAct07(path,actDict):
    '''Gender classification based on activity'''
    d=defaultdict(list)
#    actDict={'0':'blink',
#             '1':'relax',
#             '2':'math',
#             '3':'music',
#             '4':'video',
#             '5':'think'}
    for i in range(0,7):
        tempPath = data_path_generator('Activity',path,actDict[i]['Act'])
        if pathStatus==True:
            print tempPath
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[i-1].append(row)
    
    X,y=vectorsAndLabels([d[0],d[1],d[2],d[3],d[4],d[5],d[6]])
    return X,y 
def XycrossGenAct(path,actDict):
    '''Gender classification based on cross activity'''
    d=defaultdict(list)
#    actDict={'0':'blink',
#             '1':'relax',
#             '2':'math',
#             '3':'music',
#             '4':'video',
#             '5':'think'}
    male=[2,4,5,6,7,10,11]
    female=[1,3,8,9,22,24,28]
    
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
    
    X,y=vectorsAndLabels([d[0],d[1]])
    return X,y        
def convertXYtoTT(X,y):
    
    writePath1="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/"+feat+"X.csv"
    writePath2="/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/"+feat+"y.csv"
    with open(writePath1,'w') as w:
            dwri=csv.writer(w)
            dwri.writerows(X)
    y1=np.array(y)
    y2=y1.T
    print y2
    with open(writePath2,'w') as w:
            dwri=csv.writer(w)
            dwri.writerow(y)
    
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
    
    X,y=vectorsAndLabels([d[0],d[1]])
   
    #roc.plotRoc(np.array(X),np.array(y),'Gender using '+feat)
    return X,y

def ColorGenAut(blue,green,red,yellow,pathin):
    '''This function takes arguments of users who selected blue,green,red and yellow colors and their color
    activity feature vectors are used to train and test which color activity does the user selected
    the path of the user data is given using which the function loads the color_fea file'''
    d=defaultdict(list)
    for m in blue:
        tempPath = data_path_generator(m,pathin,'color_Fea')
        #tempPath = data_path_generator(m,pathin,str(m)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[0].append(row)
        if pathStatus==True:
            print tempPath
    for f in green:
        tempPath=data_path_generator(f,pathin,'color_Fea')
        #tempPath=data_path_generator(f,pathin,str(f)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[1].append(row)
        if pathStatus==True:
            print tempPath
    for f in red:
        tempPath=data_path_generator(f,pathin,'color_Fea')
        #tempPath=data_path_generator(f,pathin,str(f)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[2].append(row)
        if pathStatus==True:
            print tempPath
    for f in yellow:
        tempPath=data_path_generator(f,pathin,'color_Fea')
        #tempPath=data_path_generator(f,pathin,str(f)+'_Feat')
        with open(tempPath,'r') as f:
            dwr=csv.reader(f,delimiter=',')
            for row in dwr:
                  d[3].append(row)
        if pathStatus==True:
            print tempPath
    
    X,y=vectorsAndLabels([d[0],d[1],d[2],d[3]])
    
    return X,y
    
def runAlgos(X,y,Act):
#    scores, pvalues = chi2(X, y)
#    print 'pvalues are------------'
#    print pvalues
    #alg.neural(X,y)
    
    return alg.knnExec(array(X),array(y),Act), alg.svmExev(array(X),array(y),Act), alg.naiveBayes(array(X),array(y),Act), alg.randomForest(array(X),array(y),Act)
    #alg.svmExev(array(X),array(y),Act)
    #alg.naiveBayes(array(X),array(y),Act)
    #alg.randomForest(array(X),array(y),Act)
    #alg.decisionTree(array(X),array(y),Act)

def Finaltest():
    knn =[]
    svm=[]
    NB=[]
    RF=[]
    Act="Human Authentication"
    for i in range(1,30):
        print '==========================================================================='
        print 'The mean accuracy for human authentication is as follows:'+str(i)
        X,y=XyGenUser301(write_path,i)
        knn.append(alg.knnExec(array(X),array(y),Act))
        svm.append(alg.svmExev(array(X),array(y),Act))
        NB.append(alg.naiveBayes(array(X),array(y),Act))
        RF.append(alg.randomForest(array(X),array(y),Act))
    print knn
    print "Avg EER for Knn is :"
    print reduce(lambda x, y: x + y, knn) / len(knn)
    print svm
    print "Avg EER for svm is :"
    print reduce(lambda x, y: x + y, svm) / len(svm)
    print NB
    print "Avg EER for NB is :"
    print reduce(lambda x, y: x + y, NB) / len(NB)
    print RF
    print "Avg EER for RF is :"
    print reduce(lambda x, y: x + y, RF) / len(RF)
    
#        runAlgos(X,y,'Human Authen')
            
    #Prep1()
    print '==========================================================================='
    print 'The mean accuracy for human identification is as follows'
    #X,y=XyGenUser30(write_path)
    #runAlgos(X,y,'dummy')
    ##for i in range(0,7):
    ##    fS.ActivityFeatStore(1,16,31,write_path,actDict1[i]['Act'],actDict1[i]['t0'],actDict1[i]['t1'])
    #
    
    print '==========================================================================='
    print 'The mean accuracy for activity identification is as follows'
    X1,y1=XyGenAct07(write_path,actDict1)
    print runAlgos(X1,y1,'dummy')
    print "EER is above"
    
    Xb,yb=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'blink_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using blink activity  is as follows:'
    print runAlgos(Xb,yb,'Blink')
    print "EER is above"
    
    Xc,yc=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'color_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using color activity is as follows:'
    
    print runAlgos(Xc,yc,'Color')
    print "EER is above"
    
    Xr,yr=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'relax_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using relax activiy is as follows'
    print runAlgos(Xr,yr,'Relax')
    print "EER is above"
    
    Xv,yv=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'video_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using video activiy is as follows'
    print runAlgos(Xv,yv,'Video')
    print "EER is above"
    
    Xm,ym=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'music_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using music activiy is as follows'
    print runAlgos(Xm,ym,'Music')
    print "EER is above"
    
    Xt,yt=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'think_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using think activiy is as follows'
    print runAlgos(Xt,yt,'Think')
    print "EER is above"
    
    Xma,yma=MFGenAut([4,5,6,7,15,16,17],[1,3,8,9,22,24,28],write_path,'math_Fea')
    print '==========================================================================='
    print 'The mean accuracy for gender identification using math activiy is as follows'
    print runAlgos(Xma,yma,'Math')
    print "EER is above"
    
#X3,y3=ColorGenAut([1,2,5,6,7,11,13,14,15,17,19,21,23,25,26,30],[9,28,12,16,18,20],[3,8,22,24,10,27,29],[4],write_path)
#print '==========================================================================='
#print 'The mean accuracy for color identification using color activiy is as follows'
#runAlgos(X3,y3,'4')

#print '==========================================================================='
#print 'The mean accuracy for human authentication is as follows'
#for k in range(1,31):
#    print "K Value is: "
#    print k
#    X,y=XyGenUser301(write_path,k)
#    runAlgos(X,y,'Human Authen')
def Final2():
    knn=[]
    svm=[]
    NB=[]
    rf=[]

    for i in range(1,200):
        group1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
        group2=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
        g1=random.choice(group1)
        g2=random.choice(group2)
        Xc,yc=MFGenAut([g1],[g2],write_path,'think_Fea')
        knn.append(alg.knnExec(Xc,yc,"color"))
        svm.append(alg.svmExev(Xc,yc,"color"))
        NB.append(alg.naiveBayes(Xc,yc,"color"))
        rf.append(alg.randomForest(Xc,yc,"color"))
        
    #Finaltest()
        print '==========================================================================='
        print 'The mean accuracy for gender identification using color activity is as follows:'
        print reduce(lambda x, y: x + y, knn) / len(knn)
        print reduce(lambda x, y: x + y, svm) / len(svm)
        print reduce(lambda x, y: x + y, NB) / len(NB)
        print reduce(lambda x, y: x + y, rf) / len(rf)
        print "EER is above"
def Prep2():
    #UserFilter()
    #ActSplit()
    for i in range(1,2):
        FeatAct(i,actDict1)
   # for i in range(16,31):
    #    FeatAct(i,actDict2)      

Prep2()