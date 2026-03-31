import random

class fighter():
    name = 'unnamed'
    maxhealth  = 300
    health = maxhealth
    damage = 15
    skill = 0
    def __init__(self, name='unnamed'):
        self.name = name
        print('NEW FIGHTER: ' + self.name)

    def attack(self):
        multi = round((random.randint(0,20) * 0.01 + 1), 2)
        return self.damage * multi

    def hurt(self, dmg):
        self.health -= dmg

    def get_name(self): return self.name
    def get_health(self): return self.health
    def get_maxhealth(self): return self.maxhealth
    def get_damage(self): return self.damage

class arena():
    duelers = []

    def duel(self, fighter1, fighter2):
        duelers = [fighter1, fighter2]
        while True:
            duelers[1].hurt(duelers[0].attack())
            duelers[0].hurt(duelers[1].attack())

            for dueler in duelers:
                print(dueler.get_name() + ' health: ' + str(round(dueler.get_health(), 2)))

            # check for winner
            if (duelers[0].get_health() <= 0) and (duelers[1].get_health() > 0):
                print(duelers[1].get_name() + ' WINS')
                break
            elif (duelers[1].get_health() <= 0) and (duelers[0].get_health() > 0):
                print(duelers[0].get_name() + ' WINS')
                break
            elif (duelers[0].get_health() <= 0) and (duelers[1].get_health() <= 0):
                print('TIE')
                break
            
print(fighter().attack())
arena = arena()
arena.duel(fighter('mars'), fighter('dak'))
