from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze
from zombie.weapon_stats import _weapon_stats_dic

import streamlit as st

st.header('Call-Of-Duty-Cold-War-Zombies')
first_weapon = st.multiselect('First Weapon', list(_weapon_stats_dic.keys()))
second_weapon = st.multiselect('Second Weapon', list(_weapon_stats_dic.keys()))
third_weapon = st.multiselect('Third Weapon', list(_weapon_stats_dic.keys()))
rarity = st.multiselect('Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
pap = st.multiselect('Weapon Pack-a-punch level', ['0', '1', '2', '3'])
zom_level = st.slider('Round Number', 1, 100, 1)

weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}

damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                               max_range=100)
zom = Health(level=zom_level, health_cap=55, outbreak=False, multiplier=2)


