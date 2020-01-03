# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:28:20 2016

@author: malz
"""

# program to merge two csv file into one
import csv as csv
import numpy as np
from dateutil.parser import parse
import csv
import os.path as path
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from featurevectorgenerator import feature_vector_generator
import matplotlib.pyplot as plt
from numpy import array
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd
#from plot_roc import plotting
#from ggplot import *

path0='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/blink.csv'
path1='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/color.csv'
path2='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/math.csv'
path3='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/music.csv'
path4='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/relax.csv'
path5='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/think.csv'
path6='/media/malz/01D0E9654C2905F0/BrainWaveProj/Activity_Per_User_Data/UserActivity/video.csv'


def dataset_path (subjectnum):
  return path.join('/media/malz/01D0E9654C2905F0/TUMGAID/synchronized-brainwave-starter-pack/feature_vec', str(subjectnum) + '.csv')

def readings_in_range (csvdict):
  '''A generator that returns all readings in a CSV dict
  not including t0, including t1. Ignores readings with
  a signal quality > sq. You can only use this generator
  if the file is open for reading.'''
  inrange=True
    #print t0
  for row in csvdict:
    if inrange:
      yield row
  

def readings (subject):
  with open(dataset_path(subject), 'r') as file:
    #the below line of code uses csv.DictReader to read the contents of file in objectformat
    reader = csv.DictReader(file)

    #result = sorted(reader, key=lambda d: parse(d['main']))
    #print len(result)
    return [r for r in readings_in_range(reader)]


def parse_main_values (reading):
  # first and last values have { and } attached.
  vals = reading['main'].split(',')  
  vals[0] = vals[0][1:]
  vals[len(vals)-1] = vals[len(vals)-1][:-1]
 # print np.array(vals).astype(np.float)
 # print 'done'
  return np.array(vals).astype(np.float)

def yeild_vector(sub):
    reading=readings(sub)
    for r in reading:
        yield parse_main_values(r)
        
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
  
def knnExec(X,y,f):
    knn=KNeighborsClassifier(n_neighbors=5)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1, random_state=0)
    #print X_train.shape, y_train.shape
    #print X_test.shape, y_test.shape    
    print 'using knn classifier' 
    knn.fit(X_train,y_train)
    print knn.score(X_test, y_test)
    #print knn.predict(np.array(f))
    #print knn.predict_prob(X_test,y_test)
def svmExev(X,y,f):
    print 'using svm classifier'
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1, random_state=0)
    #print X_train.shape, y_train.shape
    #print X_test.shape, y_test.shape     
    clf =svm.SVC()
    clf.fit(X_train,y_train)
    print clf.score(X_test, y_test)
    #print clf.predict(f)

def naiveBayes(X,y,f):
    print 'using naive Bayes'
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.1, random_state=0)
    gnb = GaussianNB()
    y_pred=gnb.fit(X_train, y_train).predict(f)
    print gnb.score(X_test,y_test)
    #print y_pred

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


    
blink=yeild_vector('blink') # 0
#for r in blink:
#    print r
color=yeild_vector('color') #1
#for r in blink:
#    print r
math=yeild_vector('math') # 2
#for r in blink:
#    print r
music=yeild_vector('music')#3
#for r in blink:
#    print r
relax=yeild_vector('relax')#4
#for r in blink:
#    print r
think=yeild_vector('think')#4
#for r in blink:
#    print r
video=yeild_vector('video')#5
#for r in relax:
#    print r
X,y=vectorsAndLabels([color,blink,math])
#X,y=vectorsAndLabels([blink, math,color,music,relax,think,video])
#print len(X)
#print len(y)
#print crossValidate(X,y)
X1=array(X)
y1=array(y)
#-print type(X)
#-print type(X1)
#print y
t0 = parse('2015-05-09 22:45:55.323+00')

t1 = parse('2015-05-09 22:47:17.218+00')

test=feature_vector_generator(281,t0,t1)
M,k=vectorsAndLabels([test])
#plotting(X1,y1)
#print M
#print np.array(k).shape

knnExec(array(X),array(y),array(M))
svmExev(array(X),array(y),array(M))
naiveBayes(array(X),array(y), array(M))
#svmPlot(X1,y)