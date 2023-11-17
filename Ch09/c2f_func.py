
def c2f(c):
    return c * 9 / 5 + 32

for c in [100, 0, 37, -40]:
    f = c2f(c)
    print(f"{c}c is {f}f")
