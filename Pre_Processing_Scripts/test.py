# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:38:46 2016

@author: malz
y_test = [2,2,2,3,3,1,1,2,1]
y_score = [1,1,2,1,3,2,1,2,1]
"""

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
import numpy as np
import math
import csv as csv
import numpy as np
from dateutil.parser import parse

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
y_test = [0,0,0,1,1,0,0,0,0]
y_score = [0,0,0,0,1,0,0,0,0]
labels1=[0,0,1,0,2,1,0,1,0]
labels2=[1,1,1,2,2,0,0,1,0]  


import pylab
import numpy
def plot1():
    x = numpy.linspace(0,1,100)
    y = 0.5*x 
    k=numpy.linspace(1,2.15,100)
    ko=0.25*x+0.25
    pylab.plot(x,y) # sin(x)/x
    pylab.plot(k,ko)
    #pylab.plot(x,y,'co') # same function with cyan dots
    #pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
    pylab.show() # show the plot
    
def knnExec(X,y,Act):
    clf=KNeighborsClassifier(n_neighbors=4)
    X_train=[[2,5,5,2000,2],[20,30,50,2500,80],[25,30,55,2550,60],[2,5,10,2050,2]]
    y_train=[0,1,1,0]
    X_test=[[20,30,50,2000,50]]
    y_test=[1]
    #X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)    
    print '==========using knn classifier==========' 
    clf.fit(X_train,y_train)
    #print clf.score(X_test, y_test)
    y_pred=clf.predict(X_test)
    print 'y_pred',y_pred
#    if Act!='dummy':
#        #perf_measure(y_test,y_pred,Act+', Knn')    
#        y_preAr=precision_score(y_test, y_pred, average=None)
#        precision, recall, fscore, support = score(y_test, y_pred)
#    #print clf.predict_proba(X_test)
#        print 'The roc auc score is: ',roc_auc_score(y_test,y_pred)
#        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
#        print('precision: {}'.format(precision))
#        print('recall: {}'.format(recall))
#        print('fscore: {}'.format(fscore))
#        print('support: {}'.format(support))    

def entropy2(labels):
    n_labels = len(labels)
    print n_labels
    if n_labels <= 1:
        return 0

    counts = np.bincount(labels)
    print counts
    probs = counts / n_labels
    print probs
    n_classes = np.count_nonzero(probs)
    print n_classes
    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute standard entropy.
    for i in probs:
        ent -= i * math.log(i, base=n_classes)
    print ent
   
    return ent
     
plot1()   

#g = graph.graphxy(width=8)
#g.plot(graph.data.function("y(x)=sin(x)/x", min=-15, max=15))
 
#knnExec([[2,5,5,2000,2],[20,30,50,2000,2],[25,30,55,2550,60],[2,5,10,2050,2]],[0,1,1,0],'Color')
##dist = n([2,5,5,2000,2]-[20,30,50,2000,50])
##print dist
#print np.sqrt(np.sum((np.array([2,5,10,2050,2])-np.array([20,30,50,2000,50]))**2))