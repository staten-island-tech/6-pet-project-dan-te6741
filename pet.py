print("Welcome to take care of Iggy simulator. The Stardust Crusaders are on a sideplot or smth idk and u gotta take care of their dog while they're gone.")
print("Tutorial: Your goal is to keep Iggy fed, happy, and entertained for as long as possible. Each day you'll have 3 energy to spend how you wish. When Iggy gets too unhappy, too hungry, or too bored, you'll lose. To prevent that from happening, keep all of his values above 0 by feeding and playing with him. (If boredom hits 100, you also lose) Every day he loses 20 hunger. He also loses 20 hapiness. Play with him to make him gain 10 hapiness and lose one boredom, Feed him to keep his hunger up (+10 hunger per feeding). You may also rest to gain 1 energy but also gain 20 boredom. He starts at 50 hapiness, 50 hunger, and 25 boredom. Good luck!!")
energy = 3
day = 1
action = 0
blablabla = 1
class Pet:
    def __init__(self, name, owner, hapiness, hunger, boredom):
        self.name = name
        self.owner = owner
        self.__hapiness = hapiness
        self.__hunger = hunger
        self.__boredom = boredom
    def play(self):
        if energy > 0:
            self.__hapiness =+ 10
            energy -= 1
            self.__boredom =-1
            print (self.name,"visciously attacks you with The Fool. He then laughs in your face. +10 hapiness, -1 energy, -1 boredom")
        else:
            print("You're too tired to play with Iggy right now. Some rest would be nice")
    def feed(self):
        if energy > 0:
            self.__hunger += 10
            energy -= 1
            print ("you fed",self.name, "some coffee flavored gum. He chewed it up and put it in your hat. +10 hapiness, -1 energy")
        else:
            print("You're too tired to feed Iggy right now. Some rest would be nice.")
    def rest(self):
        energy+= 1
        boredom += 20
        print("You take a quick nap. Iggy seems pretty bored but at least you're less tired.")


Iggy =Pet("Iggy", "Daniel", "50", "50", "25")


def showstatus():
    print("Current stats:")
    print("Hapiness:", Iggy._Pet__hapiness)
    print("Hunger:", Iggy._Pet__hunger)
    print("Boredom:", Iggy._Pet__boredom)
    print(energy)

imrunningoutofideasforvariables = input(print("What would you like to do? 1= Play with Iggy. 2= Feed Iggy. 3= Rest. 4= Show Stats. 5= Move on to next day."))
while blablabla == 1:
    if imrunningoutofideasforvariables == 1:
        Iggy.play()
        action == 0
        print(imrunningoutofideasforvariables)
    elif imrunningoutofideasforvariables == 2:
        Iggy.feed()
        action == 0
        print(imrunningoutofideasforvariables)
    elif imrunningoutofideasforvariables == 3:
        Iggy.rest
        action == 0
        print(imrunningoutofideasforvariables)
    elif imrunningoutofideasforvariables == 4:
        showstatus()
        action == 0
        print(imrunningoutofideasforvariables)
    elif imrunningoutofideasforvariables == 5:
        day =day+1
        Iggy._Pet__hapiness -= 20
        Iggy._Pet__hunger -= 20
        energy = 3
        print ("Day", day, showstatus)
        print (imrunningoutofideasforvariables)
    if Iggy._Pet__hapiness <= 0 or Iggy._Pet__hunger <= 0 or Iggy._Pet__boredom >= 100:
        if Iggy._Pet__hapiness <= 0:
            print("Iggy got too unhappy and brutally murdered you with his stand for fun")
        elif Iggy._Pet__hunger <= 0:
            print("Iggy got too hungry and devoured you")
        elif Iggy._Pet__boredom >= 100:
            print ("Iggy got too bored and forced you to become his jester for eternity")
        print ("You lasted", day, "days!")




    




