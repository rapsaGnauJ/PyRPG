class Creature():

    def __init__ (self, hp, atk, deff, name):
        self.HP_MAX = hp
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.name = name

    def attack (self, creature):
        creature.attacked(self.atk)
        
    def attacked (self, atk):
        self.hp = max(0, min(self.hp - atk / (self.deff / 10), self.HP_MAX))

    def get_hp (self):
        return self.hp

    def get_name (self):
        return self.name

    def is_dead (self):
        return self.hp <= 0

    def print_stats_min (self):
        print(str(self.name) + "'s status:")
        print("HP: " + str(self.hp) + " / " + str(self.HP_MAX) + ".")
        
    def print_stats_full (self):
        print_stats_min()
        print("ATK: " + str(self.atk) + ".")
        print("DEFF: " + str(self.deff) + ".")
