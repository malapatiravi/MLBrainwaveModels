# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:43:45 2016

@author: malz
"""

import csv
import os.path as path
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import operator

time_field = 'indra_time'

class Error (Exception):
    ''' This function defines error'''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def path_evaluation (subjectnum):
  return path.join('/media/malz/01D0E9654C2905F0/BrainWaveProj/indra_mids_5_15', 
  'neurosky-data', str(subjectnum) + '.csv')

def synced_time (row):
  '''Gets indra time.
  You can change the field to get, for example,
  'readingTime' or 'createdAt'.'''
  return parse(row[time_field])
  
def signal_quality (row):
  '''Gets the signal quality of a reading.'''
  return eval(row['signal_quality'])
  
def readings_in_range (csvdict, t0, t1, sq):
  '''A generator that returns all readings in a CSV dict
  not including t0, including t1. Ignores readings with
  a signal quality > sq. You can only use this generator
  if the file is open for reading.'''
  #print t1, t0  
  inrange = False
  for row in csvdict:
    time = synced_time(row)
    #print t0
    if not inrange and time >= t0:
      inrange = True
    if inrange and signal_quality(row) <= sq:
        yield row        
    if inrange and time >= t1:
      break

def readings (subject, t0, t1, sq):
  '''Returns all of subject's readings between t0 and t1,
  not including t0, but including t1.
  sq defines minimum signal quality - 0, by default'''
  if t1 < t0:
    raise Error("First time must come before second time.")
    #the below line of code reads the file in the path specified in dataset path
    #returned by dataset_path(subject)
  with open(path_evaluation(subject), 'r') as file:
    #the below line of code uses csv.DictReader to read the contents of file in objectformat
    reader = csv.DictReader(file)
    result = sorted(reader, key=lambda d: parse(d[time_field]))
    return [r for r in readings_in_range(result, t0, t1, sq)]

