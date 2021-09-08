# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:08:22 2021

@author: Peter
"""
from typing import List, Optional
from dataclasses import dataclass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from zombie.processor import DamageProfile, ModifiedWeapon
from zombie.health_armour import Health
from zombie.base import damage_range, damage_per_second, damage_per_clip, damage_per_max_ammo, drop_off_ratio
from zombie.base import shoot_reload_ratio, time_to_kill, shoot_time, shots_to_kill, control_ratio, movement_ratio
random.seed(1)

col_lst = ['Name', 'Temp Name', 'Damage', 'Damage 2', 'Damage 3', 'Range',
           'Range 2', 'Fire Rate', 'Velocity', 'Armour Damage', 'Melee Quickness',
           'Movement Speed', 'Sprinting Speed', 'Shooting Speed', 'Sprint to Fire',
           'Aim Walking', 'ADS', 'Vertical Recoil', 'Horizontal Recoil',
           'Centering Speed', 'Idle Sway', 'Flinch', 'Hip Fire', 'Mag Capacity',
           'Reload', 'Ammo Capacity', 'Accuracy', 'Critical', 'Pack', 'Rare', 'Shooting Time',
           'Shoot To Reload Ratio', 'Movement Ratio', 'Control Ratio', 'Drop Off Ratio']


@dataclass
class Analyze:
    """

    Constructs  dicts, pd.DataFrames and visualizations for comparing various weapons.

    :param damage_profile: DamageProfile class object.
    :type damage_profile: DamageProfile
    :param zombie_info: Health class object.
    :type zombie_info: Health
    :param weapon_dic_lst: List of weapons and weapon info.
    :type weapon_dic_lst: dict
    :param columns_lst: Select columns to highlight, default is None. *Optional*
    :type columns_lst: List[str]
    :param x_limit: X limit on the graphs, default is 75. *Optional*
    :type x_limit: int
    :param viz_index_point: Reference point on the graphs, default is 40. *Optional*
    :type viz_index_point: int
    :param save_image: If True, will save the plots, default is False. *Optional*
    :type save_image: bool
    :example:
    >>> from zombie.processor import DamageProfile
    >>> from zombie.analysis import Analyze
    >>> weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
    >>>                        'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    >>> perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
    >>> damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
    >>>                                max_range=100)
    >>> analysis = Analyze(damage_profile=damage_profile)

    """
    def __init__(self, damage_profile: DamageProfile, zombie_info: Health, weapon_dic_lst: List[dict],
                 columns_lst: Optional[List[str]] = None, x_limit: Optional[int] = 100,
                 viz_index_point: Optional[int] = 3, save_image: Optional[bool] = False):
        self._DamageProfile = damage_profile
        self._perk_dict = damage_profile.get_perk_classes
        self._weapon_type_dict = damage_profile.get_weapon_classes
        self._max_range = self._DamageProfile.max_range

        self._zombie_health = zombie_info.get_health
        self._zombie_armour = zombie_info.get_armour
        self._ModifiedWeapons = self._process_multi(weapon_dic_lst=weapon_dic_lst)
        self._compare_info_for_plots = self._compare_multi(weapon_dic_lst=self._ModifiedWeapons,
                                                           zombie_health=self._zombie_health,
                                                           zombie_armour=self._zombie_armour,
                                                           for_viz=True)

        if columns_lst is None:
            self._col_lst = col_lst
        else:
            self._col_lst = col_lst

        self._x_limit = x_limit
        self._viz_index_point = viz_index_point
        self._save_image = save_image

    def __repr__(self):
        return "Analysis"

    @property
    def weapons_lst(self) -> List[ModifiedWeapon]:
        """Returns a list of ModifiedWeapons"""
        return self._ModifiedWeapons

    @property
    def weapons_df(self) -> pd.DataFrame:
        """Returns a DataFrame of weapon stats"""
        data_n = []
        for dic in self._ModifiedWeapons:
            dic = dic.modified_stats
            dic['Shooting Time'] = shoot_time(weapon_dic=dic)
            dic['Shoot To Reload Ratio'] = shoot_reload_ratio(weapon_dic=dic)
            dic['Movement Ratio'] = movement_ratio(weapon_dic=dic)
            dic['Control Ratio'] = control_ratio(weapon_dic=dic)
            dic['Drop Off Ratio'] = drop_off_ratio(weapon_dic=dic)
            data_n.append(dic)

        return pd.DataFrame(data_n)[self._col_lst].set_index('Temp Name').T

    @property
    def damage_per_second_plot(self):
        """Returns Damage Per Second Plot"""
        return self.viz(weapon_df_dic=self._compare_info_for_plots,
                        keyword='Damage Per Second',
                        x_limit=self._x_limit,
                        ind=self._viz_index_point,
                        save_image=self._save_image)

    @property
    def damage_per_max_ammo_plot(self):
        """Returns Damage Per Max Ammo Plot"""
        return self.viz(weapon_df_dic=self._compare_info_for_plots,
                        keyword='Damage Per Max Ammo',
                        x_limit=self._x_limit,
                        ind=self._viz_index_point,
                        save_image=self._save_image)

    @property
    def damage_per_clip_plot(self):
        """Returns Damage Per Clip Plot"""
        return self.viz(weapon_df_dic=self._compare_info_for_plots,
                        keyword='Damage Per Clip',
                        x_limit=self._x_limit,
                        ind=self._viz_index_point,
                        save_image=self._save_image)

    @property
    def time_to_kill_plot(self):
        """Returns Time To Kill Plot"""
        return self.viz(weapon_df_dic=self._compare_info_for_plots,
                        keyword='Time To Kill',
                        x_limit=self._x_limit,
                        ind=self._viz_index_point,
                        save_image=self._save_image)

    @property
    def shots_to_kill_plot(self):
        """Returns Shots To Kill Plot"""
        return self.viz(weapon_df_dic=self._compare_info_for_plots,
                        keyword='Shots To Kill',
                        x_limit=self._x_limit,
                        ind=self._viz_index_point,
                        save_image=self._save_image)

    def _process(self, weapon_dic: dict) -> ModifiedWeapon:
        """Create a ModifiedWeapon Class for a weapon with all stats. Including attachments,
        perk and weapon tier effects"""
        new_weapon_dic = {}
        for i in ['weapon', 'nickname', 'equipped_attachments', 'rarity', 'pap', 'accuracy', 'critical']:
            if i in weapon_dic.keys():
                new_weapon_dic[i] = weapon_dic[i]
            else:
                new_weapon_dic[i] = None

        return ModifiedWeapon(weapon_name=new_weapon_dic['weapon'], nickname=new_weapon_dic['nickname'],
                              equipped_attachments=new_weapon_dic['equipped_attachments'],
                              rarity=new_weapon_dic['rarity'], pap=new_weapon_dic['pap'],
                              accuracy=new_weapon_dic['accuracy'], critical=new_weapon_dic['critical'],
                              weapon_class_levels=self._DamageProfile.get_weapon_classes,
                              perk_class_levels=self._DamageProfile.get_perk_classes)

    def _process_multi(self, weapon_dic_lst: List[dict]) -> List[ModifiedWeapon]:
        """Create a List[ModifiedWeapon] for multiple weapons with all stats included in process()"""
        if len(weapon_dic_lst) > 6:
            print(), print('If more than 6 guns included legends will overlap.')
        return [self._process(weapon_dic=i) for i in weapon_dic_lst]

    def _mu_shots(self, weapon_dic: dict) -> np.ndarray:
        """Returns an np.ndarray of multipliers based on accuracy and critical hit percentages"""
        ac = weapon_dic['Accuracy']
        dis = self._DamageProfile.hits
        ind = np.cumsum([1 if i <= ac else 0 for i in dis])

        if self._DamageProfile.consecutive:
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

    def _compare(self, weapon_dic: dict, zombie_health: Optional[float], zombie_armour: Optional[float],
                 for_viz: Optional[bool] = False):
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
        if zombie_health is None:
            zombie_health = self._zombie_health
        if zombie_armour is None:
            zombie_armour = self._zombie_armour

        mu = self._mu_shots(weapon_dic)
        _dr = self._check_multi(damage_range_arr=damage_range(weapon_dic=weapon_dic, max_range=self._max_range),
                                weapon_dic=weapon_dic)
        if zombie_armour:
            zombie_health = zombie_health + zombie_armour
            _dr = np.multiply(np.divide(_dr, 4), weapon_dic['Armour Damage'])

        temp_dic = {'Damage Per Clip': damage_per_clip(damage_range_arr=_dr, shots_average=mu),
                    'Damage Per Second': damage_per_second(weapon_dic=weapon_dic, damage_range_arr=_dr),
                    'Time To Kill': time_to_kill(weapon_dic=weapon_dic, damage_range_arr=_dr,
                                                 zombie_health=zombie_health, max_range=self._max_range),
                    'Shots To Kill': shots_to_kill(damage_range_arr=_dr, zombie_health=zombie_health),
                    'Damage Per Max Ammo': damage_per_max_ammo(weapon_dic=weapon_dic,  damage_range_arr=_dr)
                    }

        if for_viz:
            return pd.DataFrame.from_dict(temp_dic)
        else:
            temp_dic['Temp Name'] = weapon_dic['Temp Name']
            temp_dic['Shooting Time'] = shoot_time(weapon_dic=weapon_dic)
            temp_dic['Shoot To Reload Ratio'] = shoot_reload_ratio(weapon_dic=weapon_dic)
            temp_dic['Movement Ratio'] = movement_ratio(weapon_dic=weapon_dic)
            temp_dic['Control Ratio'] = control_ratio(weapon_dic=weapon_dic)
            temp_dic['Drop Off Ratio'] = drop_off_ratio(weapon_dic=weapon_dic)
            return temp_dic

    def _compare_multi(self, weapon_dic_lst: List[ModifiedWeapon], zombie_health: Optional[float],
                       zombie_armour: Optional[float] = None, for_viz: Optional[bool] = False) -> dict:
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
        if zombie_health is None:
            zombie_health = self._zombie_health
        if zombie_armour is None:
            zombie_armour = self._zombie_armour

        return {i.modified_stats['Name']: self._compare(weapon_dic=i.modified_stats,
                                                        zombie_health=zombie_health,
                                                        zombie_armour=zombie_armour,
                                                        for_viz=for_viz) for i in weapon_dic_lst}

    def viz(self, weapon_df_dic: dict, keyword: str, x_limit: Optional[int] = 75, ind: Optional[int] = 40,
            save_image: Optional[bool] = False) -> None:
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

        if "Time" not in keyword and "Shots" not in keyword:
            if np.max(np.max(df)) > 100000:
                df = df / 1000
                keyword = keyword + ' (in 1,000s)'

        for col in df.columns:
            df[col] = np.nan_to_num(np.array(df[col]), posinf=0, neginf=0)

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

    def viz_all(self, weapon_df_dic: dict, x_limit: Optional[int] = 75, ind: Optional[int] = 40,
                save_image: Optional[bool] = False) -> None:
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
