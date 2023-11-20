from knight import Knight

# for name in ["Arthur","Galahad","Lancelot","Robin","Bedevere","Gawain"]:
#     k = Knight(name)
#     print(f"{k.name:10s} | {k.title:5s} | {k.color:13s} | {k.quest:10s} | {k.comment}")

k1 = Knight("Galahad")
k2 = Knight("Robin")
k1.joust(k2)