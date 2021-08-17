# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:08:22 2021

@author: Peter
"""
import numpy as np
from numpy.random import normal
import pandas as pd
from typing import List
import matplotlib.pyplot as plt
from random import choices, seed
seed(1)


class Analyze:

    def __init__(self, build, max_range: int = 200):

        self.consecutive = build.consecutive
        self.stats = build.stats
        self.col_lst = build.col_lst
        self.max_range = max_range
        self.gun_names = list(build.stats.keys())

        def shot_distribution() -> np.ndarray:
            acc = [i.gun_acc_value for i in build.stats.values()]
            acc_n = [i for i in acc if i != 0]
            sig1 = np.around(np.std(acc_n), 3)
            mu1 = np.around(np.mean(acc_n), 3)
            return np.around(normal(mu1, sig1, 2500), 3)

        self.hits = shot_distribution()

    def mu_shots(self, weapon_dic: dict) -> np.ndarray:
        ac = weapon_dic['Accuracy']
        dis = self.hits
        ind = np.cumsum([1 if i <= ac else 0 for i in dis])

        if self.consecutive:
            con = [0, 1.00, 1.02, 1.04, 1.06, 1.08, 1.10, 1.12, 1.14, 1.16, 1.18, 1.20] + ([1.20] * 40)
        else:
            con = [1.00] * 50

        con_lst_master = []
        con_lst = [1]
        count = 0
        for i, j in enumerate(ind):
            if j - 1 is ind[i - 1]:
                count += 1
                con_lst.append(count)
            else:
                con_lst_master.append(con_lst)
                count, con_lst = 0, [0]

        con_lst_master_n = sum(con_lst_master, [])
        con_shots = [con[i] for i in con_lst_master_n]
        crit1 = weapon_dic['Critical']
        headshots = choices([0, 1], k=len(con_shots), weights=[1 - crit1, crit1])
        headshot_multi = weapon_dic['Crit']
        temp_lst = list(
            np.around([con_shots[i] * headshot_multi if j == 1.00 else 1.00 for i, j in enumerate(headshots)], 2))
        arr = np.array(temp_lst + ([0] * (2500 - len(temp_lst))))

        mc = int(weapon_dic['Mag Capacity'])
        average_shots = np.ceil(np.mean([sum([arr[k - q] for q in range(mc)]) for k, l in enumerate(arr)]))

        return average_shots

    def damage_range(self, weapon_dic: dict) -> np.ndarray:
        m = weapon_dic['Burst']
        dam1 = weapon_dic['Damage']
        dam2 = weapon_dic['Damage 2']
        dam3 = weapon_dic['Damage 3']
        ran1 = weapon_dic['Range']
        ran2 = weapon_dic['Range 2']
        ran = list(range(self.max_range))

        if weapon_dic['Weapon Type'] == 'Shotguns':
            if ran1 == 5.72:
                m2 = [1 - (i / 15) for i in range(15)]
            else:
                m1 = np.floor((ran1 / 5.72 * 20) - ran1)
                m2 = [1 - (i / m1) for i in range(m1)]

            dam_lst = [dam1] * (np.floor(ran1)) + [np.floor(dam1 * i) for i in m2]
            dam_lst = dam_lst + ([0] * len(dam_lst))
        else:
            dam_lst = []
            if ran2 == 0:
                for i in ran:
                    if i < ran1:
                        dam_lst.append(dam1 * m)
                        continue
                    else:
                        dam_lst.append(dam3 * m)
                        continue
            else:
                for i in ran:
                    if i < ran1:
                        dam_lst.append(dam1 * m)
                        continue
                    elif i < ran2:
                        dam_lst.append(dam2 * m)
                        continue
                    else:
                        dam_lst.append(dam3 * m)

        return np.array(dam_lst)

    def damage_per_second(self, weapon_dic: dict, damage_range_arr: np.ndarray) -> np.ndarray:
        return np.multiply(np.ceil(weapon_dic['Fire Rate'] / 60), damage_range_arr)

    def time_to_kill(self, weapon_dic: dict, damage_range_arr: np.ndarray, zombie_health: float) -> np.ndarray:
        dps = self.damage_per_second(weapon_dic, damage_range_arr)
        return np.around(np.add(np.divide(zombie_health, dps),
                                np.divide(range(self.max_range), weapon_dic['Velocity'])), 2)

    def shots_to_kill(self, damage_range_arr: np.ndarray, zombie_health: float) -> np.ndarray:
        return np.around(np.divide(zombie_health, damage_range_arr), 0)

    def shoot_time(self, weapon_dic: dict) -> float:
        return round(weapon_dic['Mag Capacity'] / (weapon_dic['Fire Rate'] / 60), 2)

    def shoot_reload_ratio(self, weapon_dic: dict) -> float:
        return 1 - round(weapon_dic['Reload'] / self.shoot_time(weapon_dic=weapon_dic), 2)

    def damage_per_max_ammo(self, weapon_dic: dict, damage_range_arr: np.ndarray) -> np.ndarray:
        return np.multiply(np.divide(weapon_dic['Ammo Capacity'], weapon_dic['Burst']), damage_range_arr)

    def damage_per_clip(self, damage_range_arr: np.ndarray, shots_average: np.ndarray) -> np.ndarray:
        return np.around([damage_range_arr[i] * shots_average for i, j in enumerate(damage_range_arr)], 0)

    def movement_ratio(self, weapon_dic: dict) -> float:
        lst = {
            'Movement Speed': [0, 0, 0],
            'Sprinting Speed': [0, 0, 0],
            'Shooting Speed': [0, 0, 0],
            'Sprint to Fire': [0, 0, 0],
            'Aim Walking': [0, 0, 0],
            'ADS': [0, 0, 0]
        }

        for i in lst.keys():
            temp_lst = []
            for j in self.gun_names:
                if i == 'Movement Speed':
                    temp_lst.append(self.stats[j].movement)
                    continue
                elif i == 'Sprinting Speed':
                    temp_lst.append(self.stats[j].sprint)
                    continue
                elif i == 'Shooting Speed':
                    temp_lst.append(self.stats[j].shoot_speed)
                    continue
                elif i == 'Sprint to Fire':
                    temp_lst.append(self.stats[j].sprint_to_fire)
                    continue
                elif i == 'Aim Walking':
                    temp_lst.append(self.stats[j].aim_walking)
                    continue
                elif i == 'ADS':
                    temp_lst.append(self.stats[j].ads)
                    continue

            lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

        ratio = round(sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def control_ratio(self, weapon_dic: dict) -> float:
        lst = {
            'Vertical Recoil': [0, 0, 0],
            'Horizontal Recoil': [0, 0, 0],
            'Centering Speed': [0, 0, 0],
            'Hip Fire': [0, 0, 0],
        }

        for i in lst.keys():
            temp_lst = []
            for j in self.gun_names:
                if i == 'Vertical Recoil':
                    temp_lst.append(self.stats[j].vertical_recoil)
                    continue
                if i == 'Horizontal Recoil':
                    temp_lst.append(self.stats[j].horizontal_recoil)
                    continue
                if i == 'Centering Speed':
                    temp_lst.append(self.stats[j].centering_speed)
                    continue
                if i == 'Hip Fire':
                    temp_lst.append(self.stats[j].hip_fire)
                    continue
            lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

        ratio = 1 - round(
            sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def drop_off_ratio(self, weapon_dic: dict) -> float:
        return 1 + round((weapon_dic['Damage 3'] - weapon_dic['Damage']) / weapon_dic['Damage'], 2)

    def check_multi(self, damage_range_arr: np.ndarray, weapon_dic: dict) -> np.ndarray:
        close = weapon_dic['Close']
        long = weapon_dic['Long']
        long_shot = weapon_dic['Long Shot']
        t = list(damage_range_arr)
        temp_lst = []

        for k, j in enumerate(t):
            if k <= 4:
                temp_lst.append(j * close)
            elif k >= long_shot:
                temp_lst.append(j * long)
            else:
                temp_lst.append(j)

        return np.array(temp_lst)

    def compare(self, weapon_dic: dict, zombie_health: float, for_viz: bool = False, armour: bool = False):
        mu = self.mu_shots(weapon_dic)
        damage_range = self.check_multi(damage_range_arr=self.damage_range(weapon_dic=weapon_dic), weapon_dic=weapon_dic)

        if armour:
            armour_damage_range = np.multiply(np.divide(damage_range, 4), weapon_dic['Armour Damage'])
            if for_viz:
                temp_dic = {
                    'Damage Per Clip': self.damage_per_clip(damage_range_arr=armour_damage_range,
                                                            shots_average=mu),
                    'Damage Per Second': self.damage_per_second(weapon_dic=weapon_dic,
                                                                damage_range_arr=armour_damage_range),
                    'Time To Kill': self.time_to_kill(weapon_dic=weapon_dic,
                                                      damage_range_arr=damage_range,
                                                      zombie_health=zombie_health) +
                                    self.time_to_kill(weapon_dic=weapon_dic,
                                                      damage_range_arr=armour_damage_range,
                                                      zombie_health=zombie_health + armour),
                    'Shots To Kill': self.shots_to_kill(damage_range_arr=damage_range,
                                                        zombie_health=zombie_health) +
                                     self.shots_to_kill(damage_range_arr=armour_damage_range,
                                                        zombie_health=zombie_health + armour),
                    'Damage Per Max Ammo': self.damage_per_max_ammo(weapon_dic=weapon_dic,
                                                                    damage_range_arr=armour_damage_range)
                }

                return [weapon_dic['Temp Name'], pd.DataFrame(temp_dic)]
            else:
                temp_dic = {'Temp Name': weapon_dic['Temp Name'],
                            'Damage Per Clip': self.damage_per_clip(damage_range_arr=armour_damage_range,
                                                                    shots_average=mu),
                            'Damage Per Second': self.damage_per_second(weapon_dic=weapon_dic,
                                                                        damage_range_arr=armour_damage_range),
                            'Time To Kill': self.time_to_kill(weapon_dic=weapon_dic,
                                                              damage_range_arr=damage_range,
                                                              zombie_health=zombie_health) +
                                            self.time_to_kill(weapon_dic=weapon_dic,
                                                              damage_range_arr=armour_damage_range,
                                                              zombie_health=zombie_health + armour),
                            'Shots To Kill': self.shots_to_kill(damage_range_arr=damage_range,
                                                                zombie_health=zombie_health) +
                                             self.shots_to_kill(damage_range_arr=armour_damage_range,
                                                                zombie_health=zombie_health + armour),
                            'Damage Per Max Ammo': self.damage_per_max_ammo(weapon_dic=weapon_dic,
                                                                            damage_range_arr=armour_damage_range),
                            'Shooting Time': self.shoot_time(weapon_dic=weapon_dic),
                            'Shoot To Reload Ratio': self.shoot_reload_ratio(weapon_dic=weapon_dic),
                            'Movement Ratio': self.movement_ratio(weapon_dic=weapon_dic),
                            'Control Ratio': self.control_ratio(weapon_dic=weapon_dic),
                            'Drop Off Ratio': self.drop_off_ratio(weapon_dic=weapon_dic),
                            }
                return temp_dic
        else:
            if for_viz:
                temp_dic = {
                    'Damage Per Clip': self.damage_per_clip(damage_range_arr=damage_range,
                                                            shots_average=mu),
                    'Damage Per Second': self.damage_per_second(weapon_dic=weapon_dic,
                                                                damage_range_arr=damage_range),
                    'Time To Kill': self.time_to_kill(weapon_dic=weapon_dic,
                                                      damage_range_arr=damage_range,
                                                      zombie_health=zombie_health),
                    'Shots To Kill': self.shots_to_kill(damage_range_arr=damage_range,
                                                        zombie_health=zombie_health),
                    'Damage Per Max Ammo': self.damage_per_max_ammo(weapon_dic=weapon_dic,
                                                                    damage_range_arr=damage_range),
                    }
                return pd.DataFrame(temp_dic)
            else:
                temp_dic = {'Temp Name': weapon_dic['Temp Name'],
                            'Damage Per Clip': self.damage_per_clip(damage_range_arr=damage_range,
                                                                    shots_average=mu),
                            'Damage Per Second': self.damage_per_second(weapon_dic=weapon_dic,
                                                                        damage_range_arr=damage_range),
                            'Time To Kill': self.time_to_kill(weapon_dic=weapon_dic,
                                                              damage_range_arr=damage_range,
                                                              zombie_health=zombie_health),
                            'Shots To Kill': self.shots_to_kill(damage_range_arr=damage_range,
                                                                zombie_health=zombie_health),
                            'Damage Per Max Ammo': self.damage_per_max_ammo(weapon_dic=weapon_dic,
                                                                            damage_range_arr=damage_range),
                            'Shooting Time': self.shoot_time(weapon_dic=weapon_dic),
                            'Shoot To Reload Ratio': self.shoot_reload_ratio(weapon_dic=weapon_dic),
                            'Movement Ratio': self.movement_ratio(weapon_dic=weapon_dic),
                            'Control Ratio': self.control_ratio(weapon_dic=weapon_dic),
                            'Drop Off Ratio': self.drop_off_ratio(weapon_dic=weapon_dic),
                            }

                return temp_dic

    def build_df(self, weapon_dic_lst: List[dict], cols: List[str] = None) -> pd.DataFrame:

        data_n = []
        for dic in weapon_dic_lst:
            dic['Shooting Time'] = self.shoot_time(dic)
            dic['Shoot To Reload Ratio'] = self.shoot_reload_ratio(dic)
            dic['Movement Ratio'] = self.movement_ratio(dic)
            dic['Control Ratio'] = self.control_ratio(dic)
            dic['Drop Off Ratio'] = self.drop_off_ratio(dic)
            data_n.append(dic)

        if cols is None:
            return pd.DataFrame(data_n)[self.col_lst].set_index('Temp Name')
        else:
            return pd.DataFrame(data_n)[cols].set_index('Temp Name')

    def viz(self, gun_data: dict, keyword: str, x_limit: int, ind: int, save_image: bool = False) -> None:
        n = 0
        df = pd.DataFrame()
        for i in gun_data.keys():
            df[i] = gun_data[i][keyword]
            if keyword in gun_data[i].columns:
                n += 1

        cmap = [plt.get_cmap('viridis')(1. * i / n) for i in range(n)]
        mu = df.mean(axis=1)
        labels = []
        count = 0
        for i in df.columns:
            plt.plot(df[i], label=i, color=cmap[count])
            labels.append(str(df[i].iloc[ind]))
            count += 1
        plt.plot(mu, label='Mu', color='tab:orange', linestyle='--', alpha=1)
        labels = labels + [str(round(mu.iloc[ind], 1))]
        plt.title(keyword)
        legend1 = plt.legend(labels, title='Value at ' + str(ind), loc='upper right') #, bbox_to_anchor=(1.05, .5)
        plt.legend(title='Legend', loc='lower right') # bbox_to_anchor=(1.05, .5)
        plt.xlabel('Meters')

        if 'Damage' in keyword:
            plt.ylabel('Damage')
        elif 'Time' in keyword:
            plt.ylabel('Seconds')
        elif 'Shots' in keyword:
            plt.ylabel('Shots')
        elif 'Ratio' in keyword:
            plt.ylabel('Ratio')
        else:
            plt.ylabel('Other')

        plt.grid(linewidth=1, linestyle=(0, (5, 5)), alpha=.75)
        plt.xlim(0, x_limit)
        plt.gca().add_artist(legend1)

        if save_image:
            plt.savefig(keyword)

        plt.show()

    def viz_all(self, weapon_df_dic: dict, x_limit: int, ind: int, save_image: bool) -> None:

        for keyword in ['Damage Per Max Ammo', 'Damage Per Clip', 'Damage Per Second', 'Time To Kill', 'Shots To Kill']:
            self.viz(gun_data=weapon_df_dic,
                     keyword=keyword,
                     x_limit=x_limit,
                     ind=ind,
                     save_image=save_image)
