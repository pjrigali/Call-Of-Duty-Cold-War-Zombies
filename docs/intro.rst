Intro
*****

.. meta::
   :description: Landing page for cold-war-zombies.
   :keywords: Call of Duty, Python, Data Science, zombies

This is a package for analyzing and comparing weapons in Cold War Zombies.

`Pypi link <https://pypi.org/project/cold-war-zombies/>`_

.. code-block::

    pip install cold-war-zombies

Usage
-----
Building the package:

.. code-block:: python

    import zombie
    from zombie.health_armour import Health
    from zombie.processor import DamageProfile
    from zombie.analysis import Analyze

    # User inputs
    weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                           'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}

    # Core Classes
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
Within **weapon_class_levels** and **perk_class_levels** you should input your tier level for the respective item.

For **Health** input the desired zombie level and current zombie health cap.

Set **outbreak** to True if you would like to look at the results for outbreak.

More Info
---------
`Github <https://github.com/pjrigali/Call-Of-Duty-Cold-War-Zombies/tree/main/zombie>`_

`Home Page <https://medium.com/@peterjrigali/best-weapon-in-zombies-9fddd33735c5>`_
