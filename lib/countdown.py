# your code goes here!
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