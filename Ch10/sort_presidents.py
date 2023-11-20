
with open("./Ch10/presidents.txt") as f:
    lines = f.read().splitlines()

presidents = []
for line in lines:
    _, lname, fname, _, _, _, state, *_ = line.split(":")
    presidents.append( (lname, fname, state) )

presidents.sort(key = lambda p: (p[1], p[0]))
for p in presidents:
    lname, fname, state = p
    print(f"{fname:25s} {lname:25s} {state}")