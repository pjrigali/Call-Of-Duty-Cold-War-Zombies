# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:09:41 2021

@author: Peter
"""
from typing import Optional, List
from dataclasses import dataclass
import pandas as pd
import numpy as np
from numpy.random import normal
from zombie.weapon_stats import _weapon_stats_dic, _gun_names

rare_level = {'common': 1.00,
              'green': 1.50,
              'blue': 3.00,
              'purple': 6.00,
              'orange': 12.00,
              }

pack_level = {'0': 1.00,
              '1': 2.00,
              '2': 4.00,
              '3': 8.00,
              }

_weapon_type_dict = {'Launcher': {'elites': 1.00,
                                  'Armour Damage': 1.00,
                                  'ammo': 1.00},
                     'Special': {'elites': 1.00,
                                 'Armour Damage': 1.00,
                                 'ammo': 1.00},
                     'Smg': {'Close': 1.00,
                             'Crit': 1.00,
                             'Attachments': 5},
                     'Shotgun': {'Close': 1.00,
                                 'Crit': 1.00,
                                 'Armour Damage': 1.00},
                     'Pistol': {'Close': 1.00,
                                'Crit': 1.00,
                                'Armour Damage': 1.00},
                     'Marksman': {'Long': 1.00,
                                  'Crit': 1.00,
                                  'Attachments': 5},
                     'Sniper': {'Armour Damage': 1.00,
                                'Crit': 1.00,
                                'Attachments': 5},
                     'Lmg': {'Armour Damage': 1.00,
                             'Crit': 1.00,
                             'Attachments': 5},
                     'Assault': {'Long': 1.00,
                                 'Crit': 1.00,
                                 'Attachments': 5},
                     'Melee': {'object': 'gun butt',
                               'Damage': 1.00,
                               'regen': 0}
                     }

_perk_type_dict = {'speed': {'swap': 0,
                             'field recharge': 0,
                             'reload': 1.15,
                             'barr. and myst.': 0,
                             'fire and reload': 0},
                   'stamin up': {'movement': 1.07,
                                 'sprint': 1.07,
                                 'back pedal': 1.00,
                                 'fall damage': 0,
                                 'aim walking': 1.00,
                                 'equipment': 1.00,
                                 'sprint falloff': 0},
                   'deadshot': {'scope sway': 0,
                                'critical1': 1.00,
                                'armour': 1.00,
                                'hip fire spread': 1.00,
                                'critical': 1.00,
                                'consecutive': 1},
                   'death_perception': {'minimap': 0,
                                        'indicators': 0,
                                        'Salvage': 1.00,
                                        'Armour Damage': 1.00,
                                        'chests': 0},
                   }


def _shot_distribution(stats) -> np.ndarray:
    acc = [val.gun_acc_value for val in stats]
    acc_n = [val for val in acc if val != 0]
    sig1 = np.around(np.std(acc_n), 3)
    mu1 = np.around(np.mean(acc_n), 3)
    return np.around(normal(mu1, sig1, 2500), 3)


def _set_weapon_class(weapon_type: str, weapon_tier: str) -> dict:
    if weapon_type == 'Launcher':
        return {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                }[weapon_tier]
    elif weapon_type == 'Special':
        return {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                }[weapon_tier]
    elif weapon_type == 'Smg':
        return {'1': {'Close': 1.10, 'Crit': 1.00, 'Attachments': 1},
                '2': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1},
                '3': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                '4': {'Close': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                '5': {'Close': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                }[weapon_tier]
    elif weapon_type == 'Shotgun':
        return {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                }[weapon_tier]
    elif weapon_type == 'Pistol':
        return {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                }[weapon_tier]
    elif weapon_type == 'Marksman':
        return {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                }[weapon_tier]
    elif weapon_type == 'Sniper':
        return {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                }[weapon_tier]
    elif weapon_type == 'Lmg':
        return {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                }[weapon_tier]
    elif weapon_type == 'Assault':
        return {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                }[weapon_tier]
    elif weapon_type == 'Melee':
        return {'1': {'object': 'knife', 'Damage': 1.00, 'regen': 0},
                '2': {'object': 'knife', 'Damage': 1.10, 'regen': 0},
                '3': {'object': 'bowie', 'Damage': 1.10, 'regen': 0},
                '4': {'object': 'bowie', 'Damage': 1.25, 'regen': 0},
                '5': {'object': 'bowie', 'Damage': 1.25, 'regen': 1}
                }[weapon_tier]


def _set_perk_class(perk_type: str, perk_tier: str) -> dict:
    if perk_type == 'speed':
        return {'1': {'swap': 1, 'field recharge': 1, 'Reload': 0.85, 'barr. and myst.': 0,
                      'Shooting Speed': 1.00},
                '2': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.85, 'barr. and myst.': 0,
                      'Shooting Speed': 1.00},
                '3': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 0,
                      'Shooting Speed': 1.00},
                '4': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 1,
                      'Shooting Speed': 1.00},
                '5': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 1,
                      'Shooting Speed': 1.07}
                }[perk_tier]
    elif perk_type == 'stamin up':
        return {'1': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
                      'fall damage': 0, 'Aim Walking': 1.00, 'equipment': 1.00, 'sprint falloff': 0,
                      'Shooting Speed': 1.07},
                '2': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
                      'fall damage': 1, 'Aim Walking': 1.00, 'equipment': 1.00, 'sprint falloff': 0,
                      'Shooting Speed': 1.07},
                '3': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
                      'fall damage': 1, 'Aim Walking': 1.07, 'equipment': 1.00, 'sprint falloff': 0,
                      'Shooting Speed': 1.07},
                '4': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
                      'fall damage': 1, 'Aim Walking': 1.07, 'equipment': 1.07, 'sprint falloff': 0,
                      'Shooting Speed': 1.07},
                '5': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
                      'fall damage': 1, 'Aim Walking': 1.07, 'equipment': 1.07, 'sprint falloff': 1,
                      'Shooting Speed': 1.07}
                }[perk_tier]
    elif perk_type == 'deadshot':
        return {'1': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.00, 'Hip Fire': 1.00,
                      'Crit': 1.00, 'consecutive': 0},
                '2': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 1.00,
                      'Crit': 1.00, 'consecutive': 0},
                '3': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                      'Crit': 1.00, 'consecutive': 0},
                '4': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                      'Crit': 1.10, 'consecutive': 0},
                '5': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                      'Crit': 1.10, 'consecutive': 1}
                }[perk_tier]
    elif perk_type == 'death_perception':
        return {'1': {'minimap': 0, 'indicators': 0, 'Salvage': 1.00, 'Armour Damage': 1.00, 'chests': 0},
                '2': {'minimap': 0, 'indicators': 0, 'Salvage': 1.00, 'Armour Damage': 1.00, 'chests': 0},
                '3': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.00, 'chests': 0},
                '4': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.25, 'chests': 0},
                '5': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.25, 'chests': 0}
                }[perk_tier]


def _apply_multipliers(weapon_multi: dict, perk_multi: dict, weapon_dic: dict) -> dict:
    dn = weapon_dic.copy()
    # Weapons
    for j in weapon_multi[dn['Weapon Type']]:
        dn[j] = round(dn[j] * weapon_multi[dn['Weapon Type']][j], 2)

    # Perks
    for i in dn.keys():
        for j in perk_multi.keys():
            for k in perk_multi[j].keys():
                if i == k:
                    dn[i] = round(dn[i] * perk_multi[j][k], 2)

    return dn


def _apply_attachments(weapon_dic: dict, attachment_lst: List[str]) -> dict:

    if weapon_dic['Pack'] != '0':
        pack_mag = True
    else:
        pack_mag = False

    dn = weapon_dic.copy()
    dm = {i: 0.0 for i in weapon_dic.keys()}
    for i in attachment_lst:
        if i == 'None':
            continue
        else:
            at = i.split('%')[0]
            at_value = at.split(' ')[1].strip()
            at_pos = at.split(' ')[0].strip()
            val = float(at_value) / 100

        if '% Damage' in i:
            dm['Damage'] += val
            dm['Damage 2'] += val
            dm['Damage 3'] += val
            continue
        elif 'Effective Damage Range' in i:
            if at_pos == '+':
                dm['Range'] += val
                dm['Range 2'] += val
                continue
            else:
                dm['Range'] -= val
                dm['Range 2'] -= val
                continue
        elif 'Rate of Fire' in i:
            if at_pos == '+':
                dm['Fire Rate'] += val
                continue
            else:
                dm['Fire Rate'] -= val
                continue
        elif 'Fire Rate' in i:
            if at_pos == '+':
                dm['Fire Rate'] += val
                continue
            else:
                dm['Fire Rate'] -= val
                continue
        elif 'Bullet Velocity' in i:
            if at_pos == '+':
                dm['Velocity'] += val
                continue
            else:
                dm['Velocity'] -= val
                continue
        elif 'Armour Damage' in i:
            dm['Armour Damage'] += val
            continue
        elif 'Melee Quickness' in i:
            dm['Melee Quickness'] -= val
            continue
        elif 'Sprinting Move Speed' in i:
            if at_pos == '+':
                dm['Sprinting Speed'] += val
                continue
            else:
                dm['Sprinting Speed'] -= val
                continue
        elif 'Shooting Move Speed' in i:
            if at_pos == '+':
                dm['Shooting Speed'] += val
                continue
            else:
                dm['Shooting Speed'] -= val
                continue
        elif 'Sprint to Fire Time' in i:
            if at_pos == '+':
                dm['Sprint to Fire'] -= val
                continue
            else:
                dm['Sprint to Fire'] += val
                continue
        elif 'Aim Walking Movement Speed' in i:
            if at_pos == '+':
                dm['Aim Walking'] += val
                continue
            else:
                dm['Aim Walking'] -= val
                continue
        elif 'Movement Speed' in i:
            if at_pos == '+':
                dm['Movement Speed'] += val
                continue
            else:
                dm['Movement Speed'] -= val
                continue
        elif 'Aim Down Sight Time' in i:
            if at_pos == '-':
                dm['ADS'] += val
                continue
            else:
                dm['ADS'] -= val
                continue
        elif 'Vertical Recoil Control' in i:
            if at_pos == '+':
                dm['Vertical Recoil'] -= val
                continue
            else:
                dm['Vertical Recoil'] += val
                continue
        elif 'Horizontal Recoil Control' in i:
            if at_pos == '+':
                dm['Horizontal Recoil'] -= val
                continue
            else:
                dm['Horizontal Recoil'] += val
                continue
        elif 'Flinch Resistance' in i:
            if at_pos == '+':
                dm['Flinch'] -= val
                continue
            else:
                dm['Flinch'] += val
                continue
        elif 'Hip Fire Accuracy' in i:
            if at_pos == '+':
                dm['Hip Fire'] -= val
                continue
            else:
                dm['Hip Fire'] += val
                continue
        elif 'Magazine Ammo Capacity' in i:
            if at_pos == '+':
                dm['Mag Capacity'] += val
                continue
            else:
                dm['Mag Capacity'] -= val
                continue
        elif 'Reload Quickness' in i:
            if at_pos == '+':
                dm['Reload'] -= val
                continue
            else:
                dm['Reload'] += val
                continue
        elif 'Max Starting Ammo' in i:
            if at_pos == '+':
                dm['Starting Ammo'] += val
                continue
            else:
                dm['Starting Ammo'] -= val
                continue
        elif '% Ammo Capacity' in i:
            if at_pos == '+':
                dm['Ammo Capacity'] += val
                continue
            else:
                dm['Ammo Capacity'] -= val
                continue
        elif 'Increased Salvage Drop Rate' in i:
            dm['Salvage'] += val
            continue
        elif 'Increased Equipment Drop Chance' in i:
            dm['Equipment'] += val
            continue
        else:
            print('Attachment Processor Missed: ', i, at_value, at_pos)

    ind_lst = [
        'Damage',
        'Damage 2',
        'Damage 3',
        'Range',
        'Range 2',
        'Fire Rate',
        'Velocity',
        'Armour Damage',
        'Melee Quickness',
        'Sprinting Speed',
        'Shooting Speed',
        'Sprint to Fire',
        'Aim Walking',
        'Movement Speed',
        'ADS',
        'Vertical Recoil',
        'Horizontal Recoil',
        'Flinch',
        'Hip Fire',
        'Mag Capacity',
        'Reload',
        'Starting Ammo',
        'Ammo Capacity',
        'Salvage',
        'Equipment',
    ]

    for i in dm.keys():
        if i in ind_lst:
            dn[i] = round(float(dn[i]) * (1.00 + dm[i]), 2)

    if pack_mag:
        dn['Mag Capacity'] = dn['Mag Capacity'] * 2
        dn['Ammo Capacity'] = dn['Ammo Capacity'] * 2

    return dn


def _get_attachments(weapon_dic: dict, equipped_dic: dict = None):
    location = []
    name = []
    effect = []
    for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
        for j in weapon_dic[part].keys():
            location.append(part)
            name.append(j)
            effect.append(weapon_dic[part][j])

    df = pd.DataFrame()
    df['location'] = location
    df['name'] = name
    df['effect'] = effect

    if equipped_dic:
        temp_lst = []
        for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
            if part in equipped_dic.keys():
                temp_lst.append(weapon_dic[part][equipped_dic[part]])
        return sum(temp_lst, [])
    else:
        return df


@dataclass
class DamageProfile:
    """

    Builds a DamageProfile Class, which holds weapon and perk class levels to be applied later on.

    :param weapon_class_levels: Dict of weapon types and tier level.
    :type weapon_class_levels: dict
    :param perk_class_levels: Dict of perk type and tier level.
    :type perk_class_levels: dict
    :param max_range: Maximum range for calculations, default is 100. *Optional*
    :type max_range: int
    :example:
        >>> # User inputs
        >>> weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
        >>>                        'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
        >>> perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
        >>> # Core Classes
        >>> damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
        >>>                                max_range=100)
    :note: *None*

    """
    def __init__(self, weapon_class_levels: dict, perk_class_levels: dict, max_range: Optional[int]):
        self._weapon_class_levels = weapon_class_levels
        self._perk_class_levels = perk_class_levels
        self._max_range = max_range
        self._hits = _shot_distribution(stats=_weapon_stats_dic.values())

        self._weapon_type_dict = {}
        for i, j in enumerate(_weapon_type_dict.keys()):
            self._weapon_type_dict[j] = _set_weapon_class(j, self._weapon_class_levels[j])

        self._perk_dict = {}
        for i, j in enumerate(_perk_type_dict.keys()):
            self._perk_dict[j] = _set_perk_class(j, self._perk_class_levels[j])

        if perk_class_levels['deadshot'] == '5':
            self._consecutive = True
        else:
            self._consecutive = False

    def __repr__(self):
        return "DamageProfile"

    @property
    def hits(self) -> np.ndarray:
        """Returns hit value multipliers to account for accuracy and critical hit percentages."""
        return self._hits

    @property
    def get_weapon_classes(self) -> dict:
        """Returns user input weapon tier levels"""
        return self._weapon_type_dict

    @property
    def get_perk_classes(self) -> dict:
        """Returns user input perk tier levels"""
        return self._perk_dict

    @property
    def consecutive(self) -> bool:
        """Returns a bool value representing if consecutive shots used"""
        return self._consecutive

    @property
    def max_range(self) -> int:
        """Max distance for calculations"""
        return self._max_range


@dataclass
class ModifiedWeapon:
    """

    Builds a ModifiedWeapon Class, which holds default and modified weapon stats.

    :param weapon_name: Name of the weapon.
    :type weapon_name: str
    :param weapon_class_levels: Dict of weapon types and tier level.
    :type weapon_class_levels: dict
    :param perk_class_levels: Dict of perk type and tier level.
    :type perk_class_levels: dict
    :param nickname: User input name for the weapon.
    :type nickname: str
    :param equipped_attachments: Dict of weapon attachment location and attachment name.
    :type equipped_attachments: dict
    :param rarity: Rarity color.
    :type rarity: str
    :param pap: Pack a punch level.
    :type pap: str
    :param accuracy: Accuracy percent with the weapon.
    :type accuracy: float
    :param critical: Critical hit percent with the weapon.
    :type critical: float
    :example:

    :note:

    """

    def __init__(self,
                 weapon_name: str,
                 weapon_class_levels: dict,
                 perk_class_levels: dict,
                 nickname: Optional[str] = None,
                 equipped_attachments: Optional[dict] = None,
                 rarity: Optional[str] = None,
                 pap: Optional[str] = None,
                 accuracy: Optional[float] = None,
                 critical: Optional[float] = None):
        self._pap = pap
        self._rarity = rarity
        self._perk_class_levels = perk_class_levels
        self._weapon_class_levels = weapon_class_levels
        d = _weapon_stats_dic[weapon_name]
        self._default_stats = {'Name': d.name,
                               'Temp Name': d.temp_name,
                               'Damage': d.damage_1,
                               'Damage 2': d.damage_2,
                               'Damage 3': d.damage_3,
                               'Range': d.range_1,
                               'Range 2': d.range_2,
                               'Fire Rate': d.fire_rate,
                               'Velocity': d.velocity,
                               'Armour Damage': d.armour_damage,
                               'Melee Quickness': d.melee,
                               'Movement Speed': d.movement,
                               'Sprinting Speed': d.sprint,
                               'Shooting Speed': d.shoot_speed,
                               'Sprint to Fire': d.sprint_to_fire,
                               'Aim Walking': d.aim_walking,
                               'ADS': d.ads,
                               'Vertical Recoil': d.vertical_recoil,
                               'Horizontal Recoil': d.horizontal_recoil,
                               'Centering Speed': d.centering_speed,
                               'Idle Sway': d.idle_sway,
                               'Flinch': d.flinch,
                               'Hip Fire': d.hip_fire,
                               'Mag Capacity': d.mag_capacity,
                               'Reload': d.reload,
                               'Starting Ammo': d.starting_ammo,
                               'Ammo Capacity': d.ammo_capacity,
                               'Burst': d.burst,
                               'PAP Burst': d.pap_burst,
                               'Long Shot': d.long_shot,
                               'Crit': d.critical,
                               'Long': d.long,
                               'Close': d.close,
                               'Salvage': d.salvage,
                               'Equipment': d.equipment,
                               'Attachments': d.attachments,
                               'Weapon Type': d.weapon_type,
                               'Accuracy': d.gun_acc_value,
                               'Critical': d.gun_critical_value,
                               'Pack': d.pack,
                               'Rare': d.rare,
                               'Muzzle': d.muzzle,
                               'Barrel': d.barrel,
                               'Body': d.body,
                               'Underbarrel': d.under_barrel,
                               'Magazine': d.magazine,
                               'Handle': d.handle,
                               'Stock': d.stock,
                               }

        self._modified_stats = self._default_stats
        self._equipped_attachments = equipped_attachments

        if nickname is not None:
            self._modified_stats['Temp Name'] = nickname

        if accuracy is not None:
            self._modified_stats['Accuracy'] = accuracy

        if critical is not None:
            self._modified_stats['Critical'] = critical

        if rarity is not None:
            self._modified_stats['Rare'] = rarity
            for key in ['Damage', 'Damage 2', 'Damage 3']:
                self._modified_stats[key] = self._modified_stats[key] * rare_level[rarity]

        if pap is not None:
            if pap != '0':
                self._modified_stats['Pack'] = pap
                self._modified_stats['Mag Capacity'] = self._modified_stats['Mag Capacity'] / self._modified_stats['PAP Burst']
                for key in ['Damage', 'Damage 2', 'Damage 3']:
                    self._modified_stats[key] = self._modified_stats[key] * pack_level[pap] * self._modified_stats['PAP Burst']

        temp_dic = _apply_multipliers(weapon_multi=self._weapon_class_levels, perk_multi=self._perk_class_levels,
                                      weapon_dic=self._modified_stats)

        if equipped_attachments is not None:
            effect_lst = _get_attachments(weapon_dic=temp_dic, equipped_dic=equipped_attachments)
            final_dic = _apply_attachments(weapon_dic=temp_dic, attachment_lst=effect_lst)

            for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
                if part in equipped_attachments.keys():
                    final_dic[part] = {equipped_attachments[part]: final_dic[part][equipped_attachments[part]]}
                else:
                    final_dic[part] = {'None': 'None'}
            temp_dic = final_dic

        self._modified_stats = temp_dic

    def __repr__(self):
        return self._default_stats['Name']

    @property
    def pack_a_punch_level(self) -> str:
        """Returns pack a punch level"""
        return self._pap

    @property
    def rarity_level(self) -> str:
        """Returns rarity level"""
        return self._rarity

    @property
    def default_stats(self) -> dict:
        """Returns default stats for the weapon **before** perks, weapon tiers and attachments"""
        return self._default_stats

    @property
    def modified_stats(self) -> dict:
        """Returns default stats for the weapon **after** perks, weapon tiers and attachments"""
        return self._modified_stats

    @property
    def get_attachments(self) -> pd.DataFrame:
        """Returns attachments and effects as a DataFrame"""
        if self._equipped_attachments:
            vals = self._modified_stats
        else:
            vals = self._default_stats

        location, name, effect = [], [], []
        for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
            for j in vals[part].keys():
                location.append(part)
                name.append(j)
                effect.append(self.modified_stats[part][j])

        df = pd.DataFrame()
        df['location'] = location
        df['name'] = name
        df['effect'] = effect

        if self._equipped_attachments:
            df = df.set_index('location').loc[self._equipped_attachments.keys()]
        else:
            df = df.set_index('location').sort_index()
        return df
