# Guessing game
import sys
# pass the maximum number on the command line or 
# prompt the user to enter it
parms = sys.argv[1:]
if len(parms) == 0:
    max = int(input("Enter max integer: "))
else:
    max = int(parms[0])

min = 1

while True :
    guess = (min + max) // 2
    ans = input(f"Is your number {guess}? (L,H,Y): ").lower()
    if ans == "y" :
        print("Got it!")
        break
    elif ans == "l" :
        print("Too low. ")
        min = guess
    elif ans == "h" :
        print("Too high. ")
        max = guess
    else :
        print("Invalid response! Use only (L, H, Y)")
