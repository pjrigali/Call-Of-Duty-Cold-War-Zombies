# Zombies Module

Zombies Module is a Python library for analyzing weapons in Cold War Zombies.

Weapon stats are current through Season 4. Zombie health cap is set to level 43.

## Usage

```python
import pandas as pd
from Utils import health_armour as z
from Utils import analysis as a
from Utils import processor as p
import warnings
pd.set_option('display.max_columns', None) 

# Input your weapon class and perk tiers.
base = p.Build(weapon_class_levels=['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
               perk_class_levels=['5', '5', '5'])
aa = a.Analyze()

# Set Zombie Health and Armour
zom = z.Health(level=12, outbreak=False).get_health()
ar = z.Armour(level=12, outbreak=False).get_armour()

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

# Returns a DataFrame comparing selected weapons
guns = base.process_multi([
    ['MP5', 'Temp MP5', equipped1, 'common', '0', None, None],
    ['PPSH', 'Temp PPSH', equipped2, 'common', '0', None, None]])

col_lst = [
    'Name', 'Temp Name', 'Damage', 'Damage 2', 'Damage 3', 'Range',
    'Range 2', 'Fire Rate', 'Velocity', 'Armour Damage', 'Melee Quickness',
    'Movement Speed', 'Sprinting Speed', 'Shooting Speed', 'Sprint to Fire',
    'Aim Walking', 'ADS', 'Vertical Recoil', 'Horizontal Recoil',
    'Centering Speed', 'Idle Sway', 'Flinch', 'Hip Fire', 'Mag Capacity',
    'Reload', 'Ammo Capacity', 'Accuracy', 'Critical', 'Pack', 'Rare',
    'Shoot To Reload Ratio', 'Movement Ratio', 'Control Ratio', 'Drop Off Ratio']

gun_df = pd.DataFrame(guns)[col_lst].set_index('Temp Name')

compare_lst = []
for i in guns:
    compare_lst.append(aa.compare(i, zom, True, False))
```

## Visualizations

```python
aa.viz(gun_lst=compare_lst, keyword='Damage Per Max Ammo', x_limit=40, ind=5, save_image=False)
```
![Damage Per Max Ammo](https://miro.medium.com/max/1280/1*jiqlsA4CpFPwBMHk93DBFw.png)
```python
aa.viz(gun_lst=compare_lst, keyword='Damage Per Clip', x_limit=40, ind=5, save_image=False)
```
![Damage Per Clip](https://miro.medium.com/max/1280/1*v1flKiPd1OuTpNM8Zda9bw.png)
```python
aa.viz(gun_lst=compare_lst, keyword='Damage Per Second', x_limit=40, ind=5, save_image=False)
```
![Damage Per Second](https://miro.medium.com/max/1280/1*Ygk3yoH5y4Lvx7Th9s5mqw.png)
```python
aa.viz(gun_lst=compare_lst, keyword='Time To Kill', x_limit=40, ind=5, save_image=False)
```
![Time To Kill](https://miro.medium.com/max/1280/1*tmtdPDrGQF4BaydbqdDjhQ.png)
```python
aa.viz(gun_lst=compare_lst, keyword='Shots To Kill', x_limit=40, ind=5, save_image=False)
```    
![Shots To Kill](https://miro.medium.com/max/1280/1*Cvj_RG31PISq9bNgo1YV5Q.png)
```python
# To get a single weapon stats. Returns a dictionary
equipped3 = {
    'Muzzle': 'Agency Suppressor',
    'Barrel': 'Task Force',
    'Body': 'Ember Sighting Point',
    'Magazine': 'Salvo Fast Mag',
    'Stock': 'Dual Wield'}

t_d = base.process(weapon='Magnum', 
                   nickname='Temp Magnum', 
                   equipped_attachments=equipped3, 
                   rarity='common',
                   pap='0',
                   accuracy=False, 
                   critical=False)[0]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)