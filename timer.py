import time
import winsound
while True:
 timer=int(input("enter the time in seconds:"))
 for x in range(timer,0,-1):
    seconds=int(x%60)
    minutes=int((x/60)%60)
    hours=int((x/3600)%24)
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")
    time.sleep(1)
    winsound.Beep(1000,100)
 print("Time's up!")
 for i in range(5):
     winsound.Beep(1200,500)
 a=input("Do you want to set another timer? (yes/no): ")
 if a.lower()!="yes":
        break
 else:
        continue