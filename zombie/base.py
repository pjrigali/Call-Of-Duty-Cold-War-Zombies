from typing import List, Optional
import numpy as np
import zombie.weapon_stats as w
from zombie.processor import Build

_stats = {'XM4': w.Xm4,
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
_gun_names = list(_stats.keys())


def damage_range(weapon_dic: dict, max_range: int) -> np.ndarray:
    """Returns a np.ndarray with the damage output of a weapon at varying distances"""
    m = weapon_dic['Burst']
    dam1 = weapon_dic['Damage']
    dam2 = weapon_dic['Damage 2']
    dam3 = weapon_dic['Damage 3']
    ran1 = weapon_dic['Range']
    ran2 = weapon_dic['Range 2']
    ran = list(range(max_range))

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

    return np.nan_to_num(np.array(dam_lst))


def damage_per_second(weapon_dic: dict, damage_range_arr: np.ndarray) -> np.ndarray:
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


def time_to_kill(weapon_dic: dict, damage_range_arr: np.ndarray, zombie_health: float, max_range: int) -> np.ndarray:
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
    max_range : int
        Max range to calculate.

    Returns
    -------
    np.ndarray

    """
    dps = damage_per_second(weapon_dic, damage_range_arr)
    temp_lst = [zombie_health / dam if dam != 0 else 0 for dam in dps]
    return np.around(np.add(temp_lst, np.divide(range(max_range), weapon_dic['Velocity'])), 2)


def shots_to_kill(damage_range_arr: np.ndarray, zombie_health: float) -> np.ndarray:
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
    return np.around([zombie_health / dam if dam != 0 else 0 for dam in damage_range_arr], 0)


def shoot_time(weapon_dic: dict) -> float:
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


def shoot_reload_ratio(weapon_dic: dict) -> float:
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
    return 1 - round(weapon_dic['Reload'] / shoot_time(weapon_dic=weapon_dic), 2)


def damage_per_max_ammo(weapon_dic: dict, damage_range_arr: np.ndarray) -> np.ndarray:
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


def damage_per_clip(damage_range_arr: np.ndarray, shots_average: np.ndarray) -> np.ndarray:
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


def movement_ratio(weapon_dic: dict, weapon_names: Optional[List[str]] = None,
                   build_weapons: Optional[Build] = None) -> float:
    """
    Calculate the movement ratio for a specific weapon.

    This is used to compare the mobility of weapon against others. The closer to 1 the better the weapons overall
    movement attributes.

    Parameters
    ----------
    weapon_dic : dict
        Dict of specific weapon stats.
    weapon_names: list
        List of weapon names, default is None. *Optional*
    build_weapons: Build
        Built weapons, with perks and weapon tiers applied.

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

    if weapon_names is None:
        weapon_names = _gun_names
    else:
        weapon_names = weapon_names

    if build_weapons is None:
        stats = _stats
    else:
        stats = build_weapons.stats

    for i in lst.keys():
        temp_lst = []
        for weapon_name in weapon_names:
            if i == 'Movement Speed':
                temp_lst.append(stats[weapon_name].movement)
                continue
            elif i == 'Sprinting Speed':
                temp_lst.append(stats[weapon_name].sprint)
                continue
            elif i == 'Shooting Speed':
                temp_lst.append(stats[weapon_name].shoot_speed)
                continue
            elif i == 'Sprint to Fire':
                temp_lst.append(stats[weapon_name].sprint_to_fire)
                continue
            elif i == 'Aim Walking':
                temp_lst.append(stats[weapon_name].aim_walking)
                continue
            elif i == 'ADS':
                temp_lst.append(stats[weapon_name].ads)
                continue

        lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

    ratio = round(sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

    return ratio


def control_ratio(weapon_dic: dict, weapon_names: Optional[List[str]] = None,
                  build_weapons: Optional[Build] = None) -> float:
    """
    Calculate the control ratio for a specific weapon.

    This is used to compare the controllability of weapon against others. The closer to 1 the better the weapons
    overall control attributes.

    Parameters
    ----------
    weapon_dic : dict
        Dict of specific weapon stats.
    weapon_names: list
        List of weapon names, default is None. *Optional*
    build_weapons: Build
        Built weapons, with perks and weapon tiers applied.

    Returns
    -------
    float

    """
    lst = {'Vertical Recoil': [0, 0, 0],
           'Horizontal Recoil': [0, 0, 0],
           'Centering Speed': [0, 0, 0],
           'Hip Fire': [0, 0, 0]}

    if weapon_names is None:
        weapon_names = _gun_names
    else:
        weapon_names = weapon_names

    if build_weapons is None:
        stats = _stats
    else:
        stats = build_weapons.stats

    for i in lst.keys():
        temp_lst = []
        for weapon_name in weapon_names:
            if i == 'Vertical Recoil':
                temp_lst.append(stats[weapon_name].vertical_recoil)
                continue
            if i == 'Horizontal Recoil':
                temp_lst.append(stats[weapon_name].horizontal_recoil)
                continue
            if i == 'Centering Speed':
                temp_lst.append(stats[weapon_name].centering_speed)
                continue
            if i == 'Hip Fire':
                temp_lst.append(stats[weapon_name].hip_fire)
                continue
        lst[i] = [min(temp_lst), max(temp_lst), weapon_dic[i]]

    ratio = 1 - round(
        sum([(lst[i][2] - lst[i][0]) / (lst[i][1] - lst[i][0]) for i in lst.keys()]) / len(lst.keys()), 2)

    return ratio


def drop_off_ratio(weapon_dic: dict) -> float:
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
