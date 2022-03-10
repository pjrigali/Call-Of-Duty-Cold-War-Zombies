from dataclasses import dataclass
from typing import Optional, List
import zombie.weapon_stats as w


_stats = {'XM4': w.Xm4,
          'AK47': w.Ak47,
          'Krig': w.Krig,
          'QBZ': w.Qbz,
          'FFAR': w.Ffar,
          'Groza': w.Groza,
          'FARA': w.Fara,
          'C58': w.C58,
          'EM2': w.Em2,
          'Grav': w.Grav,
          'Vargo': w.Vargo,
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

rare_level = {'common': 1.00, 'green': 1.50, 'blue': 3.00, 'purple': 6.00, 'orange': 12.00}
pack_level = {'0': 1.00, '1': 2.00, '2': 4.00, '3': 8.00}


@dataclass
class ModifiedWeapon:

    def __init__(self, weapon_name: str, nickname: Optional[str] = None, equipped_attachments: Optional[dict] = None,
                 rarity: Optional[str] = None, pap: Optional[str] = None, accuracy: Optional[float] = None,
                 critical: Optional[float] = None):
        d = _stats[weapon_name]
        self._default_stats = {'Name': d.name,
                                 'Temp Name': d.temp_name,
                                 'Damage': d.damage_1,
                                 'Damage 2': d.damage_2,
                                 'Damage 3': d.damage_3,
                                 'Range': d.range_1,
                                 'Range 2': d.range_2,
                                 'Fire Rate': d.fire_rate,
                                 'Velocity': d.velocity,
                                 'Armour Damage': d.armour_damage,
                                 'Melee Quickness': d.melee,
                                 'Movement Speed': d.movement,
                                 'Sprinting Speed': d.sprint,
                                 'Shooting Speed': d.shoot_speed,
                                 'Sprint to Fire': d.sprint_to_fire,
                                 'Aim Walking': d.aim_walking,
                                 'ADS': d.ads,
                                 'Vertical Recoil': d.vertical_recoil,
                                 'Horizontal Recoil': d.horizontal_recoil,
                                 'Centering Speed': d.centering_speed,
                                 'Idle Sway': d.idle_sway,
                                 'Flinch': d.flinch,
                                 'Hip Fire': d.hip_fire,
                                 'Mag Capacity': d.mag_capacity,
                                 'Reload': d.reload,
                                 'Starting Ammo': d.starting_ammo,
                                 'Ammo Capacity': d.ammo_capacity,
                                 'Burst': d.burst,
                                 'PAP Burst': d.pap_burst,
                                 'Long Shot': d.long_shot,
                                 'Crit': d.critical,
                                 'Long': d.long,
                                 'Close': d.close,
                                 'Salvage': d.salvage,
                                 'Equipment': d.equipment,
                                 'Attachments': d.attachments,
                                 'Weapon Type': d.weapon_type,
                                 'Accuracy': d.gun_acc_value,
                                 'Critical': d.gun_critical_value,
                                 'Pack': d.pack,
                                 'Rare': d.rare,
                                 'Muzzle': d.muzzle,
                                 'Barrel': d.barrel,
                                 'Body': d.body,
                                 'Underbarrel': d.under_barrel,
                                 'Magazine': d.magazine,
                                 'Handle': d.handle,
                                 'Stock': d.stock,
                                 }

        self._modified_stats = self._default_stats

        if nickname is not None:
            self._modified_stats['Temp Name'] = nickname

        if accuracy is not None:
            self._modified_stats['Accuracy'] = accuracy

        if critical is not None:
            self._modified_stats['Critical'] = critical

        if rarity is not None:
            self._modified_stats['Rare'] = rarity
            self._modified_stats['Damage'] = self._modified_stats['Damage'] * self.rare_level[rarity]
            self._modified_stats['Damage 2'] = self._modified_stats['Damage 2'] * self.rare_level[rarity]
            self._modified_stats['Damage 3'] = self._modified_stats['Damage 3'] * self.rare_level[rarity]

        if pap is not None:
            if pap != '0':
                self._modified_stats['Pack'] = pap
                self._modified_stats['Damage'] = self._modified_stats['Damage'] * self.pack_level[pap] * \
                                                 self._modified_stats['PAP Burst']
                self._modified_stats['Damage 2'] = self._modified_stats['Damage 2'] * self.pack_level[pap] * \
                                                   self._modified_stats['PAP Burst']
                self._modified_stats['Damage 3'] = self._modified_stats['Damage 3'] * self.pack_level[pap] * \
                                                   self._modified_stats['PAP Burst']
                self._modified_stats['Mag Capacity'] = self._modified_stats['Mag Capacity'] / \
                                                       self._modified_stats['PAP Burst']

        temp_dic = self._apply_multipliers(weapon_multi=self.get_weapon_classes, perk_multi=self.get_perk_classes,
                                           weapon_dic=self._modified_stats)

        if equipped_attachments is not None:
            effect_lst = self._get_attachments(weapon_dic=temp_dic, equipped_dic=equipped_attachments)
            final_dic = self._apply_attachments(weapon_dic=temp_dic, attachment_lst=effect_lst)

            for part in ['Muzzle', 'Barrel', 'Body', 'Underbarrel', 'Magazine', 'Handle', 'Stock']:
                if part in equipped_attachments.keys():
                    final_dic[part] = {equipped_attachments[part]: final_dic[part][equipped_attachments[part]]}
                else:
                    final_dic[part] = {'None': 'None'}
            temp_dic = final_dic

        self._modified_stats = temp_dic

    def __repr__(self):
        return self._default_stats['Name']

    @property
    def default_stats(self) -> dict:
        return self._default_stats

    @property
    def modified_stats(self) -> dict:
        return self._modified_stats
