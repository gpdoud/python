
import sys

files = sys.argv[1:]
divider = "**********************************************"

for file in files :
    with open(file) as f :
        tuples = enumerate(f.read().splitlines(), 1) # (1, "abc")
        for t in tuples :
            nbr, line = t # unpack the tuple
            print(f"{nbr:02d} {line}")
        print(divider)