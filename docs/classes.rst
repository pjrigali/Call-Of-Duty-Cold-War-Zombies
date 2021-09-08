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
    :param health_cap: The level when zombie health values stop increasing. In season 5 this is level 55.
        Season 4 was 85. *Optional*
    :type health_cap: int
    :param outbreak: If level is True, parameter is referencing an outbreak level, default is False. *Optional*
    :type outbreak: bool
    :param multiplier: Value used to calculate armour, default is 2. *Optional*
    :type multiplier: int
    :example:
        .. code-block:: python

            from health_armour import Health
            zombie = Health(level=20, health_cap=55, outbreak=False, multiplier=2)
            zombie_health = zombie.get_health # 2450
            zombie_armour = zombie.get_armour # 1225
    :note: The multiplier is what number you would like to divide the health number by to get armour health.
        Prior to season 4 this was half the zombies health.

.. autosummary::
    zombie.health_armour.Health.get_health
    zombie.health_armour.Health.get_armour

DamageProfile
-------------
.. :currentmodule:: processor

.. class:: DamageProfile(weapon_class_levels, perk_class_levels, max_range):

    Builds a DamageProfile Class, which holds weapon and perk class levels to be applied later on.

    :param weapon_class_levels: Dict of weapon types and tier level.
    :type weapon_class_levels: dict
    :param perk_class_levels: Dict of perk type and tier level.
    :type perk_class_levels: dict
    :param max_range: Maximum range for calculations, default is 100. *Optional*
    :type max_range: int
    :example:
        .. code-block:: python

            weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                                   'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
            perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
            damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                                           max_range=100)
    :note: By default the values are set to 0.
        User inputs change these and the effects are applied across the weapons:

.. autosummary::
    zombie.processor.DamageProfile.hits
    zombie.processor.DamageProfile.get_weapon_classes
    zombie.processor.DamageProfile.get_perk_classes
    zombie.processor.DamageProfile.consecutive
    zombie.processor.DamageProfile.max_range


ModifiedWeapon
--------------
.. :currentmodule:: processor

.. class:: ModifiedWeapon:

    Builds a ModifiedWeapon Class, which holds default and modified weapon stats.

    :param weapon_name: Name of the weapon.
    :type weapon_name: str
    :param weapon_class_levels: Dict of weapon types and tier level.
    :type weapon_class_levels: dict
    :param perk_class_levels: Dict of perk type and tier level.
    :type perk_class_levels: dict
    :param nickname: User input name for the weapon. *Optional*
    :type nickname: str
    :param equipped_attachments: Dict of weapon attachment location and attachment name. *Optional*
    :type equipped_attachments: dict
    :param rarity: Rarity color. *Optional*
    :type rarity: str
    :param pap: Pack a punch level. *Optional*
    :type pap: str
    :param accuracy: Accuracy percent with the weapon. *Optional*
    :type accuracy: float
    :param critical: Critical hit percent with the weapon. *Optional*
    :type critical: float
    :example: *None*
    :note: An internal Class for organizing weapon stats.

.. autosummary::
    zombie.processor.ModifiedWeapon.pack_a_punch_level
    zombie.processor.ModifiedWeapon.rarity_level
    zombie.processor.ModifiedWeapon.default_stats
    zombie.processor.ModifiedWeapon.modified_stats
    zombie.processor.ModifiedWeapon.get_attachments

Analysis
--------
.. :currentmodule:: analysis

.. class:: Analyze(damage_profile, zombie_info, weapon_dic_lst):

    Constructs dicts, pd.DataFrames and visualizations for comparing various weapons.

    :param damage_profile: DamageProfile class object.
    :type damage_profile: DamageProfile
    :param zombie_info: Health class object.
    :type zombie_info: Health
    :param weapon_dic_lst: List of weapons and weapon info.
    :type weapon_dic_lst: dict
    :param columns_lst: Select columns to highlight, default is None. *Optional*
    :type columns_lst: List[str]
    :param x_limit: X limit on the graphs, default is 75. *Optional*
    :type x_limit: int
    :param viz_index_point: Reference point on the graphs, default is 40. *Optional*
    :type viz_index_point: int
    :param save_image: If True, will save the plots, default is False. *Optional*
    :type save_image: bool
    :example:
        .. code-block:: python

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
    :note: *None*

.. autosummary::
    zombie.analysis.Analyze.weapons_lst
    zombie.analysis.Analyze.weapons_df
    zombie.analysis.Analyze.damage_per_second_plot
    zombie.analysis.Analyze.damage_per_max_ammo_plot
    zombie.analysis.Analyze.damage_per_clip_plot
    zombie.analysis.Analyze.time_to_kill_plot
    zombie.analysis.Analyze.shots_to_kill_plot
