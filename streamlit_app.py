import pandas as pd
from zombie.health_armour import Health
from zombie.processor import DamageProfile
from zombie.analysis import Analyze
from zombie.weapon_stats import _weapon_stats_dic
import streamlit as st

st.title('Call-Of-Duty-Cold-War-Zombies')
st.markdown('*This is a demo of the Cold-War-Zombies package.*')
st.subheader('Select Zombie Level:')
zom_level = st.slider('Round Value', 1, 100, 1)

st.sidebar.title("How to Use:")
st.sidebar.markdown("1. Select the desired zombie round")
st.sidebar.markdown("2. Select desired weapons for comparison")
st.sidebar.markdown("3. Select the desired weapon attachments")
st.sidebar.markdown("4. View comparison tables below")
st.sidebar.title("Weapons")
st.sidebar.markdown("*All weapons are included up until mid-season 6.*")


gun_lst = []
st.subheader('Select Weapons for Analysis')
weapon_lst = st.multiselect('Weapons', list(_weapon_stats_dic.keys()))
for weapon in weapon_lst:
    st.subheader(weapon + ' Attachments:')
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

weapon_class_levels = {'Launcher': '5', 'Special': '5', 'Smg': '5', 'Shotgun': '5', 'Pistol': '5',
                       'Marksman': '5', 'Sniper': '5', 'Lmg': '5', 'Assault': '5', 'Melee': '5'}
perk_class_levels = {'speed': '5', 'stamin up': '5', 'deadshot': '5', 'death_perception': '5'}
damage_profile = DamageProfile(weapon_class_levels=weapon_class_levels, perk_class_levels=perk_class_levels,
                               max_range=100)
zom = Health(level=zom_level, health_cap=55, outbreak=False, multiplier=2)

# Build Analyze Class
if len(gun_lst) >= 1:
    analysis = Analyze(damage_profile=damage_profile, zombie_info=zom, weapon_dic_lst=gun_lst)

    st.header('Visualizations:')
    plots = st.multiselect('Plots to Display', ['Damage Per Max Ammo', 'Damage Per Clip', 'Damage Per Second',
                                                'Time To Kill', 'Shots To Kill'])
    for plot in plots:
            st.subheader(plot)
            dps_df = pd.DataFrame()
            for weapon in weapon_lst:
                if weapon != 'None':
                    dps_df[weapon] = analysis._compare_info_for_plots[weapon][plot]
            st.line_chart(data=dps_df)
            if 'Damage' in plot:
                st.caption('Damage Value vs Range (Meters)')
            elif 'Time' in plot:
                st.caption('Seconds vs Range (Meters)')
            elif 'Shots' in plot:
                st.caption('Shots vs Range (Meters)')
            elif 'Ratio' in plot:
                st.caption('Ratio vs Range (Meters)')

    # if 'Time To Kill' in plots:
    #     st.subheader('Time to Kill (Seconds)')
    #     ttk_df = pd.DataFrame()
    #     for weapon in weapon_lst:
    #         if weapon != 'None':
    #             ttk_df[weapon] = analysis._compare_info_for_plots[weapon]['Time To Kill']
    #     st.line_chart(data=ttk_df)
    #     st.caption('Seconds vs Range (Meters)')
    #
    # if
    # st.subheader('Time to Kill (Seconds)')
    # ttk_df = pd.DataFrame()
    # for weapon in weapon_lst:
    #     if weapon != 'None':
    #         ttk_df[weapon] = analysis._compare_info_for_plots[weapon]['Time To Kill']
    # st.line_chart(data=ttk_df)
    # st.caption('Seconds vs Range (Meters)')