class Creature():

    def __init__ (self, hp, atk, deff, name):
        self.MAX_HP = hp
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.name = name

    def attack (self, creature):
        creature.attacked(self.atk)
        
    def attacked (self, atk):
        self.hp -= atk / (creature.deff / 10)

    def get_hp (self):
        return self.hp

    def get_name (self):
        return self.name
