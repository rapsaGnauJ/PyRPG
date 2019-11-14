import random as r
from creature import Creature

class Keia(Creature):

    MANA_MAX = 100
    MANA_COST = 69
    
    def __init__ (self, hp, atk, deff, name):
        Creature.__init__(self, hp, atk, deff, name)
        self.mana = 0
        
    def special_attack (self, creature):
        if (self.mana >= self.MANA_COST):
            creature.attacked(self.atk * 1.5)
            self.mana -= self.MANA_COST
        else:
            self.attack(creature)

    def attack (self, creature):
        Creature.attack(self, creature)
        self.mana = min(self.mana + int(r.uniform(10, 20)), self.MANA_MAX)

    def set_name (self, name):
        self.name = name

    def get_name (self):
        return self.name

    def print_stats_min (self):
        Creature.print_stats_min(self)
        print("MANA: " + str(self.mana) + " / " + str(self.MANA_MAX) + ".")
    
