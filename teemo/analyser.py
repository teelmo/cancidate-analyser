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
# person_db.remove({})

i = 0
with open(file, 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  for row in reader:
    i = i + 1
    body = "{'url':'%s'}" % row[1]
    if person_db.find({'url':row[1]}).count() == 0:
      try:
        conn = httplib.HTTPSConnection('westeurope.api.cognitive.microsoft.com')
        conn.request(method='POST', url='/vision/v1.0/describe', body=body, headers=headers)
        response = conn.getresponse()
        data = response.read()
        output = {
          'id':row[0],
          'url':row[1],
          'text':json.loads(data)['description']['captions'][0]['text'],
          'response':json.loads(data),
        }
        person_db.insert(output)
        conn.close()
      except Exception as e:
        print('[Errno {0}] {1}'.format(e.errno, e.strerror))
    print i
