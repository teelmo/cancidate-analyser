#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import urllib, json
import glob

images = []

for filename in glob.glob('data/*.json'):
  response = urllib.urlopen(filename)
  data = json.loads(response.read())
  for person in data:
    if 'http://' in person['14']: 
      print person['1'] + ',' + person['14']
      images.append(person['14'])

# print images