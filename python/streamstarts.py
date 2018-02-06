#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import httplib, urllib, base64
import json

url = 'http://somedata.api.yle.fi/v2/programs/streamstarts/total.json?yle_id=1-2694514&app_id=e2630534&app_key=da5935d56e4c3e1bc8d330cff2bfa672'
response = urllib.urlopen(url)
data = json.loads(response.read())
print data