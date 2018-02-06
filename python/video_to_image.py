videos = ['video1.mp4','video2.mp4','video3.mp4','video4.mp4','video5.mp4','video6.mp4','video7.mp4','video8.mp4','video9.mp4']
import os

for video in videos:
  os.system(' ffmpeg -ss 15 -i ../vid/'+ video + ' -t 1 -s 480x300 -f image2 ../img/' + video + '.jpg ')
 