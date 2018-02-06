#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import httplib, urllib, base64
import json
import csv

results = []
with open('../data/areena_ids.txt') as inputfile:
    for row in csv.reader(inputfile):
        url = 'http://somedata.api.yle.fi/v2/programs/streamstarts/total.json?yle_id=%s&app_id=e2630534&app_key=da5935d56e4c3e1bc8d330cff2bfa672' % row[0]
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        output = {
                  "streamViews": data["data"][0]["streamStarts"],
                  "id": row[0]
        }
        results.append(output)

print json.dumps(results)
        
