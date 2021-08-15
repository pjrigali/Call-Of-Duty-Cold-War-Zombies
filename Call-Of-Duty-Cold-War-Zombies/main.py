# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:18:33 2021

@author: Peter
"""

import pandas as pd
from Utils import health_armour as z
from Utils import analysis as a
from Utils import processor as p
import warnings
pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")

base = p.Build(weapon_class_levels=['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
               perk_class_levels=['5', '5', '5'])
aa = a.Analyze()

# Health and Armour
zom = z.Health(12, False).get_health()
ar = z.Armour(12, False).get_armour()

# attach = base.process('Diamatti')[0]
# print(base.get_attachments(dic=attach, extended=True))

equipped1 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Raider Stock'
}

equipped2 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'KGB Skeletal Stock'
}

equipped3 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'KGB Skeletal Stock'
}

equipped4 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Magazine': 'Salvo Fast Mag',
    'Stock': 'Dual Wield'
}

equipped5 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Mounted Flashlight',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'SAS Combat Stock'
}

equipped6 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'RPK',
    'Body': 'Mounted Flashlight',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Raider Stock'
}

equipped7 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Strike Team',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Raider Pad'
}
equipped8 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Strike Team',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'SAS Combat Stock'
}

equipped9 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Spetsnaz PKM Stock'
}

equipped10 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Spetsnaz PKM Stock'
}
equipped11 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'SAS Combat Stock'
}
guns = base.process_multi([
    ['MP5', 'Temp MP5', equipped1, 'common', '0', None, None],
    ['PPSH', 'Temp PPSH', equipped2, 'common', '0', None, None],
    ['OTS', 'Temp Ots9', equipped3, 'common', '0', None, None],
    # ['AMP', 'Temp AMP', equipped4, 'common', '0', None, None],
    # ['XM4', 'Temp XM4', equipped5, 'common', '0', None, None],
    # ['FARA', 'Temp FARA', equipped6, 'common', '0', None, None],
    # ['M16', 'Temp M16', equipped7, 'common', '0', None, None],
    # ['CARV', 'Temp CARV', equipped8, 'common', '0', None, None],
    ['AK74u', 'Temp AK74u', equipped9, 'common', '0', None, None],
    ['Bullfrog', 'Temp Bullfrog', equipped10, 'common', '0', None, None],
    ['LC10', 'Temp LC10', equipped11, 'common', '0', None, None],

])


col_lst = [
    'Name', 'Temp Name', 'Damage', 'Damage 2', 'Damage 3', 'Range',
    'Range 2', 'Fire Rate', 'Velocity', 'Armour Damage', 'Melee Quickness',
    'Movement Speed', 'Sprinting Speed', 'Shooting Speed', 'Sprint to Fire',
    'Aim Walking', 'ADS', 'Vertical Recoil', 'Horizontal Recoil',
    'Centering Speed', 'Idle Sway', 'Flinch', 'Hip Fire', 'Mag Capacity',
    'Reload', 'Ammo Capacity', 'Accuracy', 'Critical', 'Pack', 'Rare',
    'Shoot To Reload Ratio', 'Movement Ratio', 'Control Ratio', 'Drop Off Ratio'
]
print((pd.DataFrame(guns)[col_lst]).set_index('Temp Name'))

compare_lst = []
for i in guns:
    compare_lst.append(aa.compare(i, zom, True, False))

aa.viz(compare_lst, 'Damage Per Max Ammo', 40, 5)
aa.viz(compare_lst, 'Damage Per Clip', 40, 5)
aa.viz(compare_lst, 'Damage Per Second', 40, 5)
# aa.viz(compare_lst, 'Damage Per Second', 100, 45)
# aa.viz(compare_lst, 'Damage Per Second', 150, 125)
aa.viz(compare_lst, 'Time To Kill', 40, 5)
aa.viz(compare_lst, 'Shots To Kill', 40, 5)

t_d = base.process('Magnum', 'Temp Magnum', equipped4, 'common', '0', False, False)[0]

# base.get_attachments(base.process('Magnum')[1], equipped4, False)
