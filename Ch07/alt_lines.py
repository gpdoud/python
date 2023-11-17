
afile = open("./Ch07/a.txt", "w")
bfile = open("./Ch07/b.txt", "w")

with open("./Ch07/alt.txt") as f :
    lines = f.read().splitlines()
    for line in lines :
        if line[0] == "a" :
            afile.write(line + "\n")
            # print("write to a")
        elif line[0] == "b" :
            bfile.write(line + "\n")
            # print("write to b")


afile.close()
bfile.close()

print("Done ...")