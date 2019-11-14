from creature import Creature

class Monster(Creature):

    def __init__ (self, hp, atk, deff, name):
        Creature.__init__(self, hp, atk, deff, name)
        
