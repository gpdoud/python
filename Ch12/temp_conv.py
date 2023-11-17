"""
Temp conversion module

c2f(c) Converts celsius to fahrenheit
f2c(f) Converts fahrenheit to celsius
"""
def c2f(c):
    """
    Converts celsius to fahrenheit

    :parm c is temp in celsius
    """
    return c * 9 / 5 + 32


def f2c(f):
    """
    Converts fahrenheit to celsius

    :parm f is temp in fahrenheit
    """
    return (f - 31) * (5.0 / 9)


if __name__ == "__main__":

    for c in [100, 37, 0, -40]:
        print(f"{c}c is {c2f(c)}f")
    
    for f in [212, 98.6, 32, -40]:
        print(f"{f}f is {f2c(f):.01f}")