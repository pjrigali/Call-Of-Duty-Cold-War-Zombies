# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:49:29 2021

@author: Peter
"""


class Health:
    """
    **Description**

    Get zombie health and armour values. Creates a list of zombie health values. Uses desired level and a health cap
    value to compute health level.

    **Parameters**

    level : int
        Desired zombie level to test weapon strength at.
    health_cap : int
        The level when zombie health values stop increasing. In season 5 this is level 55. Season 4 was 85.
    outbreak : bool, default False
        If level is True, parameter is referencing an outbreak level.

    **Returns**

     float

    **Example**

    >>> from zombie import health_armour as z
    >>> zombie = z.Health(level=20, health_cap=55, outbreak=False)
    >>> zombie_health = zombie.get_health() # 2450
    >>> zombie_armour = zombie.get_armour(multiplier=2) # 1225

    The multiplier is what number you would like to divide the health number by to get armour health. Prior to season 4
    this was half the zombies health.
    """
    def __init__(self, level: int, health_cap: int = 55, outbreak: bool = False, multiplier: int = 2):

        self.level = level
        self.health_cap = health_cap
        self.outbreak = outbreak
        self.multiplier = multiplier

        health_lst = []
        health_amount = 150
        for num in range(max(self.health_cap, self.level) + 1):
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
                # health_amount = 120000
            health_lst.append(health_amount)

        if outbreak:
            out_health_lst = []
            for num in range(self.level):
                if num <= 1:
                    out_health_lst.append(150)
                elif 1 < num < 10:
                    out_health_lst.append(health_lst[1 + (num * 6)])
                else:
                    out_health_lst.append(health_lst[-1])

            self.hp = out_health_lst[self.level]
        else:
            self.hp = health_lst[self.level]
        self.armour = float(int(self.hp / self.multiplier))

    @property
    def get_health(self) -> float:
        """Returns zombie health value."""
        return float(self.hp)

    @property
    def get_armour(self) -> float:
        """Returns zombie armour value. Multiplier is an int you want to divide the zombie health level by
            If 2, the armour health will be half the zombie health value.

        **Parameters**

        multiplier : int, default is 2
            Divisor to get armour health value

        """
        return float(self.armour)

    @get_armour.setter
    def get_armour(self, val):
        """Setter for updating the multiplier and armour."""
        self.multiplier = val
        self.armour = float(int(self.hp / self.multiplier))
