#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import urllib, json
import glob

output = []

for filename in glob.glob('../data/orig/*.json'):
  response = urllib.urlopen(filename)
  data = json.loads(response.read())
  for person in data:
    if 'http://' in person['14']: 
      output.append(person)

print json.dumps(output)