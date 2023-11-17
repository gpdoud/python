
search_word = "Alice"

count = 0

with open("./Ch07/alice.txt") as f :

    lines = f.read().splitlines()

    for line in lines :
        if search_word in line : 

            count += 1


print(f"Count is {count}")