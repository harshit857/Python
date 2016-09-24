# Program to play Youtube video (Bulleya song) after every 200 seconds i.e.(3min 26sec )
#To run this file save it with ->  "filename".py  (don't include "")
#Remember to have python installed on the system

import webbrowser
import time

count = 0
print("This program started on "+time.ctime())
while count<3:
    time.sleep(200)
    webbrowser.open("https://www.youtube.com/watch?v=hXh35CtnSyU")
    count += 1
