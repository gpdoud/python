ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for c in ctemps :
    print(f"{c}c is {c * 9 / 5 + 32}f")

clean_fruits = [f.strip().lower() for f in fruits]
for cf in clean_fruits :
    print(f"{cf}", end=' ')