from damage_calculator import calculate_dmg

# regular attack
def attack(attacker, defender):

    equipped_weapon = attacker.equipped_weapon.fire_dmg
    
    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        physical_dmg=attacker.equipped_weapon.physical_dmg,
        fire_dmg=attacker.equipped_weapon.fire_dmg,
        ice_dmg=attacker.equipped_weapon.ice_dmg,
        electricity_dmg=attacker.equipped_weapon.electricity_dmg
        )

    if dmg:
        defender.hitpoints = defender.hitpoints - dmg


# spells
def fireball(attacker, defender):

    physical_dmg=0,
    fire_dmg = 10
    ice_dmg = 0
    electricity_dmg = 0

    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        physical_dmg=physical_dmg,
        fire_dmg=fire_dmg,
        ice_dmg=ice_dmg,
        electricity_dmg=electricity_dmg
        )
    
    if dmg:
        defender.hitpoints = defender.hitpoints - dmg
    
def ice_shard(attacker, defender):

    physical_dmg=0,
    fire_dmg = 0
    ice_dmg = 10
    electricity_dmg = 0

    dmg = calculate_dmg(
        attacker=attacker, 
        defender=defender, 
        physical_dmg=physical_dmg,
        fire_dmg=fire_dmg,
        ice_dmg=ice_dmg,
        electricity_dmg=electricity_dmg
        )

    if dmg:
        defender.hitpoints = defender.hitpoints - dmg
    
# list of all spells
all_spells = [fireball, ice_shard]