# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:39:49 2016

@author: malz
"""
import csv as csv
import numpy as np
from dateutil.parser import parse
from sklearn.cross_validation import cross_val_score
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn import tree
import matplotlib.pyplot as plt
import rocPlot as roc
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import roc_curve, auc
from sklearn import metrics
import pandas as pd
#import ggplot as gg
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.preprocessing import label_binarize
from sknn.mlp import Classifier, Layer
from mlp1 import MLPClassifier
from sklearn.linear_model import LinearRegression
graphs_status=False

def perf_measure_new(y_test, y_score):   
    
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
    
    return(TP, FP, TN, FN)

def EERCalc(X,y_test, y_pred,clf):
    diff_arr = []
    FPR=[]
    FNR=[]
    print X,y_test, y_pred 
    for i in range(1,101):
        threshold = float(i)/float(100)
        print threshold
        #print threshold
#threshold=0.999
        y_predNew=[]
        for i in range(0,len(X)):
            if(X[i][0]>threshold):
                y_predNew.append(0)
            else:
                y_predNew.append(1)
        FP, FN, diff=perf_measure_new(y_test,y_predNew)
        print FP, FN, diff
        FPR.append(FP)
        FNR.append(FN)
        diff_arr.append(diff)
    a=FPR[diff_arr.index(min(diff_arr))]
    b=FNR[diff_arr.index(min(diff_arr))]
    print min(diff_arr)
#    with open("/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/"+clf+".csv", 'w') as w:
#        dwri=csv.writer(w)
#        #print FPR.typeof()
#
#        for i in range(0,100):
#            #x= str(FPR[i])+","+ str(FNR[i]
#                                
#            dwri.writerow([FPR[i],FNR[i]])
#            #dwri.writerow(FNR[i])
    print "EER:"
    print (float(a)+float(b))/float(2)
    return (float(a)+float(b))/float(2)

def crossValidate(X,y):
  "7-fold cross-validation with an SVM with a set of labels and vectors"
  clf = svm.LinearSVC()
  #clf1=neural_network.BernoulliRBM()
#  clf1.fit(X,y=None)
#  knn=KNeighborsClassifier(n_neighbors=1)
  #knn.fit(np.array(X),y)
  #print knn.predict(np.array(X)[93])
  scores = cross_validation.cross_val_score(clf, np.array(X), y, cv=7)
  return scores.mean()


def Knn(X_train, y_train, X_test, y_test):
    clf=KNeighborsClassifier(n_neighbors=19)
    print '==========using knn classifier=========='
    clf.fit(X_train,y_train)
    print clf.score(X_test, y_test)
    y_pred=clf.predict(X_test)
    perf_measure_new(y_test,y_pred)
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"knn")
    

def randomForest_new(X_train1, y_train1, X_test1, y_test1):
    X_train=np.array(X_train1).astype(np.float)
    y_train=np.array(y_train1).astype(np.float)
    X_test=np.array(X_test1).astype(np.float)
    y_test=np.array(y_test1).astype(np.float)
    clf=rfc(n_estimators=120)
    print '==========Using Random forest classifier=========='
    clf.fit(X_train,y_train)
    print clf.score(X_test,y_test)
    y_pred=clf.predict(X_test)
    perf_measure_new(y_test,y_pred)
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"knn")
