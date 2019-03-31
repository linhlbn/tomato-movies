import webbrowser
import time

count = 0
print ("My break time is coming: "+time.ctime())
while (count < 7):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=A8zI28le5L4")
    count = count + 1
