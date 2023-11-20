from random import randint

class Knight:

    def __init__(self, name):
        self._name = name
        knights = {}
        with open("pybasics/DATA/knights.txt") as f:
            lines = f.readlines()
            for line in lines:
                xname, title, color, quest, comment = line.rstrip().split(":")
                knights[xname] = xname, title, color, quest, comment
        knight = knights[name]        
        self._title = knights[name][1]
        self._color = knights[name][2]
        self._quest = knights[name][3]
        self._comment = knights[name][4]
        self._strength = randint(0, 100)

    def joust(self, knight):
        if self.strength >= knight.strength:
            print(f"{self.name} wins!")
        else:
            print(f"{knight.name} wins!")

    @property
    def name(self):
        return self._name
        
    @property
    def title(self):
        return self._title

    @property
    def color(self):
        return self._color

    @property
    def quest(self):
        return self._quest

    @property
    def comment(self):
        return self._comment

    @property
    def strength(self):
        return self._strength




