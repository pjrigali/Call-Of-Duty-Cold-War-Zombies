# Cold War Zombies
[![Documentation Status](https://readthedocs.org/projects/call-of-duty-cold-war-zombies/badge/?version=latest)](https://call-of-duty-cold-war-zombies.readthedocs.io/en/latest/?badge=latest)

This is a package for analyzing and comparing weapons in Cold War Zombies.

Weapon stats are current through Season 5 (_pre August 16 update_). 
[Patch Notes](https://www.ravensoftware.com/community/2021/08/call-of-duty-bocw-warzone-season-five-patch-notes)

## Installation
    pip install cold-war-zombies

**Currently this project is down from pypi while undergoing final touches**

## Usage
[Read the Docs](https://call-of-duty-cold-war-zombies.readthedocs.io/en/latest/)

[Click for example](https://medium.com/@peterjrigali/best-weapon-in-zombies-9fddd33735c5)

```python
import zombie
from zombie.health_armour import Health
from zombie.analysis import Analyze


# Input your weapon class and perk tiers.
weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
analysis = Analyze(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                     max_range=100)

# Set Zombie Health
zom_health = Health(level=20, health_cap=55, outbreak=False, multiplier=2)
zombie_health = zom_health.get_health
zombie_armour = zom_health.get_armour

# Set Attachments for weapons
equipped1 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Raider Stock'}

equipped2 = {
    'Muzzle': 'GRU Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'VDV Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'KGB Skeletal Stock'}

# Returns a Dict with the specific weapon stats, adjusted for attachments.
# Accuracy and Critical values (float) can be found in game at 
# Barracks\\Combat Record\\Zombies\\Weapon Name.
guns = analysis.process_multi(weapon_dic_lst=[
    {'weapon': 'MP5', 'nickname': 'Temp MP5', 'equipped_attachments': equipped1, 'rarity': 'common',
     'pap': '0', 'accuracy': None, 'critical': None},
    {'weapon': 'PPSH', 'nickname': 'Temp PPSH', 'equipped_attachments': equipped2, 'rarity': 'common',
     'pap': '0', 'accuracy': None, 'critical': None}])

# Convert to a DataFrame.
gun_df = analysis.build_df(weapon_dic_lst=guns, cols=None)
```

## Visualizations

```python
# Build Data for Viz.
weapon_compare_dic = analysis.compare_multi(weapon_dic_lst=guns, zombie_health=zombie_health,
                                            zombie_armour=zombie_armour, for_viz=True)

# Return all visualizations.
analysis.viz_all(weapon_df_dic=weapon_compare_dic, x_limit=40, ind=5, save_image=False)

# Return a single visualization.
analysis.viz(weapon_df_dic=weapon_compare_dic, keyword='Damage Per Second', x_limit=40, ind=5, 
             save_image=False)
```
![Damage Per Second](https://miro.medium.com/max/1280/1*IyfMpo7OxpXGAm4MZd9t7Q.png)
```python
analysis.viz(weapon_df_dic=weapon_compare_dic, keyword='Damage Per Max Ammo', x_limit=40, ind=5, 
             save_image=False)
```
![Damage Per Max Ammo](https://miro.medium.com/max/1280/1*eFT7lys6gkZMPO0LsOCQrA.png)
```python
analysis.viz(weapon_df_dic=weapon_compare_dic, keyword='Damage Per Clip', x_limit=40, ind=5, 
             save_image=False)
```
![Damage Per Clip](https://miro.medium.com/max/1280/1*Qtxn3jtbH0kRXICa7W2MfQ.png)
```python
analysis.viz(weapon_df_dic=weapon_compare_dic, keyword='Time To Kill', x_limit=40, ind=5, 
             save_image=False)
```
![Time To Kill](https://miro.medium.com/max/1280/1*VFABznePjcEVT_WdIPF5Og.png)
```python
analysis.viz(weapon_df_dic=weapon_compare_dic, keyword='Shots To Kill', x_limit=40, ind=5, 
             save_image=False)
```    
![Shots To Kill](https://miro.medium.com/max/1280/1*vrw4BIZnm_mPw-V-OeXJwg.png)
```python
# Return the attachments and their effects for a specific gun
equipped_mp5 = {'Muzzle': 'Agency Suppressor',
                'Barrel': 'Task Force',
                'Body': 'Ember Sighting Point',
                'Underbarrel': 'Bruiser Grip',
                'Magazine': 'Salvo Fast Mag',
                'Handle': 'Serpent Wrap',
                'Stock': 'Raider Stock'}

mp5 = {'weapon': 'MP5', 'nickname': 'Temp MP5', 'equipped_attachments': equipped_mp5, 'rarity': 'common',
       'pap': '0', 'accuracy': None, 'critical': None}
mp5_dic = analysis.process(weapon_dic=mp5)
attach_df = analysis.get_attachments(weapon_dic=mp5_dic, equipped_dic=None)

# Returns the effects as a list  from the attachments
effects_lst = analysis.get_attachments(weapon_dic=mp5_dic, equipped_dic=equipped_mp5)]

# ['+ 35% Increased Equipment Drop Chance', '+ 7% Vertical Recoil Control', '- 25% Effective Damage Range', 
# '+ 6% Damage', '+ 50% Effective Damage Range', '+ 75% Bullet Velocity', '- 25% Max Starting Ammo', 
# '- 20% Vertical Recoil Control', '- 15% Horizontal Recoil Control', '+ 30% Increased Salvage Drop Rate',
# '+ 25% Hip Fire Accuracy', '- 10% Sprint to Fire Time', '- 10% Aim Down Sight Time', '+ 40% Melee Quickness', 
# '+ 3% Movement Speed', '+ 3% Shooting Move Speed', '+ 3% Sprinting Move Speed', '+ 3% Aim Walking Movement Speed', 
# '+ 33% Magazine Ammo Capacity', '+ 40% Reload Quickness', '+ 33% Max Starting Ammo', '+ 33% Ammo Capacity', 
# '- 25% Aim Down Sight Time', '+ 25% Aim Down Sight Time', '- 10% Sprint to Fire Time', '+ 30% Sprint to Fire Time', 
# '+ 10% Aim Walking Movement Speed', '- 30% Hip Fire Accuracy']
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
