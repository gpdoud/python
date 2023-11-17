from temp_conv import c2f

while True:
    c = int(input("Enter celsius: "))
    f = c2f(c)
    print(f"{c}c is {c2f(c)}f")

    ans = input("Quit? (q): ").lower()
    if ans == "q":
        break

print("Done ...")