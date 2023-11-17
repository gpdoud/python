
import sys

files = sys.argv[1:]
divider = "**********************************************"

for file in files :
    with open(file) as f :
        tuples = enumerate(f.read().splitlines(), 1)
        for t in tuples :
            nbr, line = t
            print(f"{nbr:02d} {line}")
        print(divider)