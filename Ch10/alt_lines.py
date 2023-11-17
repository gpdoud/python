
alist = []
blist = []

with open("./Ch10/alt.txt") as f :
    lines = f.read().splitlines()
    for line in lines :
        if line[0] == "a" :
            alist.append(line + "\n")
        elif line[0] == "b" :
            blist.append(line + "\n")

alist.sort()
blist.sort(reverse=True)

with open("./Ch10/a_sorted.txt", "w") as fa:
    fa.writelines(alist)

with open("./Ch10/b_sorted.txt", "w") as fb:
    fb.writelines(blist)

print("Done ...")