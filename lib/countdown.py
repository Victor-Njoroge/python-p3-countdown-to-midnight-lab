# your code goes here!
import time
def CountDown():
    seconds=int(input("Enter the seconds Here: "))
    i=seconds
    while i >= 0:
        if i >0 :
            print(f"{i} SECOND(S) !")
        else:
            print("HAPPY NEW YEAR")
        i-=1
CountDown()

def CountDownPause() :
    seconds=int(input("Enter Seconds: "))
    i = seconds
    while i >=0 :
        print(i)
        time.sleep(1)
        i-=1
CountDownPause()