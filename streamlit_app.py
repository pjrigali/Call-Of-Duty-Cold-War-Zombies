import pandas as pd
from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze
from zombie.weapon_stats import _weapon_stats_dic
import streamlit as st

st.title('Call-Of-Duty-Cold-War-Zombies')
st.markdown('*This is a demo of the Cold-War-Zombies package.*')
st.subheader('Select Zombie Level')
zom_level = st.slider('Round Value', 1, 100, 1)


# first_weapon = st.selectbox('First Weapon', ['None'] + list(_weapon_stats_dic.keys()))
# if first_weapon != 'None':
#     first_weapon_muzzle = st.selectbox('First Weapon Muzzle', ['None'] + list(_weapon_stats_dic[first_weapon].muzzle.keys()))
#     first_weapon_barrel = st.selectbox('First Weapon Barrel', ['None'] + list(_weapon_stats_dic[first_weapon].barrel.keys()))
#     first_weapon_body = st.selectbox('First Weapon Body', ['None'] + list(_weapon_stats_dic[first_weapon].body.keys()))
#     first_weapon_ubarrel = st.selectbox('First Weapon Underbarrel', ['None'] + list(_weapon_stats_dic[first_weapon].under_barrel.keys()))
#     first_weapon_mag = st.selectbox('First Weapon Magazine', ['None'] + list(_weapon_stats_dic[first_weapon].magazine.keys()))
#     first_weapon_handle = st.selectbox('First Weapon Handle', ['None'] + list(_weapon_stats_dic[first_weapon].handle.keys()))
#     first_weapon_stock = st.selectbox('First Weapon Stock', ['None'] + list(_weapon_stats_dic[first_weapon].stock.keys()))
#     first_rarity = st.selectbox('Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
#     first_pap = st.selectbox('Weapon Pack-a-punch level', ['0', '1', '2', '3'])
#
#     fw_attachments = {
#         'Muzzle': first_weapon_muzzle,
#         'Barrel': first_weapon_barrel,
#         'Body': first_weapon_body,
#         'Underbarrel': first_weapon_ubarrel,
#         'Magazine': first_weapon_mag,
#         'Handle': first_weapon_handle,
#         'Stock': first_weapon_stock
#     }
#
# second_weapon = st.selectbox('Second Weapon', ['None'] + list(_weapon_stats_dic.keys()))
# if second_weapon != 'None':
#     second_weapon_muzzle = st.selectbox('Second Weapon Muzzle', ['None'] + list(_weapon_stats_dic[second_weapon].muzzle.keys()))
#     second_weapon_barrel = st.selectbox('Second Weapon Barrel', ['None'] + list(_weapon_stats_dic[second_weapon].barrel.keys()))
#     second_weapon_body = st.selectbox('Second Weapon Body', ['None'] + list(_weapon_stats_dic[second_weapon].body.keys()))
#     second_weapon_ubarrel = st.selectbox('Second Weapon Underbarrel', ['None'] + list(_weapon_stats_dic[second_weapon].under_barrel.keys()))
#     second_weapon_mag = st.selectbox('Second Weapon Magazine', ['None'] + list(_weapon_stats_dic[second_weapon].magazine.keys()))
#     second_weapon_handle = st.selectbox('Second Weapon Handle', ['None'] + list(_weapon_stats_dic[second_weapon].handle.keys()))
#     second_weapon_stock = st.selectbox('Second Weapon Stock', ['None'] + list(_weapon_stats_dic[second_weapon].stock.keys()))
#     second_rarity = st.selectbox('Second Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
#     second_pap = st.selectbox('Second Weapon Pack-a-punch level', ['0', '1', '2', '3'])
#     sw_attachments = {
#         'Muzzle': second_weapon_muzzle,
#         'Barrel': second_weapon_barrel,
#         'Body': second_weapon_body,
#         'Underbarrel': second_weapon_ubarrel,
#         'Magazine': second_weapon_mag,
#         'Handle': second_weapon_handle,
#         'Stock': second_weapon_stock
#     }

