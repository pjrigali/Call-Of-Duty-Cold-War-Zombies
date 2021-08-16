# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:18:33 2021

@author: Peter
"""
from Utils import health_armour as z
from Utils import analysis as a
from Utils import processor as p
analysis = a.Analyze()


if __name__ == '__main__':

    weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                           'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5'}
    base = p.Build(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels)

    zombie_health = z.Health(level=20, outbreak=False).get_health()
    zombie_armour = z.Armour(level=20, outbreak=False).get_armour()

    # Return the attachments and their effects for a specific gun
    attach = base.process('Diamatti')[0]
    attach_df = base.get_attachments(dic=attach, inp=None, extended=True)

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
        'Muzzle': 'GRU Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'VDV Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'Spetsnaz PKM Stock'
    }

    equipped5 = {
        'Muzzle': 'GRU Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'VDV Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'Spetsnaz PKM Stock'
    }
    equipped6 = {
        'Muzzle': 'Agency Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'Salvo Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'SAS Combat Stock'
    }

    guns = base.process_multi([
        {'weapon': 'MP5', 'nickname': 'Temp MP5', 'equipped_attachments': equipped1, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
        {'weapon': 'PPSH', 'nickname': 'Temp PPSH', 'equipped_attachments': equipped2, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
        {'weapon': 'OTS', 'nickname': 'Temp Ots9', 'equipped_attachments': equipped3, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
        {'weapon': 'AK74u', 'nickname': 'Temp AK74u', 'equipped_attachments': equipped4, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
        {'weapon': 'Bullfrog', 'nickname': 'Temp Bullfrog', 'equipped_attachments': equipped5, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
        {'weapon': 'LC10', 'nickname': 'Temp LC10', 'equipped_attachments': equipped6, 'rarity': 'common',
         'pap': '0', 'accuracy': None, 'critical': None},
    ])

    gun_df = base.build_df(data=guns, cols=base.col_lst)

    weapon_compare = {}
    for i in guns:
        weapon_compare[i['Temp Name']] = analysis.compare(dic=i, zom=zombie_health, for_viz=True, armour=False)

    analysis.viz_all(data=weapon_compare, x_limit=40, ind=5, save_image=False)

    # Returns the effects from the attachments
    base.get_attachments(base.process('AK74u')[1], equipped4, False)

