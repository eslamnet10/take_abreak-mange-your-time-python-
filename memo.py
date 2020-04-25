import time 
import webbrowser 
breaks = 3 
counter = 0
print("this program started on"+time.ctime()) 
while(counter<breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=EY9OtHQLKDE")
    counter=counter+1 

