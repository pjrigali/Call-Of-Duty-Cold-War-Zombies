from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze
from zombie.weapon_stats import _weapon_stats_dic
import streamlit as st

st.header('Call-Of-Duty-Cold-War-Zombies')
zom_level = st.slider('Round Number', 1, 100, 1)


first_weapon = st.selectbox('First Weapon', list(_weapon_stats_dic.keys()))
first_weapon_muzzle = st.selectbox('First Weapon Muzzle', list(_weapon_stats_dic[first_weapon].muzzle.keys()))
first_weapon_barrel = st.selectbox('First Weapon Barrel', list(_weapon_stats_dic[first_weapon].barrel.keys()))
first_weapon_body = st.selectbox('First Weapon Body', list(_weapon_stats_dic[first_weapon].body.keys()))
first_weapon_ubarrel = st.selectbox('First Weapon Underbarrel', list(_weapon_stats_dic[first_weapon].under_barrel.keys()))
first_weapon_mag = st.selectbox('First Weapon Magazine', list(_weapon_stats_dic[first_weapon].magazine.keys()))
first_weapon_handle = st.selectbox('First Weapon Handle', list(_weapon_stats_dic[first_weapon].handle.keys()))
first_weapon_stock = st.selectbox('First Weapon Stock', list(_weapon_stats_dic[first_weapon].stock.keys()))

fw_attachments = {
    'Muzzle': first_weapon_muzzle,
    'Barrel': first_weapon_barrel,
    'Body': first_weapon_body,
    'Underbarrel': first_weapon_ubarrel,
    'Magazine': first_weapon_mag,
    'Handle': first_weapon_handle,
    'Stock': first_weapon_stock
}


# second_weapon = st.selectbox('Second Weapon', list(_weapon_stats_dic.keys()))
# third_weapon = st.selectbox('Third Weapon', list(_weapon_stats_dic.keys()))
rarity = st.selectbox('Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
pap = st.selectbox('Weapon Pack-a-punch level', ['0', '1', '2', '3'])

weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}

damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                               max_range=100)
zom = Health(level=zom_level, health_cap=55, outbreak=False, multiplier=2)

gun_lst = [
    {'weapon': first_weapon, 'nickname': 'Temp '+first_weapon, 'equipped_attachments': fw_attachments, 'rarity': rarity,
     'pap': pap, 'accuracy': None, 'critical': None}
]

# Build Analyze Class
analysis = Analyze(damage_profile=damage_profile, zombie_info=zom, weapon_dic_lst=gun_lst)
st.line_chart(data=analysis._compare_info_for_plots[first_weapon]['Damage Per Second'])


