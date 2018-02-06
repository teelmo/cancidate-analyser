#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

########### Python 2.7 #############
import httplib, urllib, base64
import json
import sys
import csv

try:
  file = sys.argv[1]
  key = sys.argv[2]
except:
  print 'Provide file and key!!'
  exit()

headers = {
  # Request headers
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Key': '%s' % key
}
params = urllib.urlencode({
  # Request parameters
  'visualFeatures': 'Categories',
  'language': 'en',
})

# Initialize MongoDB
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection.candidate_analyzer
person_db = db.person

# Clear databases.
person_db.remove({})

i = 0
response = urllib.urlopen(file)
data = json.loads(response.read())
# reader = csv.reader(csvfile, delimiter=',', quotechar='"')
for person in data:
  i = i + 1
  body = "{'url':'%s'}" % person['14']
  if person_db.find({'url':person['14']}).count() == 0:
    conn = httplib.HTTPSConnection('westeurope.api.cognitive.microsoft.com')
    conn.request(method='POST', url='/vision/v1.0/describe', body=body, headers=headers)
    response = conn.getresponse()
    response_json = json.loads(response.read())
    output = {
      'id':person['1'],
      'url':person['14'],
      'text':response_json['description']['captions'][0]['text'],
      'response':response_json,
      'data':person
    }
    person_db.insert(output)
    conn.close()
  print i