count = 1
gun_lst = []
st.subheader('Select Weapons for Analysis')
weapon_lst = st.multiselect('Weapons', list(_weapon_stats_dic.keys()))
for weapon in weapon_lst:
    cv = str(count) + ' '
    st.subheader(weapon + ' Attachments')
    weapon_muzzle = st.selectbox(weapon + ' Weapon Muzzle', ['None'] + list(_weapon_stats_dic[weapon].muzzle.keys()))
    weapon_barrel = st.selectbox(weapon + ' Weapon Barrel', ['None'] + list(_weapon_stats_dic[weapon].barrel.keys()))
    weapon_body = st.selectbox(weapon + ' Weapon Body', ['None'] + list(_weapon_stats_dic[weapon].body.keys()))
    weapon_ubarrel = st.selectbox(weapon + ' Weapon Underbarrel', ['None'] + list(_weapon_stats_dic[weapon].under_barrel.keys()))
    weapon_mag = st.selectbox(weapon + ' Weapon Magazine', ['None'] + list(_weapon_stats_dic[weapon].magazine.keys()))
    weapon_handle = st.selectbox(weapon + ' Weapon Handle', ['None'] + list(_weapon_stats_dic[weapon].handle.keys()))
    weapon_stock = st.selectbox(weapon + ' Weapon Stock', ['None'] + list(_weapon_stats_dic[weapon].stock.keys()))
    rarity = st.selectbox(weapon + ' Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
    pap = st.selectbox(weapon + ' Weapon Pack-a-punch level', ['0', '1', '2', '3'])

    attachments = {
        'Muzzle': weapon_muzzle,
        'Barrel': weapon_barrel,
        'Body': weapon_body,
        'Underbarrel': weapon_ubarrel,
        'Magazine': weapon_mag,
        'Handle': weapon_handle,
        'Stock': weapon_stock
    }
    val = {'weapon': weapon, 'nickname': 'Temp ' + weapon, 'equipped_attachments': attachments,
           'rarity': rarity, 'pap': pap, 'accuracy': None, 'critical': None}
    gun_lst.append(val)
    count += 1

# third_weapon = st.selectbox('Third Weapon', list(_weapon_stats_dic.keys()))
# rarity = st.selectbox('Weapon Rarity', ['common', 'green', 'blue', 'purple', 'orange'])
# pap = st.selectbox('Weapon Pack-a-punch level', ['0', '1', '2', '3'])

weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                               max_range=100)
zom = Health(level=zom_level, health_cap=55, outbreak=False, multiplier=2)

# gun_lst = []
# for ind, weapon in enumerate([first_weapon, second_weapon]):
    # if weapon != 'None':
    #     if ind == 0:
    #         val = {'weapon': first_weapon, 'nickname': 'Temp ' + first_weapon, 'equipped_attachments': fw_attachments,
    #                'rarity': first_rarity, 'pap': first_pap, 'accuracy': None, 'critical': None}
    #     elif ind == 1:
    #         val = {'weapon': second_weapon, 'nickname': 'Temp ' + second_weapon, 'equipped_attachments': sw_attachments,
    #                'rarity': second_rarity, 'pap': second_pap, 'accuracy': None, 'critical': None}
    #     else:
    #         continue
    #     gun_lst.append(val)

# gun_lst = [
#     {'weapon': first_weapon, 'nickname': 'Temp ' + first_weapon, 'equipped_attachments': fw_attachments,
#      'rarity': first_rarity, 'pap': first_pap, 'accuracy': None, 'critical': None},
#     {'weapon': second_weapon, 'nickname': 'Temp ' + second_weapon, 'equipped_attachments': sw_attachments,
#      'rarity': second_rarity, 'pap': second_pap, 'accuracy': None, 'critical': None},
# ]

# Build Analyze Class
analysis = Analyze(damage_profile=damage_profile, zombie_info=zom, weapon_dic_lst=gun_lst)

# chart_df = pd.DataFrame()
# for weapon in [first_weapon, second_weapon]:
#     if weapon != 'None':
#         chart_df[weapon] = analysis._compare_info_for_plots[weapon]['Damage Per Second']
# st.line_chart(data=chart_df)

st.subheader('Damage Per Second')
dps_df = pd.DataFrame()
for weapon in weapon_lst:
    if weapon != 'None':
        dps_df[weapon] = analysis._compare_info_for_plots[weapon]['Damage Per Second']
st.line_chart(data=dps_df)
st.caption('Damage Value vs Range (Meters)')

st.subheader('Time to Kill (Seconds)')
ttk_df = pd.DataFrame()
for weapon in weapon_lst:
    if weapon != 'None':
        ttk_df[weapon] = analysis._compare_info_for_plots[weapon]['Time To Kill']
st.line_chart(data=ttk_df)
st.caption('Seconds vs Range (Meters)')
