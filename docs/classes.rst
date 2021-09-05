Classes
*******

.. meta::
   :description: This chapter describes various classes for Analyzing and Visualizing stats.
   :keywords: Call of Duty, Python, Data Science, zombies

This chapter documents the Classes used in this package.

Health
------
.. :currentmodule:: health_armour

.. class:: Health(level, health_cap, outbreak, multiplier):

    Get zombie health and armour values. Creates a list of zombie health values. Uses desired level and a health cap
    value to compute health level.

    :param level: Desired zombie level to test weapon strength at.
    :type level: int
    :param health_cap: The level when zombie health values stop increasing. In season 5 this is level 55. Season 4 was 85.
    :type health_cap: int
    :param outbreak: If level is True, parameter is referencing an outbreak level.
    :type outbreak: bool, default False
    :example:
        .. code-block:: python

            from health_armour import Health
            zombie = Health(level=20, health_cap=55, outbreak=False, multiplier=2)
            zombie_health = zombie.get_health # 2450
            zombie_armour = zombie.get_armour # 1225
    :note: The multiplier is what number you would like to divide the health number by to get armour health. Prior to season 4
        this was half the zombies health.

.. autosummary::
    zombie.health_armour.Health.get_health
    zombie.health_armour.Health.get_armour

Analysis
--------
.. :currentmodule:: analysis

.. class:: Analyze(level, health_cap, outbreak, multiplier):

    Constructs  dicts, pd.DataFrames and visualizations for comparing various weapons.
    Applies buffs from attachments.

    :param weapon_class_levels: User input tiers for each weapon class. Use str value betweem 0 and 5.
    :type weapon_class_levels: dict, default None
    :param perk_class_levels: User input tiers for each perk. Use str value value between 0 and 5.
    :type perk_class_levels: dict, default None
    :param max_range: User desired maximum distance for the function to compute values for. (In meters)
    :type max_range: int
    :example:
        .. code-block:: python

            from zombie.analysis import Analyze
            weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                                   'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
            perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
            analysis = Analyze(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                                 max_range=100)
    :note: By default the values are set to 0.
        User inputs change these and the effects are applied across the weapons:

.. autosummary::
    zombie.analysis.Analyze

Build
-----
.. :currentmodule:: processor

.. class:: Build(weapon_class_levels, perk_class_levels):

    Constructs  dicts, pd.DataFrames and visualizations for comparing various weapons.
    Applies buffs from attachments.

    :param weapon_class_levels: User input tiers for each weapon class. Use str value betweem 0 and 5.
    :type weapon_class_levels: dict, default None
    :param perk_class_levels: User input tiers for each perk. Use str value value between 0 and 5.
    :type perk_class_levels: dict, default None
    :param max_range: User desired maximum distance for the function to compute values for. (In meters)
    :type max_range: int
    :example:
        .. code-block:: python

            from zombie.processor import Build
            weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                                   'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
            perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
            build = Build(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels)
    :note: *None*

.. autosummary::
    zombie.processor.Build.get_weapon_classes
    zombie.processor.Build.get_perk_classes
