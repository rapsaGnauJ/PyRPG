import random as r

class Keia(Creature):

    MANA_MAX = 100
    MANA_COST = 69
    
    def __init__ (self, hp, atk, deff, name):
        Creature.__init__(self, hp, atk, deff, name)
        self.mana = 0
        
    def special_attack (self, creature):
        if (mana >= MANA_COST):
            creature.attaked(self.atk * 1.5)
            mana -= MANA_COST

    def attack (self, creature):
        Creature.attack(creature)
        mana = max(mana + r.uniform(10, 20), MAX_MANA)

    def set_name (self, name):
        self.name = name

    def get_name (self):
        return self.name

    def print_stats_min (self):
        print(self.name + "status:\n")
        print("HP: " + self.hp + " / " + self.MAX_HP + ".\n")
        print("MANA: " + self.mana + " / " + self.MAX_MANA + ".\n")
        
    def print_stats_full (self):
        print_stats_min()
        print("ATK: " + self.atk + ".\n")
        print("DEFF: " + self.deff + ".\n")

    
