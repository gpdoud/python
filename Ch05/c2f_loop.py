# Convert celcius to fahrenheit

while True :

    c = float(input("Enter celcius value: "))

    f = c * 9 / 5 + 32

    print(f"{c} celcius is {f} fahrenheit.")

    ans = input("'Y' to quit?: ")
    if ans.lower() == "y" :
        break