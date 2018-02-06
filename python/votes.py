#!/usr/bin/python
# -*- coding: UTF8 -*-
# @See http://www.python.org/dev/peps/pep-0263/

import httplib, urllib, base64
import json

urls = ['http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_1.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_2.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_3.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_4.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_5.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_6.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_7.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_8.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_9.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_10.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_11.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_12.json','http://static.cdn.yle.fi/vaalit/ev2015/versions/70/candidates_13.json']

for url in urls:
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  print data
  break



