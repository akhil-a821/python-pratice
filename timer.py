import time
timer=int(input("enter the time in seconds:"))
for x in range(timer,0,-1):
    seconds=int(x%60)
    minutes=int((x/60)%60)
    hours=int((x/3600)%24)
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")
    time.sleep(1)
print("Time's up!")