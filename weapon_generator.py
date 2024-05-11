from weapons import *
import random
import re

def choose_random_attribute(inputs):
    # determine damage type of weapon randomly
    dmg_type = random.choice(inputs)
    # create dictionary to determine which random attribute gets picked
    dmg_types= {}
    dmg_types['none'] = 0
    for i in inputs:
        dmg_types[i] = 0
    
    dmg_types.update({dmg_type : 1})

    return dmg_types


def generate_weapon(mainchar):
    # choose random damage type
    dmg_types = choose_random_attribute(['Fiery', 'Icy', 'Electric'])

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