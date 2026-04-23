print("Welcome to take care of Iggy simulator. The Stardust Crusaders are on a sideplot or smth idk and u gotta take care of their dog while they're gone.")
print("Tutorial: Your goal is to keep ")

class Pet:
    def __init__(self, name, owner, hapiness, hunger, energy, boredom):
        self.name = name
        self.owner = owner
        self.__hapiness = hapiness
        self.__hunger = hunger
        self.__energy = energy
        self.__boredom = boredom
    def play(self):
        self.__hapiness =+ 10
        self.__energy -= 1
        print (self.name,"visciously attacks you with The Fool. He then laughs in your face. +10 hapiness, -1 energy")
    def feed(self):
        self.__hunger += 10
        self.__energy -= 1
        print ("you fed",self.name, "some coffee flavored gum. He chewed it up and put it in your hat. +10 hapiness, -1 energy")


Iggy =Pet("Steel Ball", "Daniel", "50", "50", "3")


def showstatus():
    print("Hapiness:", Iggy._Pet__hapiness)
    print("Hunger:", Iggy._Pet__hunger)



