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
            # self.hp = [150, 510, 950, 2150, 5750, 13500, 23450, 30000][self.level - 1]
        else:
            self.hp = health_lst[self.level]
            # self.hp = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 850, 950, 1050,
            #            1150, 1250, 1550, 1850, 2150, 2450, 2750, 3500, 4250, 5000, 5750,
            #            6500, 7900, 9300, 10700, 12100, 13500, 15250, 17000, 18750, 20500,
            #            22250, 23450, 24650, 25850, 27050, 28250, 29450, 30000][self.level - 1]

    def get_health(self) -> float:
        return float(self.hp)

    def get_armour(self, multiplier: int = 2) -> float:
        return float(self.hp / multiplier)
