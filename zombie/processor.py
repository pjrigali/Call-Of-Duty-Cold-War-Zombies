# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:09:41 2021

@author: Peter
"""
import pandas as pd
import numpy as np
from numpy.random import normal
from typing import List
import zombie.weapon_stats as w
from dataclasses import dataclass


@dataclass
class Build:
    """
    Get weapon stat values.

    Applies buffs from weapon and perk tiers. Then saves the information in a class object.

    Parameters
    ----------
    weapon_class_levels : dict, default None
        User input tiers for each weapon class. Use str value betweem 0 and 5.
    perk_class_levels : dict, default None
        User input tiers for each perk. Use str value value between 0 and 5.

    Returns
    -------
    class object

    Examples
    --------
    By default the values are set to 0. User inputs change these and the effects are applied across the weapons:

    >>> from zombie.processor import Build
    >>> weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
    >>>                        'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    >>> perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
    >>> build = Build(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels)

    """
    def __init__(self, weapon_class_levels: dict = None, perk_class_levels: dict = None):
        self.weapon_class_levels = weapon_class_levels
        self.perk_class_levels = perk_class_levels

        if perk_class_levels['deadshot'] == '5':
            self.consecutive: bool = True
        else:
            self.consecutive: bool = False

        self.stats = {'XM4': w.Xm4,
                      'AK47': w.Ak47,
                      'Krig': w.Krig,
                      'QBZ': w.Qbz,
                      'FFAR': w.Ffar,
                      'Groza': w.Groza,
                      'FARA': w.Fara,
                      'C58': w.C58,
                      'EM2': w.Em2,
                      'MP5': w.Mp5,
                      'Milano': w.Milano,
                      'AK74u': w.Ak74u,
                      'KSP': w.Ksp,
                      'Bullfrog': w.Bullfrog,
                      'Mac 10': w.Mac10,
                      'LC10': w.Lc10,
                      'PPSH': w.Ppsh,
                      'OTS': w.Ots9,
                      'Tec9': w.Tec9,
                      'Type 63': w.Type63,
                      'M16': w.M16,
                      'AUG': w.Aug,
                      'DMR': w.Dmr,
                      'CARV': w.Carv,
                      'Stoner': w.Stoner,
                      'RPD': w.Rpd,
                      'M60': w.M60,
                      'Pellington': w.Pelington,
                      'LW3': w.Lw3,
                      'M82': w.M82,
                      'Swiss': w.Swiss,
                      '1911': w.N1911,
                      'Magnum': w.Magnum,
                      'Diamatti': w.Diamatti,
                      'AMP': w.Amp,
                      'Hauer': w.Hauer,
                      'Gallo': w.Gallo,
                      'Streetsweeper': w.Streetsweeper
                      }
        self.gun_names = list(self.stats.keys())
        self.rare_level = {'common': 1.00, 'green': 1.50, 'blue': 3.00, 'purple': 6.00, 'orange': 12.00}
        self.pack_level = {'0': 1.00, '1': 2.00, '2': 4.00, '3': 8.00}
        self._weapon_type_dict = {'Launcher': {'elites': 1.00, 'Armour Damage': 1.00, 'ammo': 1.00},
                                  'Special': {'elites': 1.00, 'Armour Damage': 1.00, 'ammo': 1.00},
                                  'Smg': {'Close': 1.00, 'Crit': 1.00, 'Attachments': 5},
                                  'Shotgun': {'Close': 1.00, 'Crit': 1.00, 'Armour Damage': 1.00},
                                  'Pistol': {'Close': 1.00, 'Crit': 1.00, 'Armour Damage': 1.00},
                                  'Marksman': {'Long': 1.00, 'Crit': 1.00, 'Attachments': 5},
                                  'Sniper': {'Armour Damage': 1.00, 'Crit': 1.00, 'Attachments': 5},
                                  'Lmg': {'Armour Damage': 1.00, 'Crit': 1.00, 'Attachments': 5},
                                  'Assault': {'Long': 1.00, 'Crit': 1.00, 'Attachments': 5},
                                  'Melee': {'object': 'gun butt', 'Damage': 1.00, 'regen': 0}}
        self.weapon_tier_inputs = {'Launcher': '0', 'Special': '0', 'Smg': '0', 'Shotgun': '0', 'Pistol': '0',
                                   'Marksman': '0', 'Sniper': '0', 'Lmg': '0', 'Assault': '0', 'Melee': '0'}
        self._perk_dict = {'speed': {'swap': 0, 'field recharge': 0, 'reload': 1.15, 'barr. and myst.': 0,
                                     'fire and reload': 0},
                           'stamin up': {'movement': 1.07, 'sprint': 1.07, 'back pedal': 1.00, 'fall damage': 0,
                                         'aim walking': 1.00, 'equipment': 1.00, 'sprint falloff': 0},
                           'deadshot': {'scope sway': 0, 'critical1': 1.00, 'armour': 1.00, 'hip fire spread': 1.00,
                                        'critical': 1.00, 'consecutive': 1},
                           'death_perception': {'minimap': 0, 'indicators': 0, 'Salvage': 1.00, 'Armour Damage': 1.00,
                                                'chests': 0}}
        self.perk_tier_inputs = {'speed': '0', 'stamin up': '0', 'deadshot': '0', 'death_perception': '0'}
        self.col_lst = ['Name', 'Temp Name', 'Damage', 'Damage 2', 'Damage 3', 'Range',
                        'Range 2', 'Fire Rate', 'Velocity', 'Armour Damage', 'Melee Quickness',
                        'Movement Speed', 'Sprinting Speed', 'Shooting Speed', 'Sprint to Fire',
                        'Aim Walking', 'ADS', 'Vertical Recoil', 'Horizontal Recoil',
                        'Centering Speed', 'Idle Sway', 'Flinch', 'Hip Fire', 'Mag Capacity',
                        'Reload', 'Ammo Capacity', 'Accuracy', 'Critical', 'Pack', 'Rare',
                        'Shoot To Reload Ratio', 'Movement Ratio', 'Control Ratio', 'Drop Off Ratio']

        def _shot_distribution(stats=self.stats.values()) -> np.ndarray:
            acc = [val.gun_acc_value for val in stats]
            acc_n = [val for val in acc if val != 0]
            sig1 = np.around(np.std(acc_n), 3)
            mu1 = np.around(np.mean(acc_n), 3)
            return np.around(normal(mu1, sig1, 2500), 3)

        self._hits = _shot_distribution()

        def _set_weapon_class(weapon_type: str, weapon_tier: str) -> None:

            if weapon_type == 'Launcher':
                launchers = {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                                  '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                                  '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                                  '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                                  '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                                  }[weapon_tier]
                self._weapon_type_dict['Launcher'] = launchers
            elif weapon_type == 'Special':
                specials = {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                                 '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                                 '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                                 '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                                 '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                                 }[weapon_tier]
                self._weapon_type_dict['Special'] = specials
            elif weapon_type == 'Smg':
                smgs = {'1': {'Close': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Close': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Close': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[weapon_tier]
                self._weapon_type_dict['Smg'] = smgs
            elif weapon_type == 'Shotgun':
                shotguns = {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                                 '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                                 '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                                 '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                                 '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                                 }[weapon_tier]
                self._weapon_type_dict['Shotgun'] = shotguns
            elif weapon_type == 'Pistol':
                pistols = {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                                '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                                '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                                '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                                '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                                }[weapon_tier]
                self._weapon_type_dict['Pistol'] = pistols
            elif weapon_type == 'Marksman':
                tact = {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[weapon_tier]
                self._weapon_type_dict['Marksman'] = tact
            elif weapon_type == 'Sniper':
                snipers = {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                                '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                                '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                                '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                                '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                                }[weapon_tier]
                self._weapon_type_dict['Sniper'] = snipers
            elif weapon_type == 'Lmg':
                lmgs = {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[weapon_tier]
                self._weapon_type_dict['Lmg'] = lmgs
            elif weapon_type == 'Assault':
                assault = {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                                '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                                '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                                '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                                '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                                }[weapon_tier]
                self._weapon_type_dict['Assault'] = assault
            elif weapon_type == 'Melee':
                melee = {'1': {'object': 'knife', 'Damage': 1.00, 'regen': 0},
                              '2': {'object': 'knife', 'Damage': 1.10, 'regen': 0},
                              '3': {'object': 'bowie', 'Damage': 1.10, 'regen': 0},
                              '4': {'object': 'bowie', 'Damage': 1.25, 'regen': 0},
                              '5': {'object': 'bowie', 'Damage': 1.25, 'regen': 1}
                              }[weapon_tier]
                self._weapon_type_dict['Melee'] = melee
            self.weapon_tier_inputs[weapon_type] = weapon_tier

        for i, j in enumerate(self._weapon_type_dict.keys()):
            _set_weapon_class(j, weapon_class_levels[j])

        def _set_perk_class(perk_type: str, perk_tier: str) -> None:

            if perk_type == 'speed':
                speed = {'1': {'swap': 1, 'field recharge': 1, 'Reload': 0.85, 'barr. and myst.': 0,
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
                self._perk_dict['speed'] = speed
            elif perk_type == 'stamin up':
                stamin = {'1': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
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
                self._perk_dict['stamin up'] = stamin
            elif perk_type == 'deadshot':
                dead = {'1': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.00, 'Hip Fire': 1.00,
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
                self._perk_dict['deadshot'] = dead
            elif perk_type == 'death_perception':
                death = {'1': {'minimap': 0, 'indicators': 0, 'Salvage': 1.00, 'Armour Damage': 1.00, 'chests': 0},
                             '2': {'minimap': 0, 'indicators': 0, 'Salvage': 1.00, 'Armour Damage': 1.00, 'chests': 0},
                             '3': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.00, 'chests': 0},
                             '4': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.25, 'chests': 0},
                             '5': {'minimap': 0, 'indicators': 0, 'Salvage': 1.20, 'Armour Damage': 1.25, 'chests': 0}
                             }[perk_tier]
                self._perk_dict['death_perception'] = death

            self.perk_tier_inputs[perk_type] = perk_tier

        for i, j in enumerate(self._perk_dict.keys()):
            _set_perk_class(j, perk_class_levels[j])

    def __repr__(self):
        return "Build"

    @property
    def get_weapon_classes(self) -> dict:
        """Returns user input weapon tier levels"""
        return self._weapon_type_dict

    @property
    def get_perk_classes(self) -> dict:
        """Returns user input perk tier levels"""
        return self._perk_dict

    @property
    def hits(self) -> np.ndarray:
        """Return hit distribution"""
        return self._hits

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    def _process(self, weapon: str, nickname: str = None, equipped_attachments: dict = None, rarity: str = None,
                 pap: str = None, accuracy: float = None, critical: float = None) -> dict:
        d = self.stats[weapon]
        dic_i = {'Name': d.name,
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

        if nickname is not None:
            dic_i['Temp Name'] = nickname

        if accuracy is not None:
            dic_i['Accuracy'] = accuracy

        if critical is not None:
            dic_i['Critical'] = critical

        dic_i['Damage'] = dic_i['Damage']
        dic_i['Damage 2'] = dic_i['Damage 2']
        dic_i['Damage 3'] = dic_i['Damage 3']
        dic_i['Mag Capacity'] = dic_i['Mag Capacity']

        if rarity is not None:
            dic_i['Rare'] = rarity
            dic_i['Damage'] = dic_i['Damage'] * self.rare_level[rarity]
            dic_i['Damage 2'] = dic_i['Damage 2'] * self.rare_level[rarity]
            dic_i['Damage 3'] = dic_i['Damage 3'] * self.rare_level[rarity]

        if pap is not None:
            if pap != '0':
                dic_i['Pack'] = pap
                dic_i['Damage'] = dic_i['Damage'] * self.pack_level[pap] * dic_i['PAP Burst']
                dic_i['Damage 2'] = dic_i['Damage 2'] * self.pack_level[pap] * dic_i['PAP Burst']
                dic_i['Damage 3'] = dic_i['Damage 3'] * self.pack_level[pap] * dic_i['PAP Burst']
                dic_i['Mag Capacity'] = dic_i['Mag Capacity'] / dic_i['PAP Burst']

        temp_dic = self._apply_multipliers(weapon_multi=self.get_weapon_classes, perk_multi=self.get_perk_classes,
                                           weapon_dic=dic_i)

        if equipped_attachments is not None:
            effect_lst = self._get_attachments(weapon_dic=temp_dic, equipped_dic=equipped_attachments)
            final_dic = self._apply_attachments(weapon_dic=temp_dic, attachment_lst=effect_lst)

            for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
                if part in equipped_attachments.keys():
                    final_dic[part] = {equipped_attachments[part]: final_dic[part][equipped_attachments[part]]}
                else:
                    final_dic[part] = {'None': 'None'}
            temp_dic = final_dic

        return temp_dic
