from weapons import *
import random
import re

class Weapon:
    def __init__(self, name, type, is_two_handed, is_right_hand_weapon, physical_dmg, fire_dmg, ice_dmg, electricity_dmg, skeleton_dmg_bonus, goblin_dmg_bonus):
        self.name = name
        self.type = type
        self.is_two_handed = is_two_handed
        self.is_right_hand_weapon = is_right_hand_weapon
        self.physical_dmg = physical_dmg
        self.fire_dmg = fire_dmg
        self.ice_dmg = ice_dmg
        self.electricity_dmg = electricity_dmg
        self.skeleton_dmg_bonus = skeleton_dmg_bonus
        self.goblin_dmg_bonus = goblin_dmg_bonus

    # Start weapon
    def create_starterweapon():
        import random 
        weapontype = random.choice(weapontypes)
        starterweapon = Weapon(
            name = 'Noob ' + weapontype,
            type = weapontype,
            is_two_handed = False,
            physical_dmg = random.randint(8,13),
            fire_dmg=0,
            electricity_dmg=0,
            ice_dmg=0,
            skeleton_dmg_bonus= 1.1,
            goblin_dmg_bonus=1.2
        )
        return starterweapon

    def choose_random_attribute(self, inputs):
        # determine damage type of weapon randomly
        dmg_type = random.choice(inputs)
        # create dictionary to determine which random attribute gets picked
        dmg_types= {}
        dmg_types['none'] = 0
        for i in inputs:
            dmg_types[i] = 0
        
        dmg_types.update({dmg_type : 1})

        return dmg_types


    def generate_weapon(self, mainchar):
        # choose random damage type
        dmg_types = self.choose_random_attribute(['Fiery', 'Icy', 'Electric'])

        # Create weapon object
        dropped_weapon = Weapon(
            # name = dmg type + weapon type (added below)
            name = str({i for i in dmg_types if dmg_types[i]==1}), 
            type= random.choice(weapontypes),
            physical_dmg = round(random.randint(8,13) * float('1.' + str(mainchar.level)),1),
            fire_dmg = dmg_types['Fiery'],
            ice_dmg = dmg_types['Icy'],
            electricity_dmg = dmg_types['Electric'],
            #critical_chance=1,
            is_two_handed = False,
            skeleton_dmg_bonus = 1,
            goblin_dmg_bonus = 1

        )

        dropped_weapon.name = dropped_weapon.name + ' ' + dropped_weapon.type # attach weapon type
        dropped_weapon.name = re.sub('[\{\}\']+', '', dropped_weapon.name) # remove special characters

        return dropped_weapon


weapontypes = ['Staff','Axe','Sword','Flail','Spear','Mace']