#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

# Initialize MongoDB
import urllib, json
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection.candidate_analyzer
person_db = db.person

response = urllib.urlopen("../data/streamStarts.json")
streams = json.loads(response.read())

for stream in streams:
    stream["id"]
    print person_db.find({'url': "http://images.cdn.yle.fi/image/upload/13-"+stream["id"]})
    break
