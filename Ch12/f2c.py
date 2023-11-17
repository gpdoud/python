from temp_conv import f2c
from sys import argv

f = int(argv[1])

print(f"{f}f is {f2c(f):.01f}c")

