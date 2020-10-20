import random
class Character:

    def __init__(self, name, race, c, addstr,adddex, addcon,addwis, addint, addchr):
        self.characterName = name
        self.characterRace = race
        self.characterClass = c
        self.str = addstr
        self.dex = adddex
        self.con = addcon
        self.wis = addwis
        self.int = addint
        self.chr = addchr
       
    #Prints out the stats of the charater with their name, race and class
    def printstat(self):
        print("Here are the stats for", 
        self.characterName,"the", self.characterRace,
        self.characterClass,":")
        print("\tStrength:", self.str)
        print("\tDexterity:", self.dex)
        print("\tConstitition:", self.con)
        print("\tWisdom:", self.wis)
        print("\tInteligence", self.int)
        print("\tCharisma", self.chr)

    def changeName(self):
        print("What would you like to change?")
        print("Name, Race, or Class?")
        
        responce = input()
        shouldLoop = True
        
        while shouldLoop == True:
            if responce in ["name", "Name", "n", "N"]:
                self.characterName = input("New name: ")
                shouldLoop = False

            elif responce in ["race", "Race", "r", "R"]:
                self.characterRace = input("New race: ")
                shouldLoop = False

            elif responce in ["class", "Class", "c", "C"]:
                self.characterClass = input("New class: ")
                shouldLoop = False
            else:
                print("Invalid input")
                responce = input()
            

    #this will roll the 
    def rollBaseStat(self):
        self.str = 8 + random.randint(-2,10)
        self.dex = 8 + random.randint(-2,10)
        self.con = 8 + random.randint(-2,10)
        self.wis = 8 + random.randint(-2,10)
        self.int = 8 + random.randint(-2,10)
        self.chr = 8 + random.randint(-2,10)
    
def main():
    newCharacterBob = Character("Bob", "Orc", "Barbarian",0,0,0,0,0,0)
    newCharacterBob.rollBaseStat()
    newCharacterBob.printstat()

    print()

    newCharacterJill = Character("Jill", "Elf", "Ranger",12,18,8,14,10,13)
    newCharacterJill.printstat()
    
    print("Let's re-roll Jill's stats, and change one thing")
    newCharacterJill.rollBaseStat()
    newCharacterJill.changeName()
    newCharacterJill.printstat()
    
main()

        

        



    

    

