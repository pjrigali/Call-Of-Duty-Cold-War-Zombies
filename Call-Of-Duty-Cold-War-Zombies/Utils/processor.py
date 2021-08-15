# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:09:41 2021

@author: Peter
"""
from pandas import DataFrame, concat
from typing import List
import Utils.weapon_stats as w
import Utils.analysis as a
aa = a.Analyze()


class Build:

    def __init__(self, weapon_class_levels, perk_class_levels):
        self.weapon_class_levels = weapon_class_levels
        self.perk_class_levels = perk_class_levels
        self.consecutive = True
        self.stats = {'XM4': w.Xm4,
                      'AK47': w.Ak47,
                      'Krig': w.Krig,
                      'QBZ': w.Qbz,
                      'FFAR': w.Ffar,
                      'Groza': w.Groza,
                      'FARA': w.Fara,
                      'MP5': w.Mp5,
                      'Milano': w.Milano,
                      'AK74u': w.Ak74u,
                      'KSP': w.Ksp,
                      'Bullfrog': w.Bullfrog,
                      'Mac 10': w.Mac10,
                      'LC10': w.Lc10,
                      'PPSH': w.Ppsh,
                      'OTS': w.Ots9,
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
        self.weapon_dict = {'Launcher': {'elites': 1.00, 'Armour Damage': 1.00, 'ammo': 1.00},
                            'Special': {'elites': 1.00, 'Armour Damage': 1.00, 'ammo': 1.00},
                            'Smg': {'Close': 1.00, 'Crit': 1.00, 'Attachments': 5},
                            'Shotgun': {'Close': 1.00, 'Crit': 1.00, 'Armour Damage': 1.00},
                            'Pistol': {'Close': 1.00, 'Crit': 1.00, 'Armour Damage': 1.00},
                            'Marksman': {'Long': 1.00, 'Crit': 1.00, 'Attachments': 5},
                            'Sniper': {'Armour Damage': 1.00, 'Crit': 1.00, 'Attachments': 5},
                            'Lmg': {'Armour Damage': 1.00, 'Crit': 1.00, 'Attachments': 5},
                            'Assault': {'Long': 1.00, 'Crit': 1.00, 'Attachments': 5},
                            'Melee': {'object': 'gun butt', 'Damage': 1.00, 'regen': 0}}
        self.weapon_lst = ['Launcher', 'Special', 'Smg', 'Shotgun', 'Pistol', 'Marksman', 'Sniper', 'Lmg', 'Assault',
                           'Melee']
        self.weapon_tier_inputs = {'Launcher': '0', 'Special': '0', 'Smg': '0', 'Shotgun': '0', 'Pistol': '0',
                                   'Marksman': '0', 'Sniper': '0', 'Lmg': '0', 'Assault': '0', 'Melee': '0'}
        self.perk_dict = {'speed': {'swap': 0, 'field recharge': 0, 'eload': 1.15, 'barr. and myst.': 0,
                                    'fire and reload': 0},
                          'stamin up': {'movement': 1.07, 'sprint': 1.07, 'back pedal': 1.00, 'fall damage': 0,
                                        'aim walking': 1.00, 'equipment': 1.00, 'sprint falloff': 0},
                          'deadshot': {'scope sway': 0, 'critical1': 1.00, 'armour': 1.00, 'hip fire spread': 1.00,
                                       'critical': 1.00, 'consecutive': 1}}
        self.perk_lst = ['speed', 'stamin up', 'deadshot']
        self.perk_tier_inputs = {'speed': '0', 'stamin up': '0', 'deadshot': '0'}

        def set_weapon_class(weapon_type: str, tier: str) -> None:

            if weapon_type == 'Launcher':
                self.launchers = {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                                  '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                                  '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                                  '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                                  '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                                  }[tier]
                self.weapon_dict['Launcher'] = self.launchers
            elif weapon_type == 'Special':
                self.specials = {'1': {'elites': 1.10, 'Armour Damage': 1.00, 'ammo': 1.00},
                                 '2': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 1.00},
                                 '3': {'elites': 1.10, 'Armour Damage': 1.10, 'ammo': 0.75},
                                 '4': {'elites': 1.25, 'Armour Damage': 1.10, 'ammo': 0.75},
                                 '5': {'elites': 1.25, 'Armour Damage': 1.25, 'ammo': 0.75}
                                 }[tier]
                self.weapon_dict['Special'] = self.specials
            elif weapon_type == 'Smg':
                self.smgs = {'1': {'Close': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Close': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Close': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Close': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[tier]
                self.weapon_dict['Smg'] = self.smgs
            elif weapon_type == 'Shotgun':
                self.shotguns = {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                                 '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                                 '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                                 '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                                 '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                                 }[tier]
                self.weapon_dict['Shotgun'] = self.shotguns
            elif weapon_type == 'Pistol':
                self.pistols = {'1': {'Close': 1.10, 'Crit': 1.00, 'Armour Damage': 1.00},
                                '2': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.00},
                                '3': {'Close': 1.10, 'Crit': 1.10, 'Armour Damage': 1.10},
                                '4': {'Close': 1.25, 'Crit': 1.10, 'Armour Damage': 1.10},
                                '5': {'Close': 1.25, 'Crit': 1.25, 'Armour Damage': 1.10}
                                }[tier]
                self.weapon_dict['Pistol'] = self.pistols
            elif weapon_type == 'Marksman':
                self.tact = {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[tier]
                self.weapon_dict['Marksman'] = self.tact
            elif weapon_type == 'Sniper':
                self.snipers = {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                                '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                                '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                                '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                                '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                                }[tier]
                self.weapon_dict['Sniper'] = self.snipers
            elif weapon_type == 'Lmg':
                self.lmgs = {'1': {'Armour Damage': 1.10, 'Crit': 1.00, 'Attachments': 1},
                             '2': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1},
                             '3': {'Armour Damage': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                             '4': {'Armour Damage': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                             '5': {'Armour Damage': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                             }[tier]
                self.weapon_dict['Lmg'] = self.lmgs
            elif weapon_type == 'Assault':
                self.assault = {'1': {'Long': 1.10, 'Crit': 1.00, 'Attachments': 1},
                                '2': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1},
                                '3': {'Long': 1.10, 'Crit': 1.10, 'Attachments': 1.6},
                                '4': {'Long': 1.25, 'Crit': 1.10, 'Attachments': 1.6},
                                '5': {'Long': 1.25, 'Crit': 1.25, 'Attachments': 1.6}
                                }[tier]
                self.weapon_dict['Assault'] = self.assault
            elif weapon_type == 'Melee':
                self.melee = {'1': {'object': 'knife', 'Damage': 1.00, 'regen': 0},
                              '2': {'object': 'knife', 'Damage': 1.10, 'regen': 0},
                              '3': {'object': 'bowie', 'Damage': 1.10, 'regen': 0},
                              '4': {'object': 'bowie', 'Damage': 1.25, 'regen': 0},
                              '5': {'object': 'bowie', 'Damage': 1.25, 'regen': 1}
                              }[tier]
                self.weapon_dict['Melee'] = self.melee
            self.weapon_tier_inputs[weapon_type] = tier

        for i, j in enumerate(self.weapon_lst):
            set_weapon_class(j, weapon_class_levels[i])

        def set_perk_class(perk_type: str, tier: str) -> None:

            if perk_type == 'speed':
                self.speed = {'1': {'swap': 1, 'field recharge': 1, 'Reload': 0.85, 'barr. and myst.': 0,
                                    'Shooting Speed': 1.00},
                              '2': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.85, 'barr. and myst.': 0,
                                    'Shooting Speed': 1.00},
                              '3': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 0,
                                    'Shooting Speed': 1.00},
                              '4': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 1,
                                    'Shooting Speed': 1.00},
                              '5': {'swap': 1, 'field recharge': 0.80, 'Reload': 0.70, 'barr. and myst.': 1,
                                    'Shooting Speed': 1.07}
                              }[tier]
                self.perk_dict['speed'] = self.speed
            elif perk_type == 'stamin up':
                self.stamin = {'1': {'Movement Speed': 1.07, 'Sprinting Speed': 1.07, 'back pedal': 1.07,
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
                               }[tier]
                self.perk_dict['stamin up'] = self.stamin
            elif perk_type == 'deadshot':
                self.dead = {'1': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.00, 'Hip Fire': 1.00,
                                   'Crit': 1.00, 'consecutive': 0},
                             '2': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 1.00,
                                   'Crit': 1.00, 'consecutive': 0},
                             '3': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                                   'Crit': 1.00, 'consecutive': 0},
                             '4': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                                   'Crit': 1.10, 'consecutive': 0},
                             '5': {'Idle Sway': 0, 'critical1': 2.00, 'Armour Damage': 1.50, 'Hip Fire': 0.70,
                                   'Crit': 1.10, 'consecutive': 1}
                             }[tier]
                self.perk_dict['deadshot'] = self.dead
            self.perk_tier_inputs[perk_type] = tier

        for i, j in enumerate(self.perk_lst):
            set_perk_class(j, perk_class_levels[i])

    def get_weapon_classes(self) -> dict:

        return self.weapon_dict

    def get_perk_classes(self) -> dict:

        return self.perk_dict

    # def set_weapons_perks(self, weapon_tiers, perk_tiers):
    #
    #     for i, j in enumerate(self.weapon_lst):
    #         self.set_weapon_class(j, weapon_tiers[i])
    #
    #     for i, j in enumerate(self.perk_lst):
    #         self.set_perk_class(j, perk_tiers[i])

    def apply_multipliers(self, weapon_multi: dict, perk_multi: dict, dic: dict) -> dict:

        dn = dic.copy()
        # Weapons
        for j in weapon_multi[dn['Weapon Type']]:
            dn[j] = round(dn[j] * weapon_multi[dn['Weapon Type']][j], 2)

        # Perks
        for i in dn.keys():
            for j in perk_multi.keys():
                for k in perk_multi[j].keys():
                    if i == k:
                        dn[i] = round(dn[i] * perk_multi[j][k], 2)

        if perk_multi['deadshot']['consecutive'] == 1:
            self.consecutive = True
        else:
            self.consecutive = False

        return dn

    def apply_attachments(self, dic: dict, attachment_lst: List[str]) -> dict:

        if dic['Pack'] != '0':
            pack_mag = True
        else:
            pack_mag = False

        dn = dic.copy()
        dm = {i: 0.0 for i in dic.keys()}
        for i in attachment_lst:
            if i == '0':
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

    def get_attachments(self, dic: dict, inp=None, extended=None):

        if extended is not None:
            temp_df = DataFrame(columns=['Effects', 'Spot', 'Name'])
            for part in ['Muzzle', 'Barrel', 'Body', 'Under_Barrel', 'Magazine', 'Handle', 'Stock']:
                temp_i = DataFrame(index=list(dic[part].keys()), columns=['Effects', 'Spot', 'Name'])
                for j in dic[part].keys():
                    temp_i.loc[j] = [dic[part][j], part, j]
                temp_df = concat([temp_df, temp_i])
            temp_df = temp_df.set_index(['Spot', 'Name'])

            if inp is None:
                return temp_df
        else:
            temp_df = DataFrame(columns=['Names'])
            for part in ['Muzzle', 'Barrel', 'Body', 'Under_Barrel', 'Magazine', 'Handle', 'Stock']:
                if dic[part] is not None:
                    temp_i = DataFrame([[list(dic[part].keys())]], index=[part], columns=['Names'])
                    temp_df = concat([temp_df, temp_i])

            if inp is None:
                return temp_df

        if inp is not None:
            temp_lst = []
            for part in ['Muzzle', 'Barrel', 'Body', 'Under_Barrel', 'Magazine', 'Handle', 'Stock']:
                if part in inp.keys():
                    temp_lst.append(dic[part][inp[part]])
            return sum(temp_lst, [])

    def process(self,
                weapon: str,
                nickname: str = None,
                equipped_attachments: List[str] = None,
                rarity: str = None,
                pap: str = None,
                accuracy: float = None,
                critical: float = None) -> List[dict]:

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
                 'Under_Barrel': d.under_barrel,
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

        # dic_i['Damage'] = dic_i['Damage'] * dic_i['Burst']
        # dic_i['Damage 2'] = dic_i['Damage 2'] * dic_i['Burst']
        # dic_i['Damage 3'] = dic_i['Damage 3'] * dic_i['Burst']
        # dic_i['Mag Capacity'] = dic_i['Mag Capacity'] / dic_i['Burst']

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

        temp_dic = self.apply_multipliers(self.get_weapon_classes(), self.get_perk_classes(), dic_i)

        if equipped_attachments is not None:
            effect_lst = self.get_attachments(temp_dic, equipped_attachments, True)
            final_dic = self.apply_attachments(temp_dic, effect_lst)

            for part in ['Muzzle', 'Barrel', 'Body', 'Under_Barrel', 'Magazine', 'Handle', 'Stock']:
                if part in equipped_attachments.keys():
                    final_dic[part] = (equipped_attachments[part], final_dic[part][equipped_attachments[part]])
                else:
                    final_dic[part] = None
            temp_dic = final_dic
        else:
            pass

        temp_dic['Shooting Time'] = aa.shoot_time(temp_dic)
        temp_dic['Shoot To Reload Ratio'] = aa.shoot_reload_ratio(temp_dic)
        temp_dic['Movement Ratio'] = aa.movement_ratio(temp_dic)
        temp_dic['Control Ratio'] = aa.control_ratio(temp_dic)
        temp_dic['Drop Off Ratio'] = aa.drop_off_ratio(temp_dic)

        dic_i['Shooting Time'] = aa.shoot_time(dic_i)
        dic_i['Shoot To Reload Ratio'] = aa.shoot_reload_ratio(dic_i)
        dic_i['Movement Ratio'] = aa.movement_ratio(dic_i)
        dic_i['Control Ratio'] = aa.control_ratio(dic_i)
        dic_i['Drop Off Ratio'] = aa.drop_off_ratio(dic_i)

        return [dic_i, temp_dic]

    def process_multi(self, weapon_lst) -> list:

        p_lst = []
        for i in weapon_lst:
            o, n = self.process(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            p_lst.append(n)

        return p_lst
