#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

# Initialize MongoDB
import urllib, json
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection.candidate_analyzer
person_db = db.tag
data_db = db.data
data_db.remove({})

response = urllib.urlopen("../data/streamStarts.json")
streams = json.loads(response.read())

response = urllib.urlopen("../data/votes.json")
votes = json.loads(response.read())

i = 0
for stream in streams:
  i = i + 1
  # person_db.find({'url': 'http://images.cdn.yle.fi/image/upload/13-' + stream['id'] + '.jpg'})[0]
  person = person_db.find({'url': 'http://images.cdn.yle.fi/image/upload/13-' + stream['id'] + '.jpg'})[0]
  del person[u'_id']
  first_name = person['data']['3']
  last_name = person['data']['2']
  caid = person['data']['13']
  name = last_name.strip() + ', ' + first_name.strip()
  # name = 'Jansson, Cecilia'
  vote_data = {}
  for vote in votes:
    for candidate in vote['candidates']:
      if name in candidate['name']:
        vode_data = candidate

  output = {
    'streams':stream['streamViews'],
    'data':person,
    'vode_data':vode_data
  }
  data_db.insert(output)
  # if i > 3:
    # break;
