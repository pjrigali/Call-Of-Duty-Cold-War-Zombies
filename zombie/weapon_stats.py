# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:58:18 2021

@author: Peter

See gun_critical_value and gun_acc_value for each weapon. Make changes to reflect your metrics. 
These can be found in game Barracks\\Combat Record\\Zombies\\Weapon Name.

"""


class Weapon:
    name: str = None
    """Name of weapon in game"""

    temp_name: str = None
    """Name of weapon given by user"""

    damage_1: float = None
    """Damage value before first drop off"""

    damage_2: float = None
    """Damage value before second drop off"""

    damage_3: float = None
    """Damage value before third drop off"""

    range_1: float = None
    """Distance to first drop off"""

    range_2: float = None
    """Distance to second drop off"""

    fire_rate: float = None
    """Weapon rate of fire"""

    velocity: float = None
    """Weapon bullet velocity"""

    armour_damage: float = 1.0
    """Weapon damage to armour"""

    melee: float = 1000.0
    """Weapon melee time in ms"""

    movement: float = None
    """Weapon movement speed"""

    sprint: float = None
    """Weapon sprinting speed"""

    shoot_speed: float = None
    """Weapon shooting movement speed"""

    sprint_to_fire: float = None
    """Weapon sprint to fire time in ms"""

    aim_walking: float = None
    """Weapon aim walking movement speed"""

    ads: float = None
    """Weapon aim down sight time"""

    vertical_recoil: float = None
    """Weapon vertical recoil value"""

    horizontal_recoil: float = None
    """Weapon horizontal recoil value"""

    centering_speed: float = None
    """Weapon speed at re-centering after each shot. Lower is better"""

    idle_sway: float = None
    """Weapon aim sway when aim down sight"""

    flinch: float = 10.0
    """Weapon flinch value"""

    hip_fire: float = None
    """Weapon hipfire cross hair spread. Lower is better"""

    mag_capacity: float = None
    """Weapon ammo magazine capacity"""

    reload: float = None
    """Weapon reload time in seconds"""

    starting_ammo: float = None
    """Weapon starting ammo in reserve"""

    ammo_capacity: float = None
    """Weapon max ammo capacity"""

    burst: float = 1.0
    """Weapon burst multiplier. Value is 3 if weapon uses burst fire"""

    pap_burst: float = 1.0
    """Weapon burst fire after pack-a-punch multiplier. M16 and CARV.2 have a 6 round burst after pack-a-punch"""

    long_shot: float = None
    """Weapon distance to be considered a longshot in game"""

    gun_critical_value: float = 0.50
    """User inputted gun critical hit percentage. 
    This can be found in game Barracks\\Combat Record\\Zombies\\Weapon Name"""

    gun_acc_value: float = 0.50
    """User inputted gun critical hit percentage. 
    This can be found in game Barracks\\Combat Record\\Zombies\\Weapon Name"""

    critical: float = 2.8
    """Weapon critical hit multiplier"""

    long: float = 1.0
    """Weapon multiplier for damage at a distance"""

    close: float = 1.0
    """Weapon multiplier for damage at close range"""

    salvage: float = 1.0
    """Weapon salvage multiplier"""

    equipment: float = 1.0
    """Weapon multiplier for dropped equipment"""

    attachments: float = 1.0
    """Weapon number of attachments allowed"""

    weapon_type: str = None
    """Weapon category. (smg, sniper, ...)"""

    pack: str = None
    """Weapon pack-a-punch level"""

    rare: str = None
    """Weapon rarity level"""

    muzzle: dict = {'None': ['None']}
    """Weapon muzzle attachment"""

    barrel: dict = {'None': ['None']}
    """Weapon barrel attachment"""

    body: dict = {'None': ['None']}
    """Weapon body attachment"""

    under_barrel: dict = {'None': ['None']}
    """Weapon underbarrel attachment"""

    magazine: dict = {'None': ['None']}
    """Weapon ammo magazine attachment"""

    handle: dict = {'None': ['None']}
    """Weapon handle attachment"""

    stock: dict = {'None': ['None']}
    """Weapon stock attachment"""


class Assault(Weapon):
    damage_2 = 0.00
    range_2 = 0.00
    movement = 10.26
    sprint = 14.49
    shoot_speed = 9.18
    sprint_to_fire = 400.0
    aim_walking = 4.06
    idle_sway = 20.0
    hip_fire = 7.5
    mag_capacity = 30.0
    starting_ammo = 90.0
    ammo_capacity = 180.0
    long_shot = 41.0
    weapon_type = 'Assault'
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range',
                       '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 33% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Extended': ['+ 30% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 7% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 3% Vertical Recoil Control', '+ 17% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                           '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Xm4(Assault):
    name = 'XM4'
    temp_name = 'Base XM4'
    damage_1 = 30.0
    damage_3 = 28.0
    range_1 = 45.72
    fire_rate = 722.0
    velocity = 657.0
    ads = 300.0
    vertical_recoil = 360.0
    horizontal_recoil = 30.0
    centering_speed = 11.0
    reload = 2.6
    gun_acc_value = 0.58
    gun_critical_value = 0.49
    critical = 4.4
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 11% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 15% Vertical Recoil Control', '- 5% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 22% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'Buffer Tube': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 30% Reload Quickness'],
        'Speed Mag': ['+ 17% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 17% Max Starting Ammo',
                      '+ 17% Ammo Capacity'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Mini Clamp': ['+ 50% Reload Quickness', '+ 11% Max Starting Ammo', '+ 10% Aim Down Sight Time',
                       '- 17% Ammo Capacity', '- 17% Magazine Ammo Capacity'],
        'Salvo Fast Mag': ['+ 50% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 50% Max Starting Ammo',
                           '+ 50% Ammo Capacity', '- 12% Aim Down Sight Time'],
    }


class Ak47(Assault):
    name = 'AK47'
    temp_name = 'Base AK47'
    damage_1 = 38.0
    damage_3 = 30.0
    range_1 = 38.1
    fire_rate = 600.0
    velocity = 702.0
    shoot_speed = 8.92
    ads = 300.0
    vertical_recoil = 405.0
    horizontal_recoil = 84.0
    centering_speed = 11.0
    reload = 2.6
    gun_acc_value = 0.59
    gun_critical_value = 0.49
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 13% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Spetsnaz Compensator': ['+ 9% Vertical Recoil Control', '- 7% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 10% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 6% Vertical Recoil Control',
                           '- 27% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'VDV Reinforced': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                           '- 20% Aim Walking Movement Speed'],
        'Liberator': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'RPK': ['+ 8% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity', '- 33% Max Starting Ammo',
                '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 3% Vertical Recoil Control', '+ 17% Horizontal Recoil Control',
                          '- 26% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Taped Mags': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Bakelite Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'GRU Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                         '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class Krig(Assault):
    name = 'Krig'
    temp_name = 'Base Krig'
    damage_1 = 33.0
    damage_3 = 28.0
    range_1 = 50.8
    fire_rate = 652.0
    velocity = 686.0
    ads = 300.0
    vertical_recoil = 379.5
    horizontal_recoil = 72.0
    centering_speed = 10.0
    reload = 2.4
    gun_acc_value = 0.64
    gun_critical_value = 0.51
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 15% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Contour': ['+ 10% Strafe Speed', '- 12% Bullet Velocity', '+ 15% Aim Walking Movement Speed'],
        'Ranger': ['+ 126% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'CMV Mil-Spec': ['+ 6% Damage', '+ 5% Strafe Speed', '- 33% Max Starting Ammo', '- 40% Effective Damage Range',
                         '+ 20% Aim Walking Movement Speed'],
    }
    under_barrel = {
        'Fore grip': ['+ 17% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 5% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 6% Sprinting Move Speed', '+ 16% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Qbz(Assault):
    name = 'QBZ'
    temp_name = 'Base QBZ'
    damage_1 = 32.0
    damage_3 = 28.0
    range_1 = 45.72
    fire_rate = 681.0
    velocity = 671.0
    movement = 10.53
    sprint = 14.8
    shoot_speed = 9.74
    ads = 283.0
    vertical_recoil = 350.0
    horizontal_recoil = 85.0
    centering_speed = 10.0
    reload = 2.5
    gun_acc_value = 0.61
    gun_critical_value = 0.60
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 17% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 13% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 12% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 33% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Ranger': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 6% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 3% Vertical Recoil Control', '+ 16% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 4% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 3% Movement Speed',
                            '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'CQB Pad': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Ffar(Assault):
    name = 'FFAR'
    temp_name = 'Base FFAR'
    damage_1 = 28.0
    damage_3 = 23.0
    range_1 = 38.1
    fire_rate = 909.0
    velocity = 629.0
    ads = 300.0
    vertical_recoil = 330.0
    horizontal_recoil = 180.0
    centering_speed = 10.0
    reload = 2.1
    gun_acc_value = 0.64
    gun_critical_value = 0.51
    critical = 4.5
    mag_capacity = 40
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 10% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 8% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 20% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Ranger': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 4% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 6% Vertical Recoil Control', '+ 16% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 52% Magazine Ammo Capacity', '+ 52% Max Starting Ammo', '+ 52% Ammo Capacity',
                '- 5% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 52% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 52% Max Starting Ammo',
                      '+ 52% Ammo Capacity', '- 10% Aim Down Sights Time'],
        'STANAG Mag': ['+ 76% Magazine Ammo Capacity', '+ 76% Max Starting Ammo', '+ 76% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 76% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 76% Max Starting Ammo',
                           '+ 76% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'CQB Pad': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Groza(Assault):
    name = 'Groza'
    temp_name = 'Base Groza'
    damage_1 = 34.0
    damage_3 = 28.0
    range_1 = 53.34
    fire_rate = 750.0
    velocity = 660.0
    ads = 266.0
    vertical_recoil = 375.0
    horizontal_recoil = 130.0
    centering_speed = 11.0
    reload = 2.3
    gun_acc_value = 0.46
    gun_critical_value = 0.51
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 17% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 20% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 15% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 33% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Contour M2': ['+ 10% Strafe Speed', '- 10% Effective Damage Range', '+ 15% Aim Walking Movement Speed'],
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'VDV Reinforced': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                           '- 20% Aim Walking Movement Speed'],
        'GRU Composite': ['+ 25% Effective Damage Range', '+ 25% Bullet Velocity'],
        'CMV Mil-Spec': ['+ 6% Damage', '+ 5% Strafe Speed', '- 33% Max Starting Ammo', '- 40% Effective Damage Range',
                         '+ 20% Aim Walking Movement Speed'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 7% Vertical Recoil Control', '+ 17% Horizontal Recoil Control',
                          '- 26% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Taped Mags': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'GRU Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                         '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'CQB Pad': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Fara(Assault):
    name = 'FARA'
    temp_name = 'Base FARA'
    damage_1 = 30.0
    damage_3 = 27.0
    range_1 = 63.53
    fire_rate = 800.0
    velocity = 729.0
    ads = 325.0
    vertical_recoil = 400.0
    horizontal_recoil = 150.0
    centering_speed = 11.0
    reload = 2.8
    gun_acc_value = 0.48
    gun_critical_value = 0.48
    critical = 4.5
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 20% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 16% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 12% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 32% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Contour': ['+ 10% Strafe Speed', '- 18% Bullet Velocity', '+ 15% Aim Walking Movement Speed'],
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Liberator': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'RPK': ['+ 3% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity', '- 33% Max Starting Ammo',
                '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 2% Vertical Recoil Control', '+ 18% Horizontal Recoil Control',
                          '- 26% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Taped Mags': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'GRU Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                         '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class C58(Assault):
    name = 'C58'
    temp_name = 'Base C58'
    damage_1 = 38.0
    damage_3 = 34.0
    range_1 = 25.4
    fire_rate = 555.0
    velocity = 730.0
    shoot_speed = 8.92
    ads = 300.0
    vertical_recoil = 550.0
    horizontal_recoil = 220.0
    centering_speed = 17.0
    reload = 2.4
    gun_acc_value = 0.44
    gun_critical_value = 0.47
    critical = 4.5
    mag_capacity = 20
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 8% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 12% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 17% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Ranger': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 8% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 12% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 2% Vertical Recoil Control', '+ 14% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 5% Sprinting Move Speed', '+ 12% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 75% Magazine Ammo Capacity', '+ 75% Max Starting Ammo', '+ 75% Ammo Capacity',
                '- 20% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 25% Magazine Ammo Capacity', '+ 21% Reload Quickness', '+ 25% Max Starting Ammo',
                      '+ 25% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 200% Magazine Ammo Capacity', '+ 200% Max Starting Ammo', '+ 200% Ammo Capacity',
                       '- 25% Reload Quickness', '- 15% Aim Down Sight Time', '- 8% Damage'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 50% Magazine Ammo Capacity', '+ 28% Reload Quickness', '+ 50% Max Starting Ammo',
                           '+ 50% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'CQB Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Em2(Assault):
    name = 'EM2'
    temp_name = 'Base EM2'
    damage_1 = 48.0
    damage_3 = 42.0
    range_1 = 38.1
    fire_rate = 535.0
    velocity = 688.0
    shoot_speed = 8.67
    ads = 300.0
    vertical_recoil = 319.2
    horizontal_recoil = 34.5
    centering_speed = 11.0
    reload = 2.6
    gun_acc_value = 0.39
    gun_critical_value = 0.64
    critical = 4.5
    mag_capacity = 20
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range',
                       '- 8% Bullet Velocity'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 10% Vertical Recoil Control',
                              '- 33% Effective Damage Range', '- 15% Bullet Velocity'],
    }
    barrel = {
        'Ultralight': ['+ 5% Strafe Speed', '+ 10% Aim Walking Movement Speed'],
        'Ranger': ['+ 100% Bullet Velocity', '- 20% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 100% Effective Damage Range', '+ 40% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Take Down': ['+ 150% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 6% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 5% Vertical Recoil Control', '+ 15% Horizontal Recoil Control',
                             '- 26% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 5% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 25% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 25% Max Starting Ammo',
                      '+ 25% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 100% Magazine Ammo Capacity', '+ 100% Max Starting Ammo', '+ 100% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 50% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 50% Max Starting Ammo',
                           '+ 50% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'CQB Pad': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 40% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Smg(Weapon):
    movement = 10.8
    sprint = 14.8
    shoot_speed = 10.26
    sprint_to_fire = 350.0
    aim_walking = 8.55
    idle_sway = 22.5
    hip_fire = 7.0
    centering_speed = 7.0
    long_shot = 36.0
    critical = 3.8
    weapon_type = 'Smg'
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 6% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 36% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 25% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Mp5(Smg):
    name = 'MP5'
    temp_name = 'Base MP5'
    damage_1 = 32.0
    damage_2 = 27.0
    damage_3 = 23.0
    range_1 = 10.16
    range_2 = 20.0
    fire_rate = 857.0
    velocity = 250.0
    ads = 275.0
    vertical_recoil = 252.0
    horizontal_recoil = 208.0
    mag_capacity = 30.0
    reload = 2.6
    starting_ammo = 120.0
    ammo_capacity = 180.0
    gun_acc_value = 0.59
    gun_critical_value = 0.41
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 7% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 36% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 25% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 14% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 14% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 33% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 33% Max Starting Ammo',
                           '+ 33% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Collapsed Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Milano(Smg):
    name = 'Milano'
    temp_name = 'Base Milano'
    damage_1 = 42.0
    damage_2 = 30.0
    damage_3 = 28.0
    range_1 = 15.24
    range_2 = 24.0
    fire_rate = 576.0
    velocity = 225.0
    sprint_to_fire = 300.0
    ads = 233.0
    vertical_recoil = 322.0
    horizontal_recoil = 225.0
    mag_capacity = 32.0
    reload = 2.2
    starting_ammo = 128.0
    ammo_capacity = 192.0
    gun_acc_value = 0.54
    gun_critical_value = 0.42
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 15% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 35% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 24% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 12% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 7% Vertical Recoil Control', '+ 16% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 12% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 41% Magazine Ammo Capacity', '+ 41% Max Starting Ammo', '+ 41% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 41% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 41% Max Starting Ammo',
                      '+ 41% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 72% Magazine Ammo Capacity', '+ 72% Max Starting Ammo', '+ 72% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 72% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 72% Max Starting Ammo',
                           '+ 72% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Marathon Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Ak74u(Smg):
    name = 'AK74u'
    temp_name = 'Base AK74u'
    damage_1 = 38.0
    damage_2 = 30.0
    damage_3 = 27.0
    range_1 = 7.62
    range_2 = 18.0
    fire_rate = 697.0
    velocity = 383.0
    sprint = 14.54
    shoot_speed = 9.99
    ads = 300.0
    vertical_recoil = 360.0
    horizontal_recoil = 210.0
    centering_speed = 8.0
    mag_capacity = 30.0
    reload = 2.4
    starting_ammo = 120.0
    ammo_capacity = 180.0
    gun_acc_value = 0.61
    gun_critical_value = 0.57
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 33% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'VDV Reinforced': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                           '- 20% Aim Walking Movement Speed'],
        'Liberator': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Task Force': ['+ 8% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 36% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 25% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 18% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 7% Vertical Recoil Control', '+ 21% Horizontal Recoil Control',
                          '- 30% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 3% Sprinting Move Speed', '+ 18% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Taped Mags': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'GRU Mag Clamp': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                         '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class Ksp(Smg):
    name = 'KSP'
    temp_name = 'Base KSP'
    damage_1 = 50.0
    damage_2 = 38.0
    damage_3 = 35.0
    range_1 = 15.24
    range_2 = 25.0
    fire_rate = 571.0
    velocity = 265.0
    ads = 275.0
    vertical_recoil = 200.0
    horizontal_recoil = 300.0
    centering_speed = 5.0
    mag_capacity = 30.0
    reload = 2.4
    starting_ammo = 120.0
    ammo_capacity = 180.0
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 20% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 12% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    under_barrel = {
        'Front Grip': ['+ 15% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 40% Magazine Ammo Capacity', '+ 40% Max Starting Ammo', '+ 40% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 40% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 40% Max Starting Ammo',
                      '+ 40% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 60% Magazine Ammo Capacity', '+ 60% Max Starting Ammo', '+ 60% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 60% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 60% Max Starting Ammo',
                           '+ 60% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Collapsed Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Bullfrog(Smg):
    name = 'Bullfrog'
    temp_name = 'Base Bullfrog'
    damage_1 = 34.0
    damage_2 = 25.0
    damage_3 = 22.0
    range_1 = 19.05
    range_2 = 37.5
    fire_rate = 750.0
    velocity = 250.0
    ads = 275.0
    vertical_recoil = 180.0
    horizontal_recoil = 127.5
    hip_fire = 7.5
    mag_capacity = 50.0
    reload = 2.8
    starting_ammo = 150.0
    ammo_capacity = 300.0
    gun_acc_value = 0.55
    gun_critical_value = 0.50
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 13% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 15% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 25% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'VDV Reinforced': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                           '- 20% Aim Walking Movement Speed'],
        'Liberator': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Task Force': ['+ 3% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 37% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 26% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                          '- 30% Shooting Move Speed'],
        'VDV Speed Grip': ['+ 3% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                           '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 30% Magazine Ammo Capacity', '+ 30% Max Starting Ammo', '+ 30% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 30% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 30% Max Starting Ammo',
                      '+ 30% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 70% Magazine Ammo Capacity', '+ 70% Max Starting Ammo', '+ 70% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 70% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 70% Max Starting Ammo',
                         '+ 70% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class Mac10(Smg):
    name = 'Mac 10'
    temp_name = 'Base Mac 10'
    damage_1 = 27.0
    damage_2 = 24.0
    damage_3 = 22.0
    range_1 = 11.43
    range_2 = 18.0
    fire_rate = 1111.0
    velocity = 200.0
    ads = 275.0
    vertical_recoil = 392.0
    horizontal_recoil = 100.0
    centering_speed = 10.0
    mag_capacity = 32.0
    reload = 2.0
    starting_ammo = 128.0
    ammo_capacity = 192.0
    gun_acc_value = 0.46
    gun_critical_value = 0.47
    critical = 4.0
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 25% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 15% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 4% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 4% Vertical Recoil Control', '+ 12% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 8% Vertical Recoil Control', '+ 16% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 10% Horizontal Recoil Control',
                            '+ 10% Vertical Recoil Control', '- 6% Movement Speed', '- 6% Shooting Move Speed',
                            '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 34% Magazine Ammo Capacity', '+ 34% Max Starting Ammo', '+ 34% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 34% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 34% Max Starting Ammo',
                      '+ 34% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 66% Magazine Ammo Capacity', '+ 66% Max Starting Ammo', '+ 66% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 66% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 66% Max Starting Ammo',
                           '+ 66% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Lc10(Smg):
    name = 'LC10'
    temp_name = 'Base LC10'
    damage_1 = 30.0
    damage_2 = 28.0
    damage_3 = 23.0
    range_1 = 12.7
    range_2 = 51.0
    fire_rate = 800.0
    velocity = 410.0
    ads = 275.0
    vertical_recoil = 200.0
    horizontal_recoil = 60.0
    mag_capacity = 34.0
    reload = 2.5
    starting_ammo = 136.0
    ammo_capacity = 204.0
    gun_acc_value = 0.45
    gun_critical_value = 0.38
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 7% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 32% Magazine Ammo Capacity', '+ 32% Max Starting Ammo', '+ 32% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 23% Reload Quickness'],
        'Speed Mag': ['+ 24% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 24% Max Starting Ammo',
                      '+ 24% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 62% Magazine Ammo Capacity', '+ 62% Max Starting Ammo', '+ 62% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 44% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 53% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 53% Max Starting Ammo',
                           '+ 53% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Ppsh(Smg):
    name = 'PPSH'
    temp_name = 'Base PPSH'
    damage_1 = 28.0
    damage_2 = 27.0
    damage_3 = 22.0
    range_1 = 15.25
    range_2 = 25.0
    fire_rate = 909.0
    velocity = 200.0
    ads = 275.0
    vertical_recoil = 150.0
    horizontal_recoil = 150.0
    mag_capacity = 32.0
    reload = 2.2
    starting_ammo = 128.0
    ammo_capacity = 192.0
    gun_acc_value = 0.39
    gun_critical_value = 0.38
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 5% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 25% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 4% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 18% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 8% Vertical Recoil Control', '+ 22% Horizontal Recoil Control',
                          '- 30% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 3% Sprinting Move Speed', '+ 18% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 72% Magazine Ammo Capacity', '+ 72% Max Starting Ammo', '+ 72% Ammo Capacity',
                '- 36% Reload Quickness'],
        'Taped Mags': ['+ 18% Reload Quickness'],
        'Speed Mag': ['+ 25% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 25% Max Starting Ammo',
                      '+ 25% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 122% Magazine Ammo Capacity', '+ 122% Max Starting Ammo', '+ 122% Ammo Capacity',
                         '- 42% Reload Quickness', '- 18% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 56% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 56% Max Starting Ammo',
                         '+ 56% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'CQB Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class Ots9(Smg):
    name = 'OTS'
    temp_name = 'Base OTS'
    damage_1 = 35.0
    damage_2 = 25.0
    damage_3 = 23.0
    range_1 = 12.7
    range_2 = 20.0
    fire_rate = 857.0
    velocity = 250.0
    ads = 275.0
    vertical_recoil = 252.0
    horizontal_recoil = 208.0
    mag_capacity = 20.0
    reload = 2.4
    starting_ammo = 80.0
    ammo_capacity = 120.0
    gun_acc_value = 0.36
    gun_critical_value = 0.59
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Spetsnaz Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 5% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 25% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 6% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 14% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                          '- 30% Shooting Move Speed'],
        'Spetsnaz Speed Grip': ['+ 3% Sprinting Move Speed', '+ 14% Horizontal Recoil Control', '- 6% Movement Speed',
                                '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mags': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 25% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 25% Max Starting Ammo',
                      '+ 25% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 100% Magazine Ammo Capacity', '+ 100% Max Starting Ammo', '+ 100% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 60% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 60% Max Starting Ammo',
                         '+ 60% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed',
                           '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class Tec9(Smg):
    name = 'Tec9'
    temp_name = 'Base Tec9'
    damage_1 = 50.0
    damage_2 = 40.0
    damage_3 = 30.0
    range_1 = 20.32
    range_2 = 30.0
    fire_rate = 451.0
    velocity = 258.0
    ads = 233.0
    vertical_recoil = 252.0
    horizontal_recoil = 65.0
    mag_capacity = 21.0
    reload = 2.0
    starting_ammo = 84.0
    ammo_capacity = 126.0
    gun_acc_value = 0.41
    gun_critical_value = 0.59
    critical = 4.2
    muzzle = {
        'Muzzle Brake': ['+ 4% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Burst Repeater': ['+ 10% Horizontal Recoil Control', '- 15% Effective Damage Range', '+ 17% Fire Rate'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Full Repeater': ['- 5% Horizontal Recoil Control', '- 25% Effective Damage Range', '+ 45% Fire Rate'],
    }
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Ranger': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 18% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 20% Aim Walking Movement Speed'],
        'Rifled': ['+ 25% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 6% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    under_barrel = {
        'Fore grip': ['+ 15% Horizontal Recoil Control'],
        'Red Cell Fore grip': ['+ 4% Sprinting Move Speed', '+ 30% Melee Quickness', '- 3% Movement Speed',
                               '- 3% Shooting Move Speed', '- 3% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 4% Sprinting Move Speed', '+ 3% Sprint to Fire Time'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 6% Vertical Recoil Control', '+ 20% Horizontal Recoil Control',
                             '- 30% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 3% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 43% Magazine Ammo Capacity', '+ 43% Max Starting Ammo', '+ 43% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 29% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 29% Max Starting Ammo',
                      '+ 29% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 86% Magazine Ammo Capacity', '+ 86% Max Starting Ammo', '+ 86% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 57% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 57% Max Starting Ammo',
                           '+ 57% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 15% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Marksman(Weapon):
    movement = 10.26
    sprint = 14.49
    aim_walking = 3.28
    idle_sway = 15.0
    ads = 350.0
    hip_fire = 8.5
    long_shot = 41.0
    critical = 4.2
    weapon_type = 'Marksman'
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 36% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Front Grip': ['+ 30% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 10% Vertical Recoil Control', '+ 40% Horizontal Recoil Control',
                             '- 16% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 6% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 50% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 50% Max Starting Ammo',
                      '+ 50% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 80% Magazine Ammo Capacity', '+ 80% Max Starting Ammo', '+ 80% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 80% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 80% Max Starting Ammo',
                           '+ 80% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 20% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Type63(Marksman):
    name = 'Type 63'
    temp_name = 'Base Type 63'
    damage_1 = 68.0
    damage_2 = 68.0
    damage_3 = 49.0
    range_1 = 50.8
    range_2 = 63.0
    fire_rate = 361.0
    velocity = 625.0
    shoot_speed = 8.12
    sprint_to_fire = 400.0
    vertical_recoil = 390.0
    horizontal_recoil = 180.0
    centering_speed = 7.5
    mag_capacity = 30.0
    reload = 2.7
    starting_ammo = 90.0
    ammo_capacity = 180.0
    burst = 1.0
    gun_acc_value = 0.73
    gun_critical_value = 0.55
    muzzle = {
        'Muzzle Brake': ['+ 10% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Silencer': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Spetsnaz Compensator': ['+ 25% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 13% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 12% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control',
                           '- 33% Effective Damage Range', '- 30% Bullet Velocity'],
    }
    barrel = {
        'Rapid Fire': ['+ 8% Rate of Fire'],
        'Titanium': ['+ 17% Fire Rate', '- 25% Effective Damage Range'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Strike Team': ['+ 9% Damage', '+ 11% Fire Rate', '- 25% Effective Damage Range', '- 10% Idle Sway Control'],
        'Match Grade': ['+ 100% Bullet Velocity', '- 6% Sprinting Move Speed'],
        'Task Force': ['+ 9% Damage', '+ 100% Effective Damage Range', '+ 60% Bullet Velocity',
                       '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    body = {
        'Steady Aim Laser': ['+ 18% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 36% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Front Grip': ['+ 30% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 6% Movement Speed', '+ 6% Shooting Move Speed', '+ 6% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 10% Vertical Recoil Control', '+ 40% Horizontal Recoil Control',
                          '- 16% Shooting Move Speed'],
        'VDV Speed Grip': ['+ 3% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                           '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 20% Magazine Ammo Capacity', '+ 20% Max Starting Ammo', '+ 20% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Taped Mags': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 20% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 20% Max Starting Ammo',
                      '+ 20% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'Bakelite Mag': ['+ 40% Magazine Ammo Capacity', '+ 40% Max Starting Ammo', '+ 40% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'GRU Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'VDV Fast Mag': ['+ 40% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 40% Max Starting Ammo',
                         '+ 40% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Field Grip': ['+ 20% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Pad': ['+ 30% Sprint to Fire Time', '+ 45% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class M16(Marksman):
    name = 'M16'
    temp_name = 'Base M16'
    damage_1 = 50.0
    damage_2 = 50.0
    damage_3 = 40.0
    range_1 = 21.59
    range_2 = 44.0
    fire_rate = 389.0
    velocity = 725.0
    shoot_speed = 6.77
    sprint_to_fire = 425.0
    vertical_recoil = 390.0
    horizontal_recoil = 80.0
    centering_speed = 12.5
    mag_capacity = 30.0
    reload = 2.7
    starting_ammo = 90.0
    ammo_capacity = 180.0
    burst = 3.0
    pap_burst = 2.0
    gun_acc_value = 0.53
    gun_critical_value = 0.49
    muzzle = {
        'Muzzle Brake': ['+ 10% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Silencer': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 25% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                              '- 30% Bullet Velocity'],
    }
    barrel = {
        'Rapid Fire': ['+ 7% Rate of Fire'],
        'Titanium': ['+ 13% Fire Rate', '- 25% Effective Damage Range'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Strike Team': ['+ 14% Damage', '+ 9% Fire Rate', '- 25% Effective Damage Range', '- 10% Idle Sway Control'],
        'Match Grade': ['+ 100% Bullet Velocity', '- 6% Sprinting Move Speed'],
        'Task Force': ['+ 14% Damage', '+ 50% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    stock = {
        'Tactical Stock': ['+ 65% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'Buffer Tube': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 78% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Aug(Marksman):
    name = 'Aug'
    temp_name = 'Base Aug'
    damage_1 = 52.0
    damage_2 = 52.0
    damage_3 = 38.0
    range_1 = 19.05
    range_2 = 50.0
    fire_rate = 408.0
    velocity = 775.0
    shoot_speed = 6.26
    sprint_to_fire = 425.0
    vertical_recoil = 420.0
    horizontal_recoil = 166.5
    centering_speed = 11.0
    mag_capacity = 30.0
    reload = 2.7
    starting_ammo = 90.0
    ammo_capacity = 180
    burst = 3.0
    gun_acc_value = 0.58
    gun_critical_value = 0.49
    muzzle = {
        'Muzzle Brake': ['+ 10% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Silencer': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 25% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                              '- 30% Bullet Velocity'],
    }
    barrel = {
        'Rapid Fire': ['+ 9% Rate of Fire'],
        'Titanium': ['+ 14% Fire Rate', '- 25% Effective Damage Range'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Strike Team': ['+ 14% Damage', '+ 11% Fire Rate', '- 25% Effective Damage Range', '- 10% Idle Sway Control'],
        'Match Grade': ['+ 100% Bullet Velocity', '- 6% Sprinting Move Speed'],
        'Task Force': ['+ 12% Damage', '+ 40% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'CQB Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 60% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Dmr(Marksman):
    name = 'DMR'
    temp_name = 'Base DMR'
    damage_1 = 58.0
    damage_2 = 58.0
    damage_3 = 50.0
    range_1 = 50.8
    range_2 = 62.0
    fire_rate = 400.0
    velocity = 700.0
    shoot_speed = 8.12
    sprint_to_fire = 400.0
    ads = 325.0
    vertical_recoil = 351.0
    horizontal_recoil = 270.0
    centering_speed = 8.0
    mag_capacity = 20.0
    reload = 2.5
    starting_ammo = 60.0
    ammo_capacity = 120.0
    burst = 1.0
    gun_acc_value = 0.81
    gun_critical_value = 0.60
    muzzle = {
        'Muzzle Brake': ['+ 10% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Silencer': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 25% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                           '- 30% Bullet Velocity'],
    }
    barrel = {
        'Rapid Fire': ['+ 9% Rate of Fire'],
        'Titanium': ['+ 21% Fire Rate', '- 25% Effective Damage Range'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Strike Team': ['+ 24% Damage', '+ 13% Fire Rate', '- 25% Effective Damage Range', '- 10% Idle Sway Control'],
        'Match Grade': ['+ 100% Bullet Velocity', '- 6% Sprinting Move Speed'],
        'Task Force': ['+ 24% Damage', '+ 100% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control'],
    }
    magazine = {
        'RND': ['+ 60% Magazine Ammo Capacity', '+ 60% Max Starting Ammo', '+ 60% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 60% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 60% Max Starting Ammo',
                      '+ 60% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 76% Magazine Ammo Capacity', '+ 76% Max Starting Ammo', '+ 76% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 76% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 76% Max Starting Ammo',
                           '+ 76% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Carv(Marksman):
    name = 'CARV'
    temp_name = 'Base CARV'
    damage_1 = 39.0
    damage_2 = 35.0
    damage_3 = 35.0
    range_1 = 45.72
    range_2 = 0.0
    fire_rate = 540.0
    velocity = 605.0
    shoot_speed = 6.77
    sprint_to_fire = 300.0
    vertical_recoil = 270.0
    horizontal_recoil = 100.0
    centering_speed = 11.0
    mag_capacity = 45.0
    reload = 2.5
    starting_ammo = 135.0
    ammo_capacity = 270.0
    burst = 3.0
    pap_burst = 2.0
    gun_acc_value = 0.35
    gun_critical_value = 0.36
    muzzle = {
        'Muzzle Brake': ['+ 10% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Silencer': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 25% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 15% Vertical Recoil Control',
                              '- 30% Bullet Velocity'],
    }
    barrel = {
        'Rapid Fire': ['+ 8% Rate of Fire'],
        'Titanium': ['+ 16% Fire Rate', '- 25% Effective Damage Range'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Strike Team': ['+ 5% Damage', '+ 13% Fire Rate', '- 25% Effective Damage Range', '- 10% Idle Sway Control'],
        'Match Grade': ['+ 100% Bullet Velocity', '- 6% Sprinting Move Speed'],
        'Task Force': ['+ 8% Damage', '+ 33% Effective Damage Range', '+ 50% Bullet Velocity',
                       '- 10% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
    }
    stock = {
        'Tactical Stock': ['+ 20% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'CQB Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    magazine = {
        'RND': ['+ 20% Magazine Ammo Capacity', '+ 20% Max Starting Ammo', '+ 20% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Jungle-Style Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 47% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 47% Max Starting Ammo',
                      '+ 47% Ammo Capacity', '- 20% Aim Down Sights Time'],
        'STANAG Mag': ['+ 40% Magazine Ammo Capacity', '+ 40% Max Starting Ammo', '+ 40% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'SAS Mag Clamp': ['+ 35% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 35% Reload Quickness', '+ 67% Max Starting Ammo',
                           '+ 67% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }


class Lmg(Weapon):
    damage_2 = 0.0
    range_1 = 25.4
    range_2 = 0.0
    movement = 10.26
    sprint = 13.08
    shoot_speed = 6.26
    sprint_to_fire = 450.0
    aim_walking = 2.75
    idle_sway = 15.0
    hip_fire = 7.5
    mag_capacity = 75.0
    ammo_capacity = 450.0
    long_shot = 41.0
    critical = 4.0
    weapon_type = 'LMG'
    muzzle = {
        'Muzzle Brake': ['+ 8% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 25% Effective Damage Range',
                       '- 15% Bullet Velocity'],
        'Infantry Compensator': ['+ 15% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 12% Vertical Recoil Control',
                              '- 30% Effective Damage Range', '- 25% Bullet Velocity'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 20% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Field Agent Grip': ['+ 8% Vertical Recoil Control', '+ 30% Horizontal Recoil Control',
                             '- 9% Shooting Move Speed'],
        'SFOD Speed Grip': ['+ 12% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 4% Movement Speed',
                            '- 4% Shooting Move Speed', '- 4% Aim Walking Movement Speed'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Stoner(Lmg):
    name = 'Stoner'
    temp_name = 'Base Stoner'
    damage_1 = 38.0
    damage_3 = 32.0
    range_1 = 21.59
    fire_rate = 722.0
    velocity = 714.0
    ads = 633.0
    vertical_recoil = 378.0
    horizontal_recoil = 240.0
    centering_speed = 14.0
    reload = 6.0
    starting_ammo = 225.0
    gun_acc_value = 0.56
    gun_critical_value = 0.53
    barrel = {
        'Cut Down': ['+ 25% Shooting Move Speed'],
        'Division': ['+ 35% Shooting Move Speed', '+ 8% Damage', '- 12% Effective Damage Range',
                     '- 12% Horizontal Recoil Control'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'SOR Cut Down': ['+ 50% Shooting Move Speed', '- 35% Effective Damage Range'],
        'Match Grade': ['+ 50% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 8% Damage', '+ 100% Effective Damage Range', '+ 41% Bullet Velocity',
                       '- 38% Max Starting Ammo', '- 7% Ammo Capacity', '- 7% Magazine Ammo Capacity'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 25% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 20% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 33% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time',
                                '- 5% Movement Speed', '- 5% Shooting Move Speed', '- 5% Aim Walking Movement Speed',
                                '- 5% Sprinting Move Speed'],
        'Salvo Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 67% Max Starting Ammo',
                           '+ 67% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 40% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 15% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 75% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Rpd(Lmg):
    name = 'RPD'
    temp_name = 'Base RPD'
    damage_1 = 42.0
    damage_3 = 34.0
    fire_rate = 652.0
    velocity = 684.0
    sprint = 13.69
    aim_walking = 3.28
    ads = 600.0
    vertical_recoil = 351.0
    horizontal_recoil = 100.0
    centering_speed = 15.0
    mag_capacity = 50.0
    reload = 7.0
    starting_ammo = 150.0
    ammo_capacity = 300.0
    gun_acc_value = 0.76
    gun_critical_value = 0.53
    muzzle = {
        'Muzzle Brake': ['+ 8% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 25% Effective Damage Range',
                       '- 15% Bullet Velocity'],
        'Spetsnaz Compensator': ['+ 15% Vertical Recoil Control', '- 10% Horizontal Recoil Control'],
        'KGB Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                           '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 12% Vertical Recoil Control',
                           '- 30% Effective Damage Range', '- 25% Bullet Velocity'],
    }
    barrel = {
        'Cut Down': ['+ 25% Shooting Move Speed'],
        'Division': ['+ 35% Shooting Move Speed', '+ 5% Damage', '- 15% Effective Damage Range',
                     '- 12% Horizontal Recoil Control'],
        'RPK': ['+ 50% Armour Damage'],
        'GRU Cut Down': ['+ 50% Shooting Move Speed', '- 35% Effective Damage Range'],
        'Match Grade': ['+ 50% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 5% Damage', '+ 100% Effective Damage Range', '+ 44% Bullet Velocity',
                       '- 39% Max Starting Ammo', '- 8% Ammo Capacity', '- 8% Magazine Ammo Capacity'],
    }
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'KGB Target Designator': ['+ 60% Reveal Distance'],
        'GRU 5mw Laser Sight': ['+ 40% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Fore grip': ['+ 20% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Spetsnaz Grip': ['+ 8% Vertical Recoil Control', '+ 30% Horizontal Recoil Control',
                          '- 9% Shooting Move Speed'],
        'VDV Speed Grip': ['+ 12% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 4% Movement Speed',
                           '- 4% Shooting Move Speed', '- 4% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 33% Reload Quickness'],
        'Speed Mag': ['+ 50% Magazine Ammo Capacity', '+ 27% Reload Quickness', '+ 50% Max Starting Ammo',
                      '+ 50% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'Spetsnaz Mag': ['+ 100% Magazine Ammo Capacity', '+ 100% Max Starting Ammo', '+ 100% Ammo Capacity',
                         '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 37% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time',
                                '- 5% Movement Speed', '- 5% Shooting Move Speed', '- 5% Aim Walking Movement Speed',
                                '- 5% Sprinting Move Speed'],
        'Salvo Fast Mag': ['+ 100% Magazine Ammo Capacity', '+ 33% Reload Quickness', '+ 100% Max Starting Ammo',
                           '+ 100% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'Spetsnaz Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'GRU Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                             '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Tactical Stock': ['+ 40% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 15% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'Spetsnaz PKM Stock': ['+ 10% Shooting Move Speed', '+ 75% Aim Walking Movement Speed',
                               '- 15% Hip Fire Accuracy'],
        'KGB Skeletal Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed',
                               '- 30% Hip Fire Accuracy'],
    }


class M60(Lmg):
    name = 'M60'
    temp_name = 'Base M60'
    damage_1 = 50.0
    damage_3 = 44.0
    fire_rate = 517.0
    velocity = 791.0
    ads = 683.0
    vertical_recoil = 350.0
    horizontal_recoil = 300.0
    centering_speed = 9.0
    reload = 7.4
    starting_ammo = 225.0
    gun_acc_value = 0.63
    gun_critical_value = 0.49
    barrel = {
        'Cut Down': ['+ 25% Shooting Move Speed'],
        'Division': ['+ 35% Shooting Move Speed', '+ 10% Damage', '- 15% Effective Damage Range',
                     '- 12% Horizontal Recoil Control'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'SOR Cut Down': ['+ 50% Shooting Move Speed', '- 35% Effective Damage Range'],
        'Match Grade': ['+ 50% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 10% Damage', '+ 100% Effective Damage Range', '+ 39% Bullet Velocity',
                       '- 38% Max Starting Ammo', '- 7% Ammo Capacity', '- 7% Magazine Ammo Capacity'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 30% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time',
                                '- 5% Movement Speed', '- 5% Shooting Move Speed', '- 5% Aim Walking Movement Speed',
                                '- 5% Sprinting Move Speed'],
        'Salvo Fast Mag': ['+ 67% Magazine Ammo Capacity', '+ 30% Reload Quickness', '+ 67% Max Starting Ammo',
                           '+ 67% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 40% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 15% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 75% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Mg82(Lmg):
    name = 'Mg82'
    temp_name = 'Base Mg82'
    damage_1 = 30.0
    damage_3 = 25.0
    fire_rate = 909.0
    velocity = 603.0
    ads = 583.0
    vertical_recoil = 300.0
    horizontal_recoil = 165.0
    centering_speed = 14.0
    reload = 8.0
    starting_ammo = 300.0
    hip_fire = 7.0
    mag_capacity = 100.0
    ammo_capacity = 600.0
    gun_acc_value = 0.37
    gun_critical_value = 0.59
    barrel = {
        'Cut Down': ['+ 25% Shooting Move Speed'],
        'Division': ['+ 35% Shooting Move Speed', '+ 10% Damage', '- 15% Effective Damage Range',
                     '- 12% Horizontal Recoil Control'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'SOR Cut Down': ['+ 50% Shooting Move Speed', '- 35% Effective Damage Range'],
        'Match Grade': ['+ 50% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 10% Damage', '+ 100% Effective Damage Range', '+ 38% Bullet Velocity',
                       '- 38% Max Starting Ammo', '- 7% Ammo Capacity', '- 7% Magazine Ammo Capacity'],
    }
    magazine = {
        'RND': ['+ 25% Magazine Ammo Capacity', '+ 25% Max Starting Ammo', '+ 25% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 25% Reload Quickness'],
        'Speed Mag': ['+ 25% Magazine Ammo Capacity', '+ 30% Reload Quickness', '+ 25% Max Starting Ammo',
                      '+ 25% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 45% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time',
                                '- 5% Movement Speed', '- 5% Shooting Move Speed', '- 5% Aim Walking Movement Speed',
                                '- 5% Sprinting Move Speed'],
        'Salvo Fast Mag': ['+ 50% Magazine Ammo Capacity', '+ 45% Reload Quickness', '+ 50% Max Starting Ammo',
                           '+ 50% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 40% Aim Walking Movement Speed'],
        'Marathon Stock': ['+ 15% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 75% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }


class Sniper(Weapon):
    damage_1 = 110.0
    damage_2 = 0.0
    damage_3 = 0.0
    range_1 = 127.0
    range_2 = 0.0
    movement = 10.26
    sprint = 14.49
    shoot_speed = 5.13
    sprint_to_fire = 450.0
    aim_walking = 3.28
    idle_sway = 4.0
    hip_fire = 18.0
    mag_capacity = 5.0
    reload = 3.0
    starting_ammo = 20.0
    ammo_capacity = 30.0
    long_shot = 51.0
    critical = 4.5
    weapon_type = 'Sniper'
    body = {
        'Steady Aim Laser': ['+ 30% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 50% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 40% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    under_barrel = {
        'Front Grip': ['+ 30% Vertical Recoil Control', '+ 30% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Bipod': ['+ 50% Vertical Recoil Control', '+ 50% Horizontal Recoil Control', '- 5% Sprinting Move Speed'],
        'SFOD Speed Grip': ['+ 5% Sprinting Move Speed', '+ 25% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    magazine = {
        'RND': ['+ 40% Magazine Ammo Capacity', '+ 40% Max Starting Ammo', '+ 40% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 25% Reload Quickness'],
        'Speed Mag': ['+ 40% Magazine Ammo Capacity', '+ 30% Reload Quickness', '+ 40% Max Starting Ammo',
                      '+ 40% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 80% Magazine Ammo Capacity', '+ 80% Max Starting Ammo', '+ 80% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 80% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 80% Max Starting Ammo',
                           '+ 80% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 5% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 50% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 8% Aim Down Sight Time', '+ 67% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 10% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 5% Aim Down Sight Time', '+ 25% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 15% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Pelington(Sniper):
    name = 'Pelington'
    temp_name = 'Base Pelington'
    fire_rate = 54.0
    velocity = 500.0
    ads = 550.0
    vertical_recoil = 550.0
    horizontal_recoil = 250.0
    centering_speed = 2.5
    reload = 5.1
    gun_acc_value = 1.00
    gun_critical_value = 0.59
    critical = 5.0
    muzzle = {
        'Stabilizer': ['+ 18% Idle Sway Control'],
        'Flash Hider': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Moderator': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Stabilizer': ['+ 47% Idle Sway Control', '- 20% Aim Down Sight Time'],
        'Task Force Shroud': ['+ 30% Increased Equipment Drop Chance', '+ 35% Idle Sway Control',
                              '- 40% Shooting Move Speed', '- 25% Aim Down Sight Time'],
        'Wrapped Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 8% Vertical Recoil Control',
                               '+ 29% Idle Sway Control', '- 20% Aim Down Sight Time', '- 25% Bullet Velocity'],
    }
    barrel = {
        'Extended': ['+ 17% Bullet Velocity'],
        'Reinforced Heavy': ['+ 11% Fire Rate', '+ 30% Bullet Velocity', '- 20% Aim Walking Movement Speed',
                             '- 15% Idle Sway Control'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Combat Recon': ['+ 43% Bullet Velocity', '- 20% Idle Sway Control'],
        'Ultralight': ['+ 10% Strafe Speed', '- 20% Bullet Velocity'],
        'Tiger Team': ['+ 14% Reload Quickness', '+ 20% Damage', '+ 13% Fire Rate', '+ 30% Bullet Velocity',
                       '- 20% Magazine Ammo Capacity', '- 36% Max Starting Ammo', '- 20% Ammo Capacity'],
    }
    magazine = {
        'RND': ['+ 40% Magazine Ammo Capacity', '+ 40% Max Starting Ammo', '+ 40% Ammo Capacity',
                '- 20% Reload Quickness'],
        'Fast Loader': ['+ 30% Reload Quickness'],
        'Speed Mag': ['+ 40% Magazine Ammo Capacity', '+ 10% Reload Quickness', '+ 40% Max Starting Ammo',
                      '+ 40% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 80% Magazine Ammo Capacity', '+ 80% Max Starting Ammo', '+ 80% Ammo Capacity',
                       '- 55% Reload Quickness', '- 5% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 37% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 80% Magazine Ammo Capacity', '+ 5% Reload Quickness', '+ 80% Max Starting Ammo',
                           '+ 80% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 25% Aim Walking Movement Speed'],
        'CQB Pad': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'Marathon Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 72% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    handle = {
        'Speed Tape': ['+ 5% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 50% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 8% Aim Down Sight Time', '+ 67% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 10% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 5% Aim Down Sight Time', '+ 25% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 15% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Lw3(Sniper):
    name = 'LW3'
    temp_name = 'Base LW3'
    fire_rate = 47.0
    velocity = 580.0
    ads = 650.0
    vertical_recoil = 550.0
    horizontal_recoil = 350.0
    centering_speed = 20.0
    gun_acc_value = 1.00
    gun_critical_value = 0.58
    critical = 4.0
    muzzle = {
        'Stabilizer': ['+ 14% Idle Sway Control'],
        'Flash Hider': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Moderator': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Stabilizer': ['+ 35% Idle Sway Control', '- 20% Aim Down Sight Time'],
        'Task Force Shroud': ['+ 30% Increased Equipment Drop Chance', '+ 29% Idle Sway Control',
                              '- 40% Shooting Move Speed', '- 25% Aim Down Sight Time'],
        'Wrapped Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 8% Vertical Recoil Control',
                               '+ 21% Idle Sway Control', '- 20% Aim Down Sight Time', '- 25% Bullet Velocity'],
    }
    barrel = {
        'Extended': ['+ 18% Bullet Velocity'],
        'Rapid Fire': ['+ 11% Fire Rate'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Combat Recon': ['+ 36% Bullet Velocity', '- 20% Idle Sway Control'],
        'Hammer Forge': ['+ 30% Fire Rate', '- 15% Idle Sway Control'],
        'Tiger Team': ['+ 20% Damage', '+ 21% Fire Rate', '+ 27% Bullet Velocity', '- 20% Magazine Ammo Capacity',
                       '- 40% Max Starting Ammo', '- 20% Ammo Capacity'],
    }
    stock = {
        'Tactical Stock': ['+ 25% Aim Walking Movement Speed'],
        'CQB Pad': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'Marathon Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    handle = {
        'Speed Tape': ['+ 5% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 33% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 50% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 8% Aim Down Sight Time', '+ 67% Flinch Resistance', '- 15% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 10% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 5% Aim Down Sight Time', '+ 25% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 15% Shooting Movement Speed', '- 18% Sprint to Fire Time'],
    }


class M82(Sniper):
    name = 'M82'
    temp_name = 'Base M82'
    fire_rate = 72.0
    velocity = 731.0
    ads = 666.0
    vertical_recoil = 672.0
    horizontal_recoil = 320.0
    centering_speed = 7.5
    gun_acc_value = 1.00
    gun_critical_value = 0.54
    muzzle = {
        'Stabilizer': ['+ 12% Idle Sway Control'],
        'Flash Hider': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Moderator': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Stabilizer': ['+ 50% Idle Sway Control', '- 20% Aim Down Sight Time'],
        'Task Force Shroud': ['+ 30% Increased Equipment Drop Chance', '+ 38% Idle Sway Control',
                              '- 40% Shooting Move Speed', '- 25% Aim Down Sight Time'],
        'Wrapped Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 8% Vertical Recoil Control',
                               '+ 25% Idle Sway Control', '- 20% Aim Down Sight Time', '- 25% Bullet Velocity'],
    }
    barrel = {
        'Extended': ['+ 13% Bullet Velocity'],
        'Rapid Fire': ['+ 12% Fire Rate'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Combat Recon': ['+ 26% Bullet Velocity', '- 20% Idle Sway Control'],
        'Ultralight': ['+ 10% Strafe Speed', '- 15% Bullet Velocity'],
        'Tiger Team': ['+ 20% Damage', '+ 24% Fire Rate', '+ 20% Bullet Velocity', '- 20% Magazine Ammo Capacity',
                       '- 40% Max Starting Ammo', '- 20% Ammo Capacity'],
    }
    under_barrel = {
        'Front Grip': ['+ 10% Vertical Recoil Control', '+ 10% Horizontal Recoil Control'],
        'Infiltrator Grip': ['+ 5% Movement Speed', '+ 5% Shooting Move Speed', '+ 5% Aim Walking Movement Speed'],
        'Patrol Grip': ['+ 6% Sprinting Move Speed'],
        'Bruiser Grip': ['+ 40% Melee Quickness', '+ 3% Movement Speed', '+ 3% Shooting Move Speed',
                         '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed'],
        'Bipod': ['+ 20% Vertical Recoil Control', '+ 20% Horizontal Recoil Control', '- 5% Sprinting Move Speed'],
        'SFOD Speed Grip': ['+ 5% Sprinting Move Speed', '+ 15% Horizontal Recoil Control', '- 6% Movement Speed',
                            '- 6% Shooting Move Speed', '- 6% Aim Walking Movement Speed'],
    }
    stock = {
        'Tactical Stock': ['+ 25% Aim Walking Movement Speed'],
        'Marathon Pad': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'CQB Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Pad': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    handle = {
        'Speed Tape': ['+ 5% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 50% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 8% Aim Down Sight Time', '+ 67% Flinch Resistance', '- 15% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 10% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 5% Aim Down Sight Time', '+ 25% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 15% Shooting Movement Speed', '- 18% Sprint to Fire Time'],
    }


class Swiss(Sniper):
    name = 'Swiss'
    temp_name = 'Base Swiss'
    fire_rate = 60.0
    velocity = 684.0
    ads = 600.0
    vertical_recoil = 429.0
    horizontal_recoil = 231.0
    centering_speed = 2.5
    gun_acc_value = 0.81
    gun_critical_value = 0.33
    mag_capacity = 6.0
    reload = 2.8
    starting_ammo = 24.0
    ammo_capacity = 36.0
    muzzle = {
        'Stabilizer': ['+ 20% Idle Sway Control'],
        'Flash Hider': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Moderator': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Bullet Velocity'],
        'Infantry Stabilizer': ['+ 60% Idle Sway Control', '- 20% Aim Down Sight Time'],
        'Task Force Shroud': ['+ 30% Increased Equipment Drop Chance', '+ 40% Idle Sway Control',
                              '- 40% Shooting Move Speed', '- 25% Aim Down Sight Time'],
        'GRU Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 8% Vertical Recoil Control',
                           '+ 30% Idle Sway Control', '- 20% Aim Down Sight Time', '- 25% Bullet Velocity'],
    }
    barrel = {
        'Extended': ['+ 16% Bullet Velocity'],
        'Rapid Fire': ['+ 15% Fire Rate'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Combat Recon': ['+ 31% Bullet Velocity', '- 20% Idle Sway Control'],
        'Ultralight': ['+ 10% Strafe Speed', '- 20% Bullet Velocity'],
        'Tiger Team': ['+ 20% Damage', '+ 33% Fire Rate', '+ 23% Bullet Velocity', '- 17% Magazine Ammo Capacity',
                       '- 38% Max Starting Ammo', '- 17% Ammo Capacity'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Loader': ['+ 25% Reload Quickness'],
        'Speed Mag': ['+ 17% Magazine Ammo Capacity', '+ 30% Reload Quickness', '+ 17% Max Starting Ammo',
                      '+ 17% Ammo Capacity', '- 5% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 50% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 50% Max Starting Ammo',
                           '+ 50% Ammo Capacity', '- 10% Aim Down Sight Time'],
    }
    stock = {
        'Tactical Stock': ['+ 25% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 30% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 10% Shooting Move Speed', '+ 50% Aim Walking Movement Speed',
                             '- 15% Hip Fire Accuracy'],
        'Raider Stock': ['+ 30% Sprint to Fire Time', '+ 40% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy'],
    }
    handle = {
        'Speed Tape': ['+ 5% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 50% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 8% Aim Down Sight Time', '+ 67% Flinch Resistance', '- 11% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 10% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 5% Aim Down Sight Time', '+ 25% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 15% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Pistol(Weapon):
    damage_2 = 0.0
    range_2 = 0.0
    movement = 10.8
    sprint = 15.38
    shoot_speed = 10.26
    sprint_to_fire = 300.0
    aim_walking = 9.67
    ads = 225.0
    horizontal_recoil = 120.0
    idle_sway = 120.0
    long_shot = 25.0
    weapon_type = 'Pistol'
    muzzle = {
        'Muzzle Brake': ['+ 5% Vertical Recoil Control'],
        'Flash Guard': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 15% Effective Damage Range'],
        'Infantry Compensator': ['+ 12% Vertical Recoil Control', '- 8% Horizontal Recoil Control'],
        'SOCOM Eliminator': ['+ 30% Increased Equipment Drop Chance', '+ 17% Vertical Recoil Control',
                             '- 10% Shooting Move Speed', '- 10% Horizontal Recoil Control'],
        'Agency Suppressor': ['+ 35% Increased Equipment Drop Chance', '+ 8% Vertical Recoil Control',
                              '- 25% Effective Damage Range'],
    }
    body = {
        'Steady Aim Laser': ['+ 15% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 35% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 25% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }
    stock = {
        'Dual Wield': ['+ 100% Damage']
    }


class N1911(Pistol):
    name = '1911'
    temp_name = 'Base 1911'
    damage_1 = 50.0
    damage_3 = 40.0
    range_1 = 19.05
    fire_rate = 400.0
    velocity = 206.0
    ads = 200.0
    vertical_recoil = 231.0
    centering_speed = 4.0
    hip_fire = 6.5
    mag_capacity = 8.0
    reload = 1.8
    starting_ammo = 24.0
    ammo_capacity = 48.0
    gun_acc_value = 0.58
    gun_critical_value = 0.36
    critical = 4.2
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Chrome': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 30% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Tac Ops': ['+ 60% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 12% Damage', '+ 40% Effective Damage Range', '+ 120% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 30% Vertical Recoil Control', '- 20% Horizontal Recoil Control'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 50% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 50% Max Starting Ammo',
                      '+ 50% Ammo Capacity', '- 15% Aim Down Sights Time'],
        'STANAG Mag': ['+ 75% Magazine Ammo Capacity', '+ 75% Max Starting Ammo', '+ 75% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 75% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 75% Max Starting Ammo',
                           '+ 75% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }


class Magnum(Pistol):
    name = 'Magnum'
    temp_name = 'Base Magnum'
    damage_1 = 75.0
    damage_3 = 49.0
    range_1 = 25.4
    fire_rate = 180.0
    velocity = 313.0
    shoot_speed = 9.41
    sprint_to_fire = 275.0
    vertical_recoil = 200.0
    horizontal_recoil = 200.0
    centering_speed = 2.0
    hip_fire = 6.5
    mag_capacity = 6.0
    reload = 6.3
    starting_ammo = 24.0
    ammo_capacity = 36.0
    gun_acc_value = 0.75
    gun_critical_value = 0.51
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Chrome': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 30% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Tight Snub': ['+ 21% Damage', '+ 50% Armour Damage', '- 30% Effective Damage Range',
                       '- 33% Horizontal Recoil Control'],
        'Task Force': ['+ 17% Damage', '+ 40% Effective Damage Range', '+ 120% Bullet Velocity',
                       '- 25% Max Starting Ammo', '- 30% Vertical Recoil Control', '- 20% Horizontal Recoil Control'],
    }
    magazine = {
        'RND': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                '- 33% Reload Quickness'],
        'Fast Mag': ['+ 57% Reload Quickness'],
        'Speed Mag': ['+ 50% Magazine Ammo Capacity', '+ 56% Reload Quickness', '+ 50% Max Starting Ammo',
                      '+ 50% Ammo Capacity', '- 15% Aim Down Sights Time'],
        'STANAG Mag': ['+ 100% Magazine Ammo Capacity', '+ 100% Max Starting Ammo', '+ 100% Ammo Capacity',
                       '- 67% Reload Quickness', '- 5% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 68% Reload Quickness', '+ 25% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 100% Magazine Ammo Capacity', '+ 65% Reload Quickness', '+ 100% Max Starting Ammo',
                           '+ 100% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }


class Diamatti(Pistol):
    name = 'Diamatti'
    temp_name = 'Base Diamatti'
    damage_1 = 30.0
    damage_3 = 25.0
    range_1 = 21.59
    fire_rate = 576.0
    velocity = 257.0
    vertical_recoil = 168.0
    centering_speed = 8.0
    hip_fire = 7.0
    mag_capacity = 15.0
    reload = 1.7
    starting_ammo = 45.0
    ammo_capacity = 90.0
    burst = 3.0
    gun_acc_value = 0.64
    gun_critical_value = 0.48
    critical = 4.5
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Chrome': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 30% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Tac Ops': ['+ 60% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 13% Damage', '+ 40% Effective Damage Range', '+ 120% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 30% Vertical Recoil Control', '- 20% Horizontal Recoil Control'],
    }
    magazine = {
        'RND': ['+ 60% Magazine Ammo Capacity', '+ 60% Max Starting Ammo', '+ 60% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 60% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 60% Max Starting Ammo',
                      '+ 60% Ammo Capacity', '- 15% Aim Down Sights Time'],
        'STANAG Mag': ['+ 100% Magazine Ammo Capacity', '+ 100% Max Starting Ammo', '+ 100% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 100% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 100% Max Starting Ammo',
                           '+ 100% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }


class Amp(Pistol):
    name = 'Amp'
    temp_name = 'Base Amp'
    damage_1 = 33.0
    damage_3 = 27.0
    range_1 = 19.05
    fire_rate = 652.0
    velocity = 200.0
    vertical_recoil = 180.0
    horizontal_recoil = 180.0
    centering_speed = 7.0
    hip_fire = 7.5
    mag_capacity = 15.0
    reload = 2.0
    starting_ammo = 45.0
    ammo_capacity = 90.0
    burst = 1.0
    gun_acc_value = 0.40
    gun_critical_value = 0.47
    critical = 4.5
    barrel = {
        'Extended': ['+ 40% Bullet Velocity'],
        'Chrome': ['+ 100% Bullet Velocity', '- 25% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 30% Effective Damage Range', '+ 80% Bullet Velocity', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Takedown': ['+ 60% Effective Damage Range', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 3% Damage', '+ 40% Effective Damage Range', '+ 120% Bullet Velocity',
                       '- 33% Max Starting Ammo', '- 30% Vertical Recoil Control', '- 20% Horizontal Recoil Control'],
    }
    magazine = {
        'RND': ['+ 33% Magazine Ammo Capacity', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity',
                '- 10% Reload Quickness'],
        'Fast Mag': ['+ 20% Reload Quickness'],
        'Speed Mag': ['+ 33% Magazine Ammo Capacity', '+ 25% Reload Quickness', '+ 33% Max Starting Ammo',
                      '+ 33% Ammo Capacity', '- 15% Aim Down Sights Time'],
        'STANAG Mag': ['+ 67% Magazine Ammo Capacity', '+ 67% Max Starting Ammo', '+ 67% Ammo Capacity',
                       '- 10% Reload Quickness', '- 15% Aim Down Sight Time'],
        'Vandal Speed Loader': ['+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '- 6% Aim Down Sight Time'],
        'Salvo Fast Mag': ['+ 47% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 47% Max Starting Ammo',
                           '+ 47% Ammo Capacity', '- 25% Aim Down Sight Time'],
    }


class Shotgun(Weapon):
    damage_2 = 0.0
    damage_3 = 0.0
    range_2 = 0.0
    velocity = 850.0
    movement = 10.8
    sprint = 14.8
    shoot_speed = 9.66
    sprint_to_fire = 400.0
    aim_walking = 8.55
    ads = 250.0
    idle_sway = 35.0
    hip_fire = 8.0
    long_shot = 14.0
    weapon_type = 'Shotgun'
    body = {
        'Steady Aim Laser': ['+ 20% Hip Fire Accuracy'],
        'Mounted Flashlight': ['+ 17.5% Increased Salvage Drop Rate'],
        'SOF Target Designator': ['+ 60% Reveal Distance'],
        'SWAT 5mw Laser Sight': ['+ 35% Hip Fire Accuracy', '- 8% Aim Down Sight Time'],
        'Tiger Team Spotlight': ['+ 22.5% Increased Salvage Drop Rate', '- 10% Sprint to Fire Time'],
        'Ember Sighting Point': ['+ 30% Increased Salvage Drop Rate', '+ 30% Hip Fire Accuracy',
                                 '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time'],
    }
    handle = {
        'Speed Tape': ['+ 10% Aim Down Sight Time'],
        'Drop Shot Tape': ['+ 50% Flinch Resistance', '+ Aim While Going Prone'],
        'Field Tape': ['+ 90% Flinch Resistance'],
        'SASR Jungle Grip': ['+ 15% Aim Down Sight Time', '+ 80% Flinch Resistance', '- 12% Sprint to Fire Time'],
        'Serpent Wrap': ['+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time'],
        'Airborne Elastic Wrap': ['+ 30% Aim Down Sight Time', '+ 90% Flinch Resistance', '+ Aim While Going Prone',
                                  '- 10% Shooting Movement Speed', '- 15% Sprint to Fire Time'],
    }


class Hauer(Shotgun):
    name = 'Hauer'
    temp_name = 'Base Hauer'
    damage_1 = 159.0
    range_1 = 6.35
    fire_rate = 66.0
    vertical_recoil = 750.0
    horizontal_recoil = 150.0
    centering_speed = 2.5
    mag_capacity = 5.0
    reload = 4.5
    starting_ammo = 20.0
    ammo_capacity = 30.0
    gun_acc_value = 0.33
    gun_critical_value = 0.28
    muzzle = {
        'Duckbill Choke': ['+ 50% Wider Pellet Spread'],
        'Flash Cone': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 12% Effective Damage Range'],
        'Infantry V-Choke': ['+ 70% Tighter Pellet Spread'],
        'SOCOM Blast Mitigator': ['+ 30% Increased Equipment Drop Chance', '- 15% Shooting Move Speed',
                                  '- 20% Sprint to Fire Time'],
        'Agency Choke': ['+ 35% Increased Equipment Drop Chance', '+ 10% Hip Fire Accuracy',
                         '+ 55% Tighter Pellet Spread', '- 15% Sprint to Fire Time', '- 17% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 12% Effective Damage Range'],
        'Ranger': ['+ 30% Effective Damage Range', '- 35% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 12% Effective Damage Range', '+ 6% Fire Rate', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Hammer Forge': ['+ 6% Fire Rate', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 15% Damage', '- 7% Effective Damage Range'],
    }
    magazine = {
        'RND': ['+ 20% Magazine Ammo Capacity', '+ 20% Max Starting Ammo', '+ 20% Ammo Capacity'],
        'STANAG Mag': ['+ 60% Magazine Ammo Capacity', '+ 60% Max Starting Ammo', '+ 60% Ammo Capacity',
                       '- 25% Reload Quickness'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Shotgun Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Pad': ['+ 5% Slide Speed'],
        'No Stock': ['+ 40% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 20% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Marathon Stock': ['+ 4% Sprinting Move Speed', '+ 10% Shooting Move Speed', '+ 25% Sprint to Fire Time',
                           '+ 10% Aim Walking Movement Speed', '- 20% Hip Fire Accuracy'],
    }


class Gallo(Shotgun):
    name = 'Gallo'
    temp_name = 'Base Gallo'
    damage_1 = 108.0
    range_1 = 5.72
    fire_rate = 189.0
    vertical_recoil = 450.0
    horizontal_recoil = 250.0
    centering_speed = 5.0
    mag_capacity = 7.0
    reload = 6.0
    starting_ammo = 28.0
    ammo_capacity = 42.0
    gun_acc_value = 0.42
    gun_critical_value = 0.30
    muzzle = {
        'Duckbill Choke': ['+ 50% Wider Pellet Spread'],
        'Flash Cone': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 13% Effective Damage Range'],
        'Infantry V-Choke': ['+ 67% Tighter Pellet Spread'],
        'SOCOM Blast Mitigator': ['+ 30% Increased Equipment Drop Chance', '- 15% Shooting Move Speed',
                                  '- 20% Sprint to Fire Time'],
        'Agency Choke': ['+ 35% Increased Equipment Drop Chance', '+ 10% Hip Fire Accuracy',
                         '+ 50% Tighter Pellet Spread', '- 15% Sprint to Fire Time', '- 18% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 12% Effective Damage Range'],
        'Ranger': ['+ 30% Effective Damage Range', '- 35% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 12% Effective Damage Range', '+ 15% Fire Rate', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Hammer Forge': ['+ 15% Fire Rate', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 52% Damage', '- 13% Effective Damage Range'],
    }
    magazine = {
        'RND': ['+ 29% Magazine Ammo Capacity', '+ 29% Max Starting Ammo', '+ 29% Ammo Capacity',
                '- 5% Reload Quickness'],
        'STANAG Mag': ['+ 71% Magazine Ammo Capacity', '+ 71% Max Starting Ammo', '+ 71% Ammo Capacity',
                       '- 34% Reload Quickness'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 40% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 20% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Marathon Stock': ['+ 4% Sprinting Move Speed', '+ 10% Shooting Move Speed', '+ 25% Sprint to Fire Time',
                           '+ 10% Aim Walking Movement Speed', '- 20% Hip Fire Accuracy'],
    }


class Streetsweeper(Shotgun):
    name = 'Streetsweeper'
    temp_name = 'Base Streetsweeper'
    damage_1 = 88.0
    range_1 = 5.08
    fire_rate = 300.0
    vertical_recoil = 350.0
    horizontal_recoil = 350.0
    centering_speed = 5.0
    mag_capacity = 12.0
    reload = 14.1
    starting_ammo = 36.0
    ammo_capacity = 72.0
    gun_acc_value = 0.42
    gun_critical_value = 0.33
    muzzle = {
        'Duckbill Choke': ['+ 50% Wider Pellet Spread'],
        'Flash Cone': ['+ 17.5% Increased Equipment Drop Chance'],
        'Sound Suppressor': ['+ 22.5% Increased Equipment Drop Chance', '- 12% Effective Damage Range'],
        'Infantry V-Choke': ['+ 75% Tighter Pellet Spread'],
        'SOCOM Blast Mitigator': ['+ 30% Increased Equipment Drop Chance', '- 15% Shooting Move Speed',
                                  '- 20% Sprint to Fire Time'],
        'Agency Choke': ['+ 35% Increased Equipment Drop Chance', '+ 10% Hip Fire Accuracy',
                         '+ 55% Tighter Pellet Spread', '- 15% Sprint to Fire Time', '- 17% Effective Damage Range'],
    }
    barrel = {
        'Extended': ['+ 13% Effective Damage Range'],
        'Ranger': ['+ 30% Effective Damage Range', '- 35% Aim Walking Movement Speed'],
        'Cavalry Lancer': ['+ 50% Armour Damage'],
        'Reinforced Heavy': ['+ 13% Effective Damage Range', '+ 9% Fire Rate', '- 4% Sprinting Move Speed',
                             '- 15% Aim Walking Movement Speed'],
        'Hammer Forge': ['+ 9% Fire Rate', '- 5% Sprinting Move Speed'],
        'Task Force': ['+ 27% Damage', '- 13% Effective Damage Range'],
    }
    magazine = {
        'RND': ['+ 25% Magazine Ammo Capacity', '+ 25% Max Starting Ammo', '+ 25% Ammo Capacity',
                '- 11% Reload Quickness'],
        'STANAG Mag': ['+ 50% Magazine Ammo Capacity', '+ 50% Max Starting Ammo', '+ 50% Ammo Capacity',
                       '- 32% Reload Quickness'],
    }
    stock = {
        'Tactical Stock': ['+ 10% Aim Walking Movement Speed'],
        'Wire Stock': ['+ 10% Sprint to Fire Time'],
        'Duster Stock': ['+ 5% Slide Speed'],
        'No Stock': ['+ 40% Sprint to Fire Time', '- 15% Hip Fire Accuracy'],
        'SAS Combat Stock': ['+ 5% Shooting Move Speed', '+ 20% Aim Walking Movement Speed', '- 15% Hip Fire Accuracy'],
        'Marathon Stock': ['+ 4% Sprinting Move Speed', '+ 10% Shooting Move Speed', '+ 25% Sprint to Fire Time',
                           '+ 10% Aim Walking Movement Speed', '- 20% Hip Fire Accuracy'],
    }
