videos = ['https://areena.yle.fi/1-4024908','https://areena.yle.fi/1-4051829','https://areena.yle.fi/1-4009994','https://areena.yle.fi/1-4053501','https://areena.yle.fi/1-4071008','https://areena.yle.fi/1-4031055','https://areena.yle.fi/1-4017509','https://areena.yle.fi/1-4031031','https://areena.yle.fi/1-4042257']

import os

for video in videos:
  print video
  os.system('yle-dl ' + video)