# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:18:33 2021

@author: Peter
"""
from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze

if __name__ == '__main__':

    # User inputs
    weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                           'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}

    # Core Classes
    damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                                   max_range=100)

    # Set Zombie Health
    zom = Health(level=60, health_cap=55, outbreak=False, multiplier=2)
    zombie_health = zom.get_health  # 60,250
    zombie_armour = zom.get_armour  # 30,125

    # Example Loadouts
    rarity = 'orange'
    pap = '3'

    M16 = {
        'Muzzle': 'Agency Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'Salvo Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'Raider Pad'
    }
    carv = {
        'Muzzle': 'Agency Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'Salvo Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'Raider Pad'
    }
    ots = {
        'Muzzle': 'GRU Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'VDV Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'KGB Skeletal Stock'
    }
    tec = {
        'Muzzle': 'Full Repeater',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Underbarrel': 'Bruiser Grip',
        'Magazine': 'Salvo Fast Mag',
        'Handle': 'Serpent Wrap',
        'Stock': 'SAS Combat Stock'
    }
    amp = {
        'Muzzle': 'Agency Suppressor',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Magazine': 'Salvo Fast Mag',
        'Stock': 'Dual Wield'
    }
    gallo = {
        'Muzzle': 'Infantry V-Choke',
        'Barrel': 'Task Force',
        'Body': 'Ember Sighting Point',
        'Magazine': 'STANAG Mag',
        'Stock': 'Marathon Stock'
    }
    gun_lst = [
        {'weapon': 'M16', 'nickname': 'Temp M16', 'equipped_attachments': M16, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
        {'weapon': 'CARV', 'nickname': 'Temp CARV', 'equipped_attachments': carv, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
        {'weapon': 'Gallo', 'nickname': 'Temp Gallo', 'equipped_attachments': gallo, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
        {'weapon': 'OTS', 'nickname': 'Temp Ots9', 'equipped_attachments': ots, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
        {'weapon': 'Tec9', 'nickname': 'Temp Tec9', 'equipped_attachments': tec, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
        {'weapon': 'AMP', 'nickname': 'Temp AMP', 'equipped_attachments': amp, 'rarity': rarity,
         'pap': pap, 'accuracy': None, 'critical': None},
    ]

    # Build Analyze Class
    analysis = Analyze(damage_profile=damage_profile, zombie_info=zom, weapon_dic_lst=gun_lst)

    gun_df

    # Not Finished
    # data = base.get_attachments(weapon_dic=base.process('AK74u'))
    # effect_lst = []
    # index_lst = []
    # for ind, val in enumerate(data['effect']):
    #     for effect in val:
    #         if 'Vertical' in effect:
    #             index_lst.append(ind)
    #             effect_lst.append(effect)
    # data_n = data.iloc[index_lst]
    #
    # import matplotlib.pyplot as plt
    # import pandas as pd
    # import numpy as np
    #
    # t = base.stats['AK74u'].vertical_recoil
    #
    # num_lst = []
    # for effect in effect_lst:
    #     e_i = float(effect.split('%')[0].split(' ')[1]) / 100
    #     if '+' in effect:
    #         num_lst.append(t + (t * e_i))
    #     else:
    #         num_lst.append(t - (t * e_i))
    #
    # people = ['None'] + list(data_n['name'])
    # y_pos = np.arange(len(people))
    # # performance = [t] + num_lst
    # fig, ax = plt.subplots(figsize=(10, 7))
    #
    # arr = np.array(num_lst)
    # tt = [.5] + list(np.around((arr - t) / (np.max(arr) - np.min(arr)).T + 0.50, 3))
    # performance = tt
    # ax.barh(y_pos, performance, align='center')
    # for i, v in enumerate(performance):
    #     ax.text(v + 5, i, str(int(v)), color='black', fontsize='medium')
    #
    # for i, v in enumerate(['None'] + list(data_n['location'])):
    #     ax.text(5, i, v, color='black', fontsize='xx-large')
    #
    # ax.set_yticks(y_pos)
    # ax.set_yticklabels(people)
    # ax.invert_yaxis()
    # ax.set_xlabel('Vertical Recoil')
    # ax.set_title('AK74u')
    # plt.show()

