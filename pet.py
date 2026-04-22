class Pet:
    def __init__(self, name, owner, hapiness, hunger):
        self.name = name
        self.owner = owner
        self.__hapiness = hapiness
        self.__hunger = hunger
    def play(self):
        self.__hapiness =+ 10
        print (self.name,"is playing with you")
    def feed(self):
        self.__hunger =+ 10
        print ("you fed",self.name, "a treat!")


DanielJr =Pet("Daniel Jr", "Daniel", "0", "0")

DanielJr.play()
def showstatus():
    print("Hapiness:", DanielJr._Pet__hapiness)
    print("Hunger:", DanielJr._Pet__hunger)

showstatus()

