from damage_calculator import calculate_dmg

# regular attack
def attack(attacker, defender):

    equipped_weapon = attacker.equipped_weapon.fire_dmg
    
    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        fire_dmg=equipped_weapon.fire_dmg,
        ice_dmg=equipped_weapon.ice_dmg,
        electricity_dmg=equipped_weapon.electricity_dmg
        )
    
    defender.hitpoints = defender.hitpoints - dmg


# spells

def fireball(attacker, defender):

    fire_dmg = 10
    ice_dmg = 0
    electricity_dmg = 0

    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        fire_dmg=fire_dmg,
        ice_dmg=ice_dmg,
        electricity_dmg=electricity_dmg
        )
    
def ice_shard(attacker, defender):

    fire_dmg = 0
    ice_dmg = 10
    electricity_dmg = 0

    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        fire_dmg=fire_dmg,
        ice_dmg=ice_dmg,
        electricity_dmg=electricity_dmg
        )