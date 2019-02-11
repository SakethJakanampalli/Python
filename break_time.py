import webbrowser
import time

var = 0
while var < 3:
    var+=1
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=Ct6BUPvE2sM")
    print ('The count is:', var)
