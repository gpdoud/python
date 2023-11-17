# Guessing game

min = 1
max = 250000
#max += 1

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
