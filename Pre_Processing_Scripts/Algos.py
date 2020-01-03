# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:28:20 2016

@author: malz
"""

# program to merge two csv file into one
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
#from __future__ import division
graphs_status=False
#from sklearn.neural_network import MLPClassifier

#from ggplot import *
def EERCalc(X,y_test, y_pred,clf):
    #print y_test,y_pred
    #print X,clf
    diff_arr = []
    FPR=[]
    FNR=[]
    for i in range(1,101):
        threshold = float(i)/float(100)
        #print threshold
#threshold=0.999
        y_predNew=[]
        for i in range(0,len(X)):
            if(X[i][0]>threshold):
                y_predNew.append(0)
            else:
                y_predNew.append(1)
        FP, FN, diff=perf_measure_new(y_test,y_predNew,"color")
        FPR.append(FP)
        FNR.append(FN)
        diff_arr.append(diff)
    a=FPR[diff_arr.index(min(diff_arr))]
    b=FNR[diff_arr.index(min(diff_arr))]
    
    with open("/media/malz/01D0E9654C2905F0/BrainWaveProj/ActivityRegressionTest/"+clf+".csv", 'w') as w:
        dwri=csv.writer(w)
        #print FPR.typeof()

        for i in range(0,100):
            #x= str(FPR[i])+","+ str(FNR[i]
                                
            dwri.writerow([FPR[i],FNR[i]])
            #dwri.writerow(FNR[i])
    print "EER:"
    return (float(a)+float(b))/float(2)
    
    
                #print y_predNew, y_pred
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
    #return(FP, FN)        
def perf_measure(y_test, y_score,Act):   
    
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_score)
    
    roc_auc = auc(false_positive_rate, true_positive_rate)
    if Act!='dummy':
        if graphs_status==True:
            plt.title('Receiver Operating Characteristic')
            plt.plot(false_positive_rate, true_positive_rate, 'b',label=Act+'AUC = %0.2f'% roc_auc)
            plt.legend(loc='best')
            plt.plot([0,1],[0,1],'r--',color='green')
            plt.xlim([-0.1,1.5])
            plt.ylim([-0.1,1.2])
            plt.ylabel('True Positive Rate')
            plt.xlabel('False Positive Rate')
            plt.show()
    
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
    print 'TP=',TP,'TN=' ,TN,'FN=' , FN, 'FP=', FP
    
    return(TP, FP, TN, FN)

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
  
def knnExec(X,y,Act):
    clf=KNeighborsClassifier(n_neighbors=19)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)    
    print '==========using knn classifier==========' 
    clf.fit(X_train,y_train)
    #clf.score(X_test, y_test)
    print clf.score(X_test, y_test)
    y_pred=clf.predict(X_test)
    #EERCalc(clf.predict_proba(X_test), y_test, y_pred,"knn")
    #print clf.predict_proba(X_test)
    #print y_train
    #print y_pred
    if Act!='dummy':
        perf_measure(y_test,y_pred,Act+', Knn')    
        y_preAr=precision_score(y_test, y_pred, average=None)
        #print y_preAr
        precision, recall, fscore, support = score(y_test, y_pred)
    #print clf.predict_proba(X_test)
        print 'The roc auc score is: ',roc_auc_score(y_test,y_pred)
        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"knn")
    
    
def svmExev(X,y,Act):
    print '==========using svm classifier=========='
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)
    #print X_train.shape, y_train.shape
    #print X_test.shape, y_test.shape     
    clf =svm.SVC(probability=True)
    clf.fit(X_train,y_train)
    print clf.score(X_test, y_test)
    y_pred= clf.predict(X_test)
    #print clf.predict_proba(X_test)
    #EERCalc(clf.predict_proba(X_test), y_test, y_pred,"svm")
    if Act!='dummy':
        perf_measure(list(y_test),list(y_pred),Act+', Svm')     
        y_preAr=precision_score(y_test, y_pred, average=None)
        precision, recall, fscore, support = score(y_test, y_pred)
        #print clf.predict_proba(X_test)
        print 'The roc auc score is: ',roc_auc_score(y_test,y_pred)
        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"svm")
     
def naiveBayes(X,y,Act):
    print '==========using naive Bayes=========='
    X1=np.array(X).astype(np.float)
    y1=np.array(y).astype(np.float)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X1, y1, test_size=0.4, random_state=0)
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    print clf.score(X_test,y_test)
    #print y_pred
    y_pred=clf.predict(X_test)
    #print clf.predict_proba(X_test)
    #EERCalc(clf.predict_proba(X_test), y_test, y_pred,"NB")
    if Act!='dummy':
        perf_measure(y_test,y_pred,Act+', Naive Bayes')
        y_preAr=precision_score(y_test, y_pred, average=None)
        precision, recall, fscore, support = score(y_test, y_pred)
        #Sprint clf.predict_proba(X_test)
        print 'The roc auc score is: ',roc_auc_score(y_test,y_pred)
        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"NB")
    
def randomForest(X,y,Act):
    print '==========Using Random forest classifier=========='
    X1=np.array(X).astype(np.float)
    y1=np.array(y).astype(np.float)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X1, y1, test_size=0.4, random_state=0)
    clf=rfc(n_estimators=120)
    clf.fit(X_train,y_train)
    print clf.score(X_test,y_test)
    y_pred=clf.predict(X_test)
    y_preAr=precision_score(y_test, y_pred, average=None)
    #EERCalc(clf.predict_proba(X_test), y_test, y_pred,"RF")
    #print clf.predict_proba(X_test)
    if Act!='dummy':
        perf_measure(y_test,y_pred,Act+', Random Forest')
        y_preAr=precision_score(y_test, y_pred, average=None)          
        precision, recall, fscore, support = score(y_test, y_pred)
        #Sprint clf.predict_proba(X_test)
        x=roc_auc_score(y_test,y_pred)
        print 'The roc auc score is: ',x
        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
    return EERCalc(clf.predict_proba(X_test), y_test, y_pred,"RF")
    
def randomForest_new(trainData, trainTarget, testData, testTarget,Act):
    print '==========Using Random forest classifier=========='
    
    trainX=np.array(trainData).astype(np.float)
    trainy=np.array(trainTarget).astype(np.float)
    testX=np.array(testData).astype(np.float)
    testy=np.array(testTarget).astype(np.float)
    
    
    clf=rfc(n_estimators=120)
    clf.fit(trainX,trainy)
    print clf.score(testX,testy)
    y_pred=clf.predict(testX)
    y_preAr=precision_score(testy, y_pred, average=None)

    if Act!='dummy':
        perf_measure(testy,y_pred,Act+', Random Forest')
        y_preAr=precision_score(testy, y_pred, average=None)  
               
        precision, recall, fscore, support = score(testy, y_pred)
        #Sprint clf.predict_proba(X_test)
        x=roc_auc_score(testy,y_pred)
        print 'The roc auc score is: ',x
        print 'The Avg precision score is:',average_precision_score(testy,y_pred)
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
        return x
    
def decisionTree(X,y,Act):
    print '==========Using Decision Tree=========='
    X1=np.array(X).astype(np.float)
    y1=np.array(y).astype(np.float)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X1, y1, test_size=0.4, random_state=0)
    clf=tree.DecisionTreeClassifier()
    clf.fit(X_train,y_train)
    print clf.score(X_test,y_test)
    y_pred=clf.predict(X_test)
    if Act!='dummy':
        perf_measure(y_test,y_pred,Act+', Decision Tree')
        y_preAr=precision_score(y_test, y_pred, average="binary") 
        print 'The roc auc score is: ',roc_auc_score(y_test,y_pred)  
        print 'The Avg precision score is:',average_precision_score(y_test,y_pred)
        #print y_preAr
    #    accuracy=accuracy_score(y_test,y_pred)
    #    print accuracy
        precision, recall, fscore, support = score(y_test, y_pred)
        #print clf.predict_proba(X_test)
        
        print('precision: {}'.format(precision))
        print('recall: {}'.format(recall))
        print('fscore: {}'.format(fscore))
        print('support: {}'.format(support))
    

    
    
def neural(X,y):
    print '==========Using Neuralnetworks=========='
    X1=np.array(X).astype(np.float)
    y1=np.array(y).astype(np.float)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X1, y1, test_size=0.4, random_state=0)
    clf = MLPClassifier()
    clf.fit(X_train,y_train)
    print clf.score(X_test,y_test)
    #y_pred=clf.predict(X_test)
    #y_preAr=precision_score(y_test, y_pred, average="binary")
    #precision, recall, fscore, support = score(y_test, y_pred)
    #print clf.predict_proba(X_test)
    
    #print('precision: {}'.format(precision))
    #print('recall: {}'.format(recall))
    #print('fscore: {}'.format(fscore))
    #print('support: {}'.format(support))

    
def svmPlot(X,y):
    C = 1.0  # SVM regularization parameter
    h = .02
    svc = svm.SVC(kernel='linear', C=C).fit(X, y)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
    lin_svc = svm.LinearSVC(C=C).fit(X, y)
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
    titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']


    for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

    # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])

    plt.show()


