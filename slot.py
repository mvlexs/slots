import random
from collections import Counter
import player
import input
prizelist = ['🍒','🍑','🍋','💎','💲']
values = ['','','']

class Slot():
    roll1 = None
    roll2 = None
    roll3 = None
    prize = 0
    prizelist = ['🍒','🍑','🍋','💎','💲']
    values = values

    def __init__ (self, roll1, roll2, roll3, prize, prizelist, values):
        self.roll1 = roll1
        self.roll2 = roll2
        self.roll3 = roll3
        self.prize = prize
        self.prizelist = prizelist
        self.values = values

    def roll(self):
        self.roll1 = random.choice(self.prizelist)
        self.roll2 = random.choice(self.prizelist)
        self.roll3 = random.choice(self.prizelist)
        self.values = [self.roll1,self.roll2,self.roll3]
        print(self.values)
        self.checkWin()

    def checkWin(self):
        print(Counter(self.values).most_common(1))
        

    def checkPrize(self):
        pass

    def again(self):
        pass