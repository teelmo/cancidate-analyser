#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import json
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection.candidate_analyzer

data_db = db.data

output = {}
for element in data_db.find({}).sort('streams',-1).limit(100):
  for tag in element['data']['response']['tags']:
    if tag['name'] in output and tag['confidence'] > 0.7:
      output[tag['name']] = output[tag['name']] + 1
    elif tag['confidence'] > 0.7:
      output[tag['name']] = 1

i = 0
print '\nMost viewed videos:'
for key, value in sorted(output.iteritems(), key=lambda (k,v): (v,k), reverse=True):
  print '%s: %s' % (key, value)
  i = i + 1
  if i == 20:
    break

output = {}
for element in data_db.find({}).sort('streams',1).limit(100):
  for tag in element['data']['response']['tags']:
    if tag['name'] in output and tag['confidence'] > 0.7:
      output[tag['name']] = output[tag['name']] + 1
    elif tag['confidence'] > 0.7:
      output[tag['name']] = 1

i = 0
print '\nLeast viewed videos:'
for key, value in sorted(output.iteritems(), key=lambda (k,v): (v,k), reverse=True):
  print '%s: %s' % (key, value)
  i = i + 1
  if i == 20:
    break

# output = {}
# for element in data_db.find({}).sort('streams',1).limit(100):
#   print element['data']['response']['captions'][0]['text']
