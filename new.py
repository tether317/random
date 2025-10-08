class fighter():
    def __init__(self, name = 'unnamed player', hp = 100, stam = 100):
        self.name = name
        self.hp = hp
        self.stam = stam
    
    def print_info(self):
        print(
            f'''
            --- PLR STATS ---
            NAME:   {self.name}
            HP:     {self.hp}
            STAM:   {self.stam}
            '''
        )

class weapon():
    def __init__(self, name = 'unnamed weapon', dmg = 35, drain = 0, negation = 0):
        self.name = name
        self.dmg = dmg
        self.drain = drain
        self.negation = negation
    
    def print_info(self):
        print(
            f'''
            --- WEP STATS ---
            NAME:       {self.name}
            DRAIN:      {self.drain}
            NEGATION:   {self.negation}
            '''
        )

class seer():
    def __init__(self):
        print('SEER was created.')

if __name__ == '__main__':
    print('RUNNING')

    wep_list = {
        "maul"  :   weapon('Maul', 64, 24, 13)
    }

    wep_list["maul"].print_info()
    


input(
'''
###############################
### Press [ENTER] to close. ###
###############################
'''
)