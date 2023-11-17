
import sys

# (index)     0             1       2         3          4
# python count_alice_b.py Alice Alice.txt parrot.txt tyger.txt

search_word = sys.argv[1]
files = sys.argv[2:]

for file in files :
    with open(file) as f :
        count = 0
        lines = f.read().splitlines()
        for line in lines :
            if search_word in line : 
                count += 1
    print(f"In {file}, found the word '{search_word}' in {count} lines.")