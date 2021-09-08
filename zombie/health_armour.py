# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:49:29 2021

@author: Peter
"""
from typing import Optional
from dataclasses import dataclass


@dataclass
class Health:
    """

    Get zombie health and armour values. Creates a list of zombie health values. Uses desired level and a health cap
    value to compute health level.

    :param level: Desired zombie level to test weapon strength at.
    :type level: int
    :param health_cap: The level when zombie health values stop increasing. In season 5 this is level 55.
        Season 4 was 85. *Optional*
    :type health_cap: int
    :param outbreak: If level is True, parameter is referencing an outbreak level, default is False. *Optional*
    :type outbreak: bool
    :param multiplier: Value used to calculate armour, default is 2. *Optional*
    :type multiplier: int
    :example:
        >>> from health_armour import Health
        >>> zombie = Health(level=20, health_cap=55, outbreak=False, multiplier=2)
        >>> zombie_health = zombie.get_health # 2,450
        >>> zombie_armour = zombie.get_armour # 1,225
    :note: The multiplier is what number you would like to divide the health number by to get armour health.
        Prior to season 4 this was half the zombies health.
    """
    def __init__(self, level: int, health_cap: Optional[int] = 55, outbreak: Optional[bool] = False,
                 multiplier: Optional[int] = 2):
        self._level = level
        self._health_cap = health_cap
        self._outbreak = outbreak
        self._multiplier = multiplier

        health_lst = []
        health_amount = 150
        for num in range(max(self._health_cap, self._level) + 1):
            if 1 < num <= 11:
                health_amount += 60
            elif 11 < num <= 16:
                health_amount += 100
            elif 16 < num <= 21:
                health_amount += 300
            elif 21 < num <= 26:
                health_amount += 750
            elif 26 < num <= 31:
                health_amount += 1400
            elif 31 < num <= 36:
                health_amount += 1750
            elif 36 < num <= health_cap:
                health_amount += 2000
            elif health_cap < num:
                pass
            health_lst.append(health_amount)

        if outbreak:
            out_health_lst = []
            for num in range(self._level):
                if num <= 1:
                    out_health_lst.append(150)
                elif 1 < num < 10:
                    out_health_lst.append(health_lst[1 + (num * 6)])
                else:
                    out_health_lst.append(health_lst[-1])

            self._hp = out_health_lst[self._level]
        else:
            self._hp = health_lst[self._level]
        self._armour = float(int(self._hp / self._multiplier))

    def __repr__(self):
        return "Zombie Health"

    @property
    def get_health(self) -> float:
        """Returns zombie health value."""
        return float(self._hp)

    @property
    def get_armour(self) -> float:
        """Returns zombie armour value. Multiplier is an int you want to divide the zombie health level by
            If 2, the armour health will be half the zombie health value."""
        return float(self._armour)

    @get_armour.setter
    def get_armour(self, val):
        """Setter for updating the multiplier and armour value."""
        self._multiplier = val
        self._armour = float(int(self._hp / self._multiplier))
