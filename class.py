class Hero:
        def __init__(self, name, moola, inventory, stand):
                self.name = name
                self.moola = moola
                self.inventory = [inventory]
                self.stand = stand
        
        def buy(self, item):
                self.inventory.append(item)
                print(self.inventory["title"])

Luka_Kid = Hero("Luka Kid", "15000", "Dual Deringers", "SPTW" )

Luka_Kid.buy({"title": "Winchester Repeater", "atk": 26})
