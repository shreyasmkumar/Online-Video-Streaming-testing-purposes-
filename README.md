# Online-Video-Streaming-for-testing-purposes

This is our Dash server for adaptive video streaming. We plan to implement this further to accommodate Virtual Reality video Streaming.  This document is a brief on how you can install our server and run it and also, it contains instructions you on how to make your changes to our server.

However, before that, please have the following tools installed for smooth running.

# Tools
-ffmpeg:         https://www.ffmpeg.org/download.html

-mahimahi:       http://mahimahi.mit.edu/#getting

-selenium:       https://pypi.python.org/packages/source/s/selenium/selenium-2.39.0.tar.gz

Firstly, here are some instructions to install our server and how to run it.

#   Steps to run server                             				                            
1. Open our folder and run the setup file in a terminal.           	     
2. And next, execute this command to run the server.                  	
3. In another terminal run the mahimahi network shell of 20 ms.    		   
and run a browser on it.                                  					    
4. And in the browser run the webpage                            			   
(Also have disabled Cache in the browser
Ctrl+Shift+I -> Network -> check disable cache)

# Corresponding Command Prompt lines
1.$ python2 setup.py

2.$ python2 run_server.py RL 4000 1
(RL implies protocol, and you can replace with BOLA or 
Others. 4000 implies run time of the server in milliseconds
And 1 implies the ID of the log file that will be saved)

3.$ mm-delay 20
$ chromium-browser
4. 100.64.0.1/test.html


Following these steps opens a webpage. The webpage will switch our pre-installed video after ten seconds with another one of our videos.
To make changes to the way the videos are loaded, you can make changes to test.html in /var/www/html/ directory, and you can see the changes when you run the server.
However, if you want to replace our videos with your own, please take a look at the following instructions

# Working with your own video file
1.    Know where your video file is and put it in a folder where you want the split m4s files of your video.
2.    Execute the following ffmpeg command on a terminal: 
ffmpeg -i <video file name> -codec copy -f dash -seg_duration 5 -use_template 1 -use_timeline 1  -init_seg_name '$RepresentationID$-init.m4s' -media_seg_name '$RepresentationID$-$Number$.m4s' Manifest.mpd  
3.    Now copy all these files to the directory ‘/var/www/html’ (you can use our setup file for your convenience) and change test.html accordingly.
4.    Follow the same steps as above to run our server.

You can change how many seconds you want your split video/audio files to be using the ‘-seg_duration’ option in step 2 (it can be in a fraction too), for example in the above command it has been set to 5 seconds. An inventory of the split video files will be stored in Manifest.mpd.


# Issues we faced

Initially, we could not figure out where the video segments needed to be placed, after much research and deliberation we found the root folder where the apache server streams from where the video is streamed. 
And once we figured out where to put the video segments, we were not able to figure out the right codec software to split our video into sub-second chunks. And we came across ffmpeg and how this option can be used to split the videos into chunks smaller than seconds.
These were few of the issues we overcame.
