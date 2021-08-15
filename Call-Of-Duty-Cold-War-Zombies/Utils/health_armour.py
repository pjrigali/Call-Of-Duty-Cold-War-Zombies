# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:49:29 2021

@author: Peter
"""


class Health:

    def __init__(self,
                 level: int,
                 outbreak: bool = False):

        self.level = level
        self.outbreak = outbreak

        if outbreak:
            if level >= 7:
                self.level = 7
            else:
                pass
        else:
            if level >= 43:
                self.level = 43
            else:
                pass

        if outbreak:
            self.hp = [150, 510, 950, 2150, 5750, 13500, 23450, 30000][self.level - 1]
        else:
            self.hp = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 850, 950, 1050,
                       1150, 1250, 1550, 1850, 2150, 2450, 2750, 3500, 4250, 5000, 5750,
                       6500, 7900, 9300, 10700, 12100, 13500, 15250, 17000, 18750, 20500,
                       22250, 23450, 24650, 25850, 27050, 28250, 29450, 30000][self.level - 1]

    def get_health(self) -> float:

        return float(self.hp)


class Armour:

    def __init__(self,
                 level: int,
                 outbreak: bool = False):

        self.level = level
        self.outbreak = outbreak

        if outbreak:
            if level >= 7:
                self.level = 7
            else:
                pass
        else:
            if level >= 43:
                self.level = 43
            else:
                pass

        if outbreak:
            self.arm = [150, 510, 950, 2150, 5750, 13500, 23450, 30000][self.level - 1]
        else:
            self.arm = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 850, 950, 1050,
                        1150, 1250, 1550, 1850, 2150, 2450, 2750, 3500, 4250, 5000, 5750,
                        6500, 7900, 9300, 10700, 12100, 13500, 15250, 17000, 18750, 20500,
                        22250, 23450, 24650, 25850, 27050, 28250, 29450, 30000][self.level - 1]

    def get_armour(self) -> float:

        return float(self.arm / 2)
