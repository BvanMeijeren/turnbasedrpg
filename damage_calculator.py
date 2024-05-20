import random

# this file make sure that resistances and such are taken into account when the player or an enemy attacks

def critical_multiplier(critical_chance, critical_multiplier):
    
    real_critical_multiplier = 1 # no crit means 1
    
    # critical hits
    is_critical_hit = random.random() < critical_chance

    if is_critical_hit:
        critical_multiplier

    return real_critical_multiplier
   

def calculate_dmg(attacker, defender, physical_dmg, fire_dmg, ice_dmg, electricity_dmg):

    # elemental dmg / defence
    physical_dmg = round(physical_dmg / (defender.physical_def / 10), 0) * 10
    fire_dmg = round(fire_dmg / (defender.fire_def / 10), 0) * 10 # if fire_def is 120 and dmg 10, then (10 / 12) *10 =  8 (rounded)
    ice_dmg = round(ice_dmg / (defender.ice_def / 10), 0) * 10
    electricity_dmg = round(electricity_dmg / (defender.electricity_def / 10), 0) * 10

    # combined dmg with crits
    combined_dmg = (physical_dmg + fire_dmg + ice_dmg + electricity_dmg) * critical_multiplier(attacker.critical_chance, attacker.critical_multiplier)

    # apply dmg to defender
    defender.hitpoints = defender.hitpoints - combined_dmg
