# Program to play Youtube video (Bulleya song) after every 200 seconds i.e.(3min 26sec )
import webbrowser
import time

count = 0
print("This program started on "+time.ctime())
while count<3:
    time.sleep(200)
    webbrowser.open("https://www.youtube.com/watch?v=hXh35CtnSyU")
    count += 1
