# Convert celcius to fahrenheit

import sys

print(sys.argv)

c = float(sys.argv[1])

f = c * 9 / 5 + 32

print(f"{c} celcius is {f} fahrenheit.")