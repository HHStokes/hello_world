import random

class Dice():
    def __init__(self):
        self.total = 0
        self.x = 0

    def rollD4(self,rollCount):

        while self.x < rollCount:
            self.total = self.total + random.randint(1,4)
            self.x = self.x + 1 
        return self.total
        
    def rollD6(self,rollCount):

        while self.x < rollCount:
            self.total = self.total + random.randint(1,6)
            self.x = self.x + 1 
        return self.total
    
    def rollD20(self,rollCount):

        while self.x < rollCount:
            self.total = self.total + random.randint(1,20)
            self.x = self.x + 1 
        return self.total
    