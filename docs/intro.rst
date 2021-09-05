Intro
*****

.. meta::
   :description: Landing page for cold-war-zombies.
   :keywords: Call of Duty, Python, Data Science, zombies

`PYPI Page <https://pypi.org/project/cold-war-zombies/>`_

.. code-block::

    pip install cold-war-zombies

Usage
-----

Building the package:

.. code-block:: python

    import zombie
    from zombie.analysis import Analyze
    from zombie.health_armour import Health
    weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                           'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
    perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
    analysis = Analyze(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels, max_range=100)

    zom = Health(level=60, health_cap=55, outbreak=False, multiplier=2)
    zombie_health = zom.get_health
    zombie_armour = zom.get_armour

Within **weapon_class_levels** and **perk_class_levels** you should input your tier level for the respective item.

For **Health** put in the desired zombie level and current zombie health cap.

Set **outbreak** to True if you would like to look at the results for outbreak.

More Info
---------
`Github <https://github.com/pjrigali/Call-Of-Duty-Cold-War-Zombies/tree/main/zombie>`_

`Home Page <https://medium.com/@peterjrigali/best-weapon-in-zombies-9fddd33735c5>`_
