# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:08:22 2021

@author: Peter
"""
import Utils.weapon_stats as w
import numpy as np
from numpy.random import normal
from pandas import DataFrame
import matplotlib.pyplot as plt
from random import choices, seed
seed(1)


def damage_per_clip(dr: np.ndarray, shots_average: np.ndarray) -> np.ndarray:
    n_dr = [dr[i] * shots_average for i, j in enumerate(dr)]
    return np.around(n_dr, 0)


class Analyze:

    def __init__(self, ranges: int = 200):
        self.ranges = ranges
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

        def shot_distribution() -> np.ndarray:
            acc = [i.gun_acc_value for i in self.stats.values()]
            acc_n = [i for i in acc if i != 0]
            sig1 = np.around(np.std(acc_n), 3)
            mu1 = np.around(np.mean(acc_n), 3)
            return np.around(normal(mu1, sig1, 2500), 3)

        self.hits = shot_distribution()

    def mu_shots(self, dic: dict) -> np.ndarray:
        ac = dic['Accuracy']
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
        crit1 = dic['Critical']
        headshots = choices([0, 1], k=len(con_shots), weights=[1 - crit1, crit1])
        headshot_multi = dic['Crit']
        temp_lst = list(
            np.around([con_shots[i] * headshot_multi if j == 1.00 else 1.00 for i, j in enumerate(headshots)], 2))
        arr = np.array(temp_lst + ([0] * (2500 - len(temp_lst))))

        mc = int(dic['Mag Capacity'])
        average_shots = np.ceil(np.mean([sum([arr[k - q] for q in range(mc)]) for k, l in enumerate(arr)]))

        return average_shots

    def damage_range(self, dic: dict) -> np.ndarray:
        m = dic['Burst']
        dam1 = dic['Damage']
        dam2 = dic['Damage 2']
        dam3 = dic['Damage 3']
        ran1 = dic['Range']
        ran2 = dic['Range 2']
        ran = list(range(self.ranges))

        if dic['Weapon Type'] == 'Shotguns':
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

    def damage_per_second(self, dic: dict, dr: np.ndarray) -> np.ndarray:
        return np.multiply(np.ceil(dic['Fire Rate'] / 60), dr)

    def time_to_kill(self, dic: dict, dr: np.ndarray, zom: float) -> np.ndarray:
        dps = self.damage_per_second(dic, dr)
        return np.around(np.add(np.divide(zom, dps), np.divide(range(self.ranges), dic['Velocity'])), 2)

    def shots_to_kill(self, dr: np.ndarray, zom: float) -> np.ndarray:
        return np.around(np.divide(zom, dr), 0)

    def shoot_time(self, dic: dict) -> float:
        return round(dic['Mag Capacity'] / (dic['Fire Rate'] / 60), 2)

    def shoot_reload_ratio(self, dic: dict) -> float:
        return 1 - round(dic['Reload'] / self.shoot_time(dic), 2)

    def damage_per_max_ammo(self, dic: dict, dr: np.ndarray) -> np.ndarray:
        return np.multiply(np.divide(dic['Ammo Capacity'], dic['Burst']), dr)

    def movement_ratio(self, dic: dict) -> float:
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

            lst[i] = [min(temp_lst), max(temp_lst), dic[i]]

        ratio = round(sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def control_ratio(self, dic: dict) -> float:
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
            lst[i] = [min(temp_lst), max(temp_lst), dic[i]]

        ratio = 1 - round(
            sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def drop_off_ratio(self, dic: dict) -> float:
        return 1 + round((dic['Damage 3'] - dic['Damage']) / dic['Damage'], 2)

    def check_multi(self, lst, dic: dict) -> np.ndarray:
        close, long, long_shot, t, temp_lst = dic['Close'], dic['Long'], dic['Long Shot'], list(lst), []
        for k, j in enumerate(t):
            if k <= 4:
                temp_lst.append(j * close)
            elif k >= long_shot:
                temp_lst.append(j * long)
            else:
                temp_lst.append(j)

        return np.array(temp_lst)

    def compare(self, dic: dict, zom: float, for_viz: bool = False, armour: bool = False):
        mu = self.mu_shots(dic)
        damage_range = self.check_multi(self.damage_range(dic), dic)

        if armour:
            adr = np.multiply(np.divide(damage_range, 4), dic['Armour Damage'])
            if for_viz:
                temp_dic = {
                    'Damage Per Clip': damage_per_clip(adr, mu),
                    'Damage Per Second': self.damage_per_second(dic, adr),
                    'Time To Kill': self.time_to_kill(dic, damage_range, zom) + self.time_to_kill(dic, adr,
                                                                                                  zom + armour),
                    'Shots To Kill': self.shots_to_kill(damage_range, zom) + self.shots_to_kill(adr, zom + armour),
                    'Damage Per Max Ammo': self.damage_per_max_ammo(dic, adr)
                }

                return [dic['Temp Name'], DataFrame(temp_dic)]
            else:
                temp_dic = {'Temp Name': dic['Temp Name'],
                            'Damage Per Clip': damage_per_clip(adr, mu),
                            'Damage Per Second': self.damage_per_second(dic, adr),
                            'Time To Kill': self.time_to_kill(dic, damage_range, zom) + self.time_to_kill(dic,
                                                                                                          adr,
                                                                                                          zom + armour),
                            'Shots To Kill': self.shots_to_kill(damage_range, zom) + self.shots_to_kill(adr,
                                                                                                        zom + armour),
                            'Damage Per Max Ammo': self.damage_per_max_ammo(dic, adr),
                            'Shooting Time': self.shoot_time(dic),
                            'Shoot To Reload Ratio': self.shoot_reload_ratio(dic),
                            'Movement Ratio': self.movement_ratio(dic),
                            'Control Ratio': self.control_ratio(dic),
                            'Drop Off Ratio': self.drop_off_ratio(dic),
                            }
                return temp_dic
        else:
            if for_viz:
                temp_dic = {
                    'Damage Per Clip': damage_per_clip(damage_range, mu),
                    'Damage Per Second': self.damage_per_second(dic, damage_range),
                    'Time To Kill': self.time_to_kill(dic, damage_range, zom),
                    'Shots To Kill': self.shots_to_kill(damage_range, zom),
                    'Damage Per Max Ammo': self.damage_per_max_ammo(dic, damage_range),
                    }
                return [dic['Temp Name'], DataFrame(temp_dic)]
            else:
                temp_dic = {'Temp Name': dic['Temp Name'],
                            'Damage Per Clip': damage_per_clip(damage_range, mu),
                            'Damage Per Second': self.damage_per_second(dic, damage_range),
                            'Time To Kill': self.time_to_kill(dic, damage_range, zom),
                            'Shots To Kill': self.shots_to_kill(damage_range, zom),
                            'Damage Per Max Ammo': self.damage_per_max_ammo(dic, damage_range),
                            'Shooting Time': self.shoot_time(dic),
                            'Shoot To Reload Ratio': self.shoot_reload_ratio(dic),
                            'Movement Ratio': self.movement_ratio(dic),
                            'Control Ratio': self.control_ratio(dic),
                            'Drop Off Ratio': self.drop_off_ratio(dic),
                            }

                return temp_dic

    def viz(self, gun_lst: list, keyword: str, x_limit: int, ind: int, save_image: bool = False) -> None:
        n = 0
        for i in gun_lst:
            if keyword in i[1].columns:
                n += 1

        cmap = [plt.get_cmap('viridis')(1. * i / n) for i in range(n)]

        df = DataFrame()
        for i in gun_lst:
            df[i[0]] = i[1][keyword]

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

        plt.grid(linestyle=':')
        plt.xlim(0, x_limit)
        plt.gca().add_artist(legend1)

        if save_image:
            plt.savefig(keyword)

        plt.show()


