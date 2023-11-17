
fruit1 = set()
fruit2 = set()

with open("./Ch08/fruit1.txt") as f:
    for fruit in f:
        fruit1.add(fruit.rstrip("\n\r"))

with open("./Ch08/fruit2.txt") as f:
    for fruit in f:
        fruit2.add(fruit.rstrip("\n\r"))

common_fruit = fruit1 & fruit2

for fruit in common_fruit:
    print(f"{fruit}", end=" ")
print()
