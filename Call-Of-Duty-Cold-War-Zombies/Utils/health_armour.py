# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:49:29 2021

@author: Peter
"""


class Health:

    def __init__(self,
                 level: int,
                 health_cap: int = 55,
                 outbreak: bool = False):

        self.level = level
        self.health_cap = health_cap
        self.outbreak = outbreak

        health_lst = []
        health_amount = 150
        for num in range(self.health_cap + 1):
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
            elif 36 < num <= 85:
                health_amount += 2000
            elif 85 < num:
                health_amount = 120000
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

    def get_health(self) -> float:
        return float(self.hp)

    def get_armour(self, multiplier: int = 2) -> float:
        return float(self.hp / multiplier)
