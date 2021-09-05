# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:08:22 2021

@author: Peter
"""
import numpy as np
import pandas as pd
from typing import List
import matplotlib.pyplot as plt
import random
from processor import Build
random.seed(1)


class Analyze(Build):
    """
    Constructs  dicts, pd.DataFrames and visualizations for comparing various weapons.

    Applies buffs from attachments.

    Parameters
    ----------
    weapon_class_levels : dict, default None
        User input tiers for each weapon class. Use str value betweem 0 and 5.
    perk_class_levels : dict, default None
        User input tiers for each perk. Use str value value between 0 and 5.
    max_range : int
        User desired maximum distance for the function to compute values for. (In meters)

    Examples
    --------
    By default the values are set to 0. User inputs change these and the effects are applied across the weapons:

    >>> from zombie import analysis as a
    >>> weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
    >>>                        'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    >>> perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
    >>> analysis = a.Analyze(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
    >>>                      max_range=100)

    """

    def __init__(self, weapon_class_levels: dict = None, perk_class_levels: dict = None, max_range: int = 200):
        self._build = Build(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels)
        self.max_range = max_range

    def process(self, weapon_dic: dict) -> dict:
        """Create a dict for a weapon with all stats. Including attachments, perk and weapon tier effects"""

        new_weapon_dic = {}
        for i in ['weapon', 'nickname', 'equipped_attachments', 'rarity', 'pap', 'accuracy', 'critical']:
            if i in weapon_dic.keys():
                new_weapon_dic[i] = weapon_dic[i]
            else:
                new_weapon_dic[i] = None

        return self._build._process(weapon=new_weapon_dic['weapon'], nickname=new_weapon_dic['nickname'],
                                    equipped_attachments=new_weapon_dic['equipped_attachments'],
                                    rarity=new_weapon_dic['rarity'], pap=new_weapon_dic['pap'],
                                    accuracy=new_weapon_dic['accuracy'], critical=new_weapon_dic['critical'])

    def process_multi(self, weapon_dic_lst: List[dict]) -> List[dict]:
        """Create a List[dict] for multiple weapons with all stats included in process()"""

        return [self.process(weapon_dic=i) for i in weapon_dic_lst]

    def get_attachments(self, weapon_dic: dict, equipped_dic: dict = None):
        """
        Returns a pd.DataFrame if nothing is passed in equipped_dic. If a dict of attachments is passed, the function
        will return a lst of the attachment(s) effects.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.
        equipped_dic : dict
            A dict of attachment types and selected attachment name.

            {'Muzzle': 'Agency Suppressor',
             'Barrel': 'Task Force',
             'Body': 'Ember Sighting Point',
             'Underbarrel': 'Bruiser Grip',
             'Magazine': 'Salvo Fast Mag',
             'Handle': 'Serpent Wrap',
             'Stock': 'None'}

        Returns
        -------
        pd.DataFrame or list

        """

        return self._build._get_attachments(weapon_dic=weapon_dic, equipped_dic=equipped_dic)

    def _mu_shots(self, weapon_dic: dict) -> np.ndarray:
        """Returns an np.ndarray of multipliers based on accuracy and critical hit percentages"""

        ac = weapon_dic['Accuracy']
        dis = self._build.hits
        ind = np.cumsum([1 if i <= ac else 0 for i in dis])

        if self._build.consecutive:
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
        headshots = random.choices([0, 1], k=len(con_shots), weights=[1 - crit1, crit1])
        headshot_multi = weapon_dic['Crit']
        temp_lst = list(
            np.around([con_shots[i] * headshot_multi if j == 1.00 else 1.00 for i, j in enumerate(headshots)], 2))
        arr = np.array(temp_lst + ([0] * (2500 - len(temp_lst))))
        mc = range(int(weapon_dic['Mag Capacity']))
        average_shots = np.ceil(np.mean([sum([arr[k - q] for q in mc]) for k, l in enumerate(arr)]))

        return average_shots

    def damage_range(self, weapon_dic: dict) -> np.ndarray:
        """Returns a np.ndarray with the damage output of a weapon at varying distances"""

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
        """
        Calculate the damage per second output of a specific weapon over varying distances.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.
        damage_range_arr : np.ndarray
            The damage at varying distances.

        Returns
        -------
        np.ndarray

        """

        return np.multiply(np.ceil(weapon_dic['Fire Rate'] / 60), damage_range_arr)

    def time_to_kill(self, weapon_dic: dict, damage_range_arr: np.ndarray, zombie_health: float) -> np.ndarray:
        """
        Calculate the time to kill value of a specific weapon over varying distances.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.
        damage_range_arr : np.ndarray
            The damage at varying distances.
        zombie_health : float
            The zombie health value.

        Returns
        -------
        np.ndarray

        """

        dps = self.damage_per_second(weapon_dic, damage_range_arr)
        return np.around(np.add(np.divide(zombie_health, dps),
                                np.divide(range(self.max_range), weapon_dic['Velocity'])), 2)

    def shots_to_kill(self, damage_range_arr: np.ndarray, zombie_health: float) -> np.ndarray:
        """
        Calculate the shots to kill value of a specific weapon over varying distances.

        Parameters
        ----------
        damage_range_arr : np.ndarray
            The damage at varying distances.
        zombie_health : float
            The zombie health value.

        Returns
        -------
        np.ndarray

        """

        return np.around(np.divide(zombie_health, damage_range_arr), 0)

    def shoot_time(self, weapon_dic: dict) -> float:
        """
        Calculate the time spent shooting in seconds.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.

        Returns
        -------
        float

        """

        return round(weapon_dic['Mag Capacity'] / (weapon_dic['Fire Rate'] / 60), 2)

    def shoot_reload_ratio(self, weapon_dic: dict) -> float:
        """
        Calculate the shoot to reload ratio value of a specific weapon.

        This is used to see how long a weapon can output damage before having to be halted to reload.
        A weapon like the Bullfrog has a high shoot to reload ratio due to its large magazine size.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.

        Returns
        -------
        float

        """

        return 1 - round(weapon_dic['Reload'] / self.shoot_time(weapon_dic=weapon_dic), 2)

    def damage_per_max_ammo(self, weapon_dic: dict, damage_range_arr: np.ndarray) -> np.ndarray:
        """
        Calculate the damage per max ammo at varying distances.

        This assumes you were to fire all ammo in the gun and in reserve at a set distance.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.
        damage_range_arr : np.ndarray
            The damage at varying distances.

        Returns
        -------
        np.ndarray

        """

        return np.multiply(np.divide(weapon_dic['Ammo Capacity'], weapon_dic['Burst']), damage_range_arr)

    def damage_per_clip(self, damage_range_arr: np.ndarray, shots_average: np.ndarray) -> np.ndarray:
        """
        Calculate the damage per clip value of a specific weapon over varying distances.

        Parameters
        ----------
        damage_range_arr : np.ndarray
            The damage at varying distances.
        shots_average : np.ndarray
            An np.ndarray() with expected damage output based on accuracy and critical hit percentage.

        Returns
        -------
        np.ndarray

        """

        return np.around([damage_range_arr[i] * shots_average for i, j in enumerate(damage_range_arr)], 0)

    def movement_ratio(self, weapon_dic: dict) -> float:
        """
        Calculate the movement ratio for a specific weapon.

        This is used to compare the mobility of weapon against others. The closer to 1 the better the weapons overall
        movement attributes.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.

        Returns
        -------
        float

        """

        lst = {'Movement Speed': [0, 0, 0],
               'Sprinting Speed': [0, 0, 0],
               'Shooting Speed': [0, 0, 0],
               'Sprint to Fire': [0, 0, 0],
               'Aim Walking': [0, 0, 0],
               'ADS': [0, 0, 0]}

        for i in lst.keys():
            temp_lst = []
            for j in self._build.gun_names:
                if i == 'Movement Speed':
                    temp_lst.append(self._build.stats[j].movement)
                    continue
                elif i == 'Sprinting Speed':
                    temp_lst.append(self._build.stats[j].sprint)
                    continue
                elif i == 'Shooting Speed':
                    temp_lst.append(self._build.stats[j].shoot_speed)
                    continue
                elif i == 'Sprint to Fire':
                    temp_lst.append(self._build.stats[j].sprint_to_fire)
                    continue
                elif i == 'Aim Walking':
                    temp_lst.append(self._build.stats[j].aim_walking)
                    continue
                elif i == 'ADS':
                    temp_lst.append(self._build.stats[j].ads)
                    continue

            lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

        ratio = round(sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def control_ratio(self, weapon_dic: dict) -> float:
        """
        Calculate the control ratio for a specific weapon.

        This is used to compare the controllability of weapon against others. The closer to 1 the better the weapons
        overall control attributes.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.

        Returns
        -------
        float

        """

        lst = {'Vertical Recoil': [0, 0, 0],
               'Horizontal Recoil': [0, 0, 0],
               'Centering Speed': [0, 0, 0],
               'Hip Fire': [0, 0, 0]}

        for i in lst.keys():
            temp_lst = []
            for j in self._build.gun_names:
                if i == 'Vertical Recoil':
                    temp_lst.append(self._build.stats[j].vertical_recoil)
                    continue
                if i == 'Horizontal Recoil':
                    temp_lst.append(self._build.stats[j].horizontal_recoil)
                    continue
                if i == 'Centering Speed':
                    temp_lst.append(self._build.stats[j].centering_speed)
                    continue
                if i == 'Hip Fire':
                    temp_lst.append(self._build.stats[j].hip_fire)
                    continue
            lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

        ratio = 1 - round(
            sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

        return ratio

    def drop_off_ratio(self, weapon_dic: dict) -> float:
        """
        Calculate the damage drop off ratio for a specific weapon.

        This is used to compare the how much damage is lost as targets get farther away.The closer to 0 the better
        the weapons overall control attributes. A higher value means the damage starts out strong build falls off.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.

        Returns
        -------
        float

        """

        return 1 + round((weapon_dic['Damage 3'] - weapon_dic['Damage']) / weapon_dic['Damage'], 2)

    def _check_multi(self, damage_range_arr: np.ndarray, weapon_dic: dict) -> np.ndarray:
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

    def compare(self, weapon_dic: dict, zombie_health: float, zombie_armour: float = None, for_viz: bool = False):
        """
        Constructs the dict or pd.DataFrame with all comparison stats and metrics.

        Parameters
        ----------
        weapon_dic : dict
            Dict of specific weapon stats.
        zombie_health : float
            The zombie health value.
        zombie_armour : float, default None
            The zombie health value.
        for_viz : bool, default False
            Whether or not the data will be used to create plots. If False the function will return a dict.
            If True the function will return a pd.DataFrame.

        Returns
        -------
        dict or pd.DataFrame

        """

        mu = self._mu_shots(weapon_dic)
        damage_range = self._check_multi(damage_range_arr=self.damage_range(weapon_dic=weapon_dic),
                                         weapon_dic=weapon_dic)
        if zombie_armour:
            zombie_health = zombie_health + zombie_armour
            damage_range = np.multiply(np.divide(damage_range, 4), weapon_dic['Armour Damage'])

        temp_dic = {'Damage Per Clip': self.damage_per_clip(damage_range_arr=damage_range, shots_average=mu),
                    'Damage Per Second': self.damage_per_second(weapon_dic=weapon_dic, damage_range_arr=damage_range),
                    'Time To Kill': self.time_to_kill(weapon_dic=weapon_dic,
                                                      damage_range_arr=damage_range,
                                                      zombie_health=zombie_health),
                    'Shots To Kill': self.shots_to_kill(damage_range_arr=damage_range, zombie_health=zombie_health),
                    'Damage Per Max Ammo': self.damage_per_max_ammo(weapon_dic=weapon_dic,
                                                                    damage_range_arr=damage_range)
                    }

        if for_viz:
            return pd.DataFrame.from_dict(temp_dic)
        else:
            temp_dic['Temp Name'] = weapon_dic['Temp Name']
            temp_dic['Shooting Time'] = self.shoot_time(weapon_dic=weapon_dic)
            temp_dic['Shoot To Reload Ratio'] = self.shoot_reload_ratio(weapon_dic=weapon_dic)
            temp_dic['Movement Ratio'] = self.movement_ratio(weapon_dic=weapon_dic)
            temp_dic['Control Ratio'] = self.control_ratio(weapon_dic=weapon_dic)
            temp_dic['Drop Off Ratio'] = self.drop_off_ratio(weapon_dic=weapon_dic)

            return temp_dic

    def compare_multi(self, weapon_dic_lst: List[dict], zombie_health: float, zombie_armour: float = None,
                      for_viz: bool = False) -> dict:
        """
        Constructs the dict with all comparison stats and metrics; for multiple weapons.

        Parameters
        ----------
        weapon_dic_lst : List[dict]
            Dict of specific weapon stats.
        zombie_health : float
            The zombie health value.
        zombie_armour : float, default None
            The zombie health value.
        for_viz : bool, default False
            Whether or not the data will be used to create plots. If False the function will return a dict.
            If True the function will return a pd.DataFrame.

        Returns
        -------
        dict

        """

        return {i['Name']: self.compare(weapon_dic=i, zombie_health=zombie_health, zombie_armour=zombie_armour,
                                             for_viz=for_viz) for i in weapon_dic_lst}

    def build_df(self, weapon_dic_lst: List[dict], cols: List[str] = None) -> pd.DataFrame:
        """
        Constructs a pd.DataFrame with all comparison stats and metrics; for multiple weapons.

        Parameters
        ----------
        weapon_dic_lst : List[dict]
            Dict of specific weapon stats.
        cols : List[str], default None
            List of keys to include as output pd.DataFrame columns.

        Returns
        -------
        pd.DataFrame

        """

        data_n = []
        for dic in weapon_dic_lst:
            dic['Shooting Time'] = self.shoot_time(dic)
            dic['Shoot To Reload Ratio'] = self.shoot_reload_ratio(dic)
            dic['Movement Ratio'] = self.movement_ratio(dic)
            dic['Control Ratio'] = self.control_ratio(dic)
            dic['Drop Off Ratio'] = self.drop_off_ratio(dic)
            data_n.append(dic)

        if cols is None:
            return pd.DataFrame(data_n)[self._build.col_lst].set_index('Temp Name')
        else:
            return pd.DataFrame(data_n)[cols].set_index('Temp Name')

    def viz(self, weapon_df_dic: dict, keyword: str, x_limit: int, ind: int, save_image: bool = False) -> None:
        """
        Constructs a plot related to a phrase for comparing weapons.

        Parameters
        ----------
        weapon_df_dic : dict
            Dict of specific weapon stats. {MP5: mp5 DataFrame, ...}
        keyword : str
            Phrase used to denote a plot type.
            ['Damage Per Max Ammo', 'Damage Per Clip', 'Damage Per Second', 'Time To Kill', 'Shots To Kill']
        x_limit : int
            Maximum limit of x axis in the plot.
        ind : int
            Index used to populate the Value legend.
        save_image :  bool, default False
            If True will save the plot to the working directory.

        Returns
        -------
        None

        """

        n = 0
        df = pd.DataFrame()
        for i in weapon_df_dic.keys():
            df[i] = weapon_df_dic[i][keyword]
            if keyword in weapon_df_dic[i].columns:
                n += 1

        cmap = [plt.get_cmap('viridis')(1. * i / n) for i in range(n)]

        if 'Time' not in keyword:
            mu = df.mean(axis=1).astype(int)
        else:
            mu = df.mean(axis=1).round(1)

        labels = []
        count = 0
        for i in df.columns:

            if 'Time' not in keyword:
                val = df[i].astype(int)
            else:
                val = df[i].round(1)

            plt.plot(val, label=i, color=cmap[count])
            labels.append(str(val.iloc[ind]))
            count += 1
        plt.plot(mu, label='Mu', color='tab:orange', linestyle='--', alpha=1)
        labels = labels + [str(round(mu.iloc[ind], 1))]
        plt.title(keyword)
        legend1 = plt.legend(labels, title='Value at ' + str(ind), loc='upper right')  # bbox_to_anchor=(1.05, .5)
        plt.legend(title='Legend', loc='lower right')  # bbox_to_anchor=(1.05, .5)
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
        """
        Constructs a series of plots related utilizing all phrases for comparing weapons.

        Parameters
        ----------
        weapon_df_dic : dict
            Dict of specific weapon stats. {MP5: mp5 DataFrame, ...}
        x_limit : int
            Maximum limit of x axis in the plot.
        ind : int
            Index used to populate the Value legend.
        save_image :  bool, default False
            If True will save the plot to the working directory.

        Returns
        -------
        None

        """

        for keyword in ['Damage Per Max Ammo', 'Damage Per Clip', 'Damage Per Second', 'Time To Kill', 'Shots To Kill']:
            self.viz(weapon_df_dic=weapon_df_dic, keyword=keyword, x_limit=x_limit, ind=ind, save_image=save_image)
