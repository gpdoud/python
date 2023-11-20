# Convert celcius to fahrenheit

while True :

    cStr = input("Enter celcius value: ")

    if not cStr.isnumeric():
        print(f"ERROR!: a{cStr} is an invalid number")
        continue

    c = float(cStr)

    f = c * 9 / 5 + 32

    print(f"{c} celcius is {f} fahrenheit.")

    ans = input("'Y' to quit?: ")
    if ans.lower() == "y" :
        break