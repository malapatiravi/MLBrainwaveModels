import csv
import os.path as path
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import operator


# Utilities to query date ranges from the indra dataset
#
# EXAMPLE USAGE
#
# subject_num = 11
# t0 = parse('2015-05-09 23:28:46+00')
# t1 = parse('2015-05-09 23:29:46+00')
# readings(subject_num, t0, t1)

# This is the time field we use for querying.
# You can change this to get, for example, 'createdAt'
# indra_time is the synchronized timestamp field.
# So, don't change this unless you know what you're doing.
time_field = 'indra_time'

class DatasetQueryError (Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def dataset_path (subjectnum):
  return path.join('/media/malz/01D0E9654C2905F0/TUMGAID/synchronized-brainwave-starter-pack/dataset', 'neurosky-data', str(subjectnum) + '.csv')

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
      print row
      yield row
    if inrange and time >= t1:
      break

def readings (subject, t0, t1, sq, sub_path):
  '''Returns all of subject's readings between t0 and t1,
  not including t0, but including t1.
  sq defines minimum signal quality - 0, by default'''
  if t1 < t0:
    raise DatasetQueryError("First time must come before second time.")
    #the below line of code reads the file in the path specified in dataset path
    #returned by dataset_path(subject)
  with open(sub_path, 'r') as file:
    #the below line of code uses csv.DictReader to read the contents of file in objectformat
    reader = csv.DictReader(file)

    result = sorted(reader, key=lambda d: parse(d[time_field]))
    #print len(result)
    return [r for r in readings_in_range(result, t0, t1, sq)]
