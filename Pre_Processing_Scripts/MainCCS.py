# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:58:59 2016

@author: malz
Function: This is the main program to run for Neurosky data of 
"""
import numpy as np
import csv
import random
import os.path as path
import grouper
import brainlib
import sys

vector_resolution=3;
write_path = '/home/malz/workspace_mars/Java_Practice/src'
read_path = '/home/malz/workspace_mars/Java_Practice/src'
#list_of_Users=['User1/Testing','User1/Training','User2/Testing','User2/Training','User3/Testing','User3/Training']
list_of_Users=['User5/Training']
list_of_sessions=['Activity_Two']
list_of_files=['Neurosky/Neurosky.csv.csv']
list_of_filesO=['Neurosky/Neurosky_Fea.csv']

def parse_raw_values (reading):
  "make list of power spectra for all raw_values in a list"
  # first and last values have { and } attached.
  vals = reading['raw_values'].split(',')  
  vals[0] = vals[0][1:]
  vals[len(vals)-1] = vals[len(vals)-1][:-1]
 # print np.array(vals).astype(np.float)
 # print 'done'
  return np.array(vals).astype(np.float)

def spectra (readings):
  "Parse + calculate the power spectrum for every reading in a list"
  #print [brainlib.pSpectrum(parse_raw_values(r)) for r in readings]
  return [brainlib.pSpectrum(parse_raw_values(r)) for r in readings]

def data_path_generator(fol,user_path,session,file1): 
    temp=str(fol)
    return path.join(user_path, temp, str(session),str(file1))
def readAllReadings(reader1):
    print 'in second'
    for row in reader1:
        #print row
        yield row

def make_feature_vector (readings): # A function we apply to each group of power spectra
  '''
  Create 100, log10-spaced bins for each power spectrum.
  For more on how this particular implementation works, see:
  http://coolworld.me/pre-processing-EEG-consumer-devices/
  '''
  #for read in readings:
   #  print read
  #print('Done')
  #print readings
  spect=spectra(readings)
  print len(spect[1])
  bin=brainlib.binnedPowerSpectra(spect, 100)
  print len(bin[2])
  #print bin
  Y=brainlib.avgPowerSpectrum( bin, np.log10)
  print type(Y)
  
  return Y


def readings(filePath):
       print 'In readAllreadings'
       #print filePath
       with open(filePath, 'r') as file:
           reader = csv.DictReader(file)
           #print reader
          # for row in reader:
               # print row
                #yield row
           return [r for r in readAllReadings(reader)]


def featureStep1(read1):
    print 'I am here'
    groups = grouper.grouper(3, read1)
    for g in groups:
        readings1 = filter(None, g)
        #print len(g)
        print '============================================================'
    #print readings
        #print len(readings1)
    # throw out readings with fewer signals than our desired resolution
        if len(readings1) == vector_resolution:
            yield make_feature_vector(readings1)
def FeatureStore(pathS,arrayOfGen):
    list1=list(arrayOfGen)
    #print list1
    outFile=open(pathS,'wb')
    wr=csv.writer(outFile)
    wr.writerows(list1)
for i in range (0,1):
    for k in range(0,1):
        for j in range(0,1):
            print list_of_Users[i]+list_of_sessions[k]
            print data_path_generator(list_of_Users[i],read_path,list_of_sessions[k],list_of_files[j]);
            read1 = readings(data_path_generator(list_of_Users[i],read_path,list_of_sessions[k],list_of_files[j]))
            #print read1
            #print '==============================================================================================='            
            arrayOfGen=featureStep1(read1)
            FeatureStore(data_path_generator(list_of_Users[i],read_path,list_of_sessions[k],list_of_filesO[j]), arrayOfGen)
            #print arrayOfGen
#print read1
print 'Hello'
