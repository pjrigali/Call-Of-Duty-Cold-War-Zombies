# Cold War Zombies

[![Documentation Status](https://readthedocs.org/projects/call-of-duty-cold-war-zombies/badge/?version=latest)](https://call-of-duty-cold-war-zombies.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/cold-war-zombies?color=brightgreen&logoColor=lightgrey)](https://pypi.org/project/cold-war-zombies/)
[![Downloads](https://static.pepy.tech/personalized-badge/cold-war-zombies?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/cold-war-zombies)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/pjrigali/Call-Of-Duty-Cold-War-Zombies?color=blue&label=commits&logoColor=blue)](https://github.com/pjrigali)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/pjrigali/call-of-duty-cold-war-zombies/main)

This is a package for analyzing and comparing weapons in Cold War Zombies.

Weapon stats are current through Season 6 (_October 13th_). 

A demo of the package can be found here: [Demo](https://share.streamlit.io/pjrigali/call-of-duty-cold-war-zombies/main)

## Installation
[Pypi Documentation](https://pypi.org/project/cold-war-zombies/)

The package can be accessed via pip install.

    pip install cold-war-zombies

## Usage
[Read the Docs](https://call-of-duty-cold-war-zombies.readthedocs.io/en/latest/)

[Click for example](https://medium.com/@peterjrigali/best-weapon-in-zombies-9fddd33735c5)

```python
import zombie
from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze


# Input your weapon class and perk tiers.
weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}

# Build Core Classes
damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                               max_range=100)

# Set Zombie Health
zom = Health(level=60, health_cap=55, outbreak=False, multiplier=2)

# Set Attachments for weapons
MP5 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Underbarrel': 'Bruiser Grip',
    'Magazine': 'Salvo Fast Mag',
    'Handle': 'Serpent Wrap',
    'Stock': 'Raider Stock'}

PPSH = {
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
gun_lst = [
    {'weapon': 'MP5', 'nickname': 'Temp MP5', 'equipped_attachments': MP5, 'rarity': 'common',
     'pap': '0', 'accuracy': None, 'critical': None},
    {'weapon': 'PPSH', 'nickname': 'Temp PPSH', 'equipped_attachments': PPSH, 'rarity': 'common',
     'pap': '0', 'accuracy': None, 'critical': None}]

# Calculate 
analysis = Analyze(damage_profile=damage_profile, zombie_info=zom, weapon_dic_lst=gun_lst)
```

## Visualizations

The *Analyze* class will return the following plots:
* Damage Per Second
* Damage Per Max Ammo
* Damage Per Clip
* Time To Kill
* Shots To Kill

![Damage Per Second](https://miro.medium.com/max/1280/1*IyfMpo7OxpXGAm4MZd9t7Q.png)
![Damage Per Max Ammo](https://miro.medium.com/max/1280/1*eFT7lys6gkZMPO0LsOCQrA.png)
![Damage Per Clip](https://miro.medium.com/max/1280/1*Qtxn3jtbH0kRXICa7W2MfQ.png)
![Time To Kill](https://miro.medium.com/max/1280/1*VFABznePjcEVT_WdIPF5Og.png) 
![Shots To Kill](https://miro.medium.com/max/1280/1*vrw4BIZnm_mPw-V-OeXJwg.png)

## Changelog
* 1.0.0 - Base package.
* 1.0.1 - Add Classes and Viz
* 1.0.2 - Adds Grav, Ironhide, and updates inline with season 6.
* 1.0.3 - Adds Vargo.
* 1.0.4 - Update dependencies

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
