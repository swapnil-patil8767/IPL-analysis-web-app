import streamlit as st
import pandas as pd
import preprocess, helper
import plotly.express as px
from PIL import Image




user_menu = st.sidebar.radio(
    'Select an Option',
    ('IPL Tital winner', 'Top 10 player of year', 'Top 10 Bowler of year', 'Batting records', 'Bowling records',
     'Wicketkeeping records',
     'Players', 'Teams', 'Ground','Fielding records','Partnership records'))

if user_menu == 'IPL Tital winner':
    img = Image.open(r"C:\Users\Akashay\Desktop\IPL project\ipl_logo.jpeg")
    st.image(img, width=800)
    st.header('IPL Tital winner')
    wi = preprocess.preprocess(preprocess.data1)
    st.dataframe(wi)

if user_menu == 'Top 10 player of year':
    st.header('Top 10 player of year')
    year1 = helper.year_list()
    selected_year = st.sidebar.selectbox('select year', year1)

    year_all = helper.top_batsman(selected_year)
    st.dataframe(year_all)

if user_menu == 'Top 10 Bowler of year':
    st.header('Top 10 Bowler of year')
    year1 = helper.year_list()
    selected_year = st.sidebar.selectbox('select year', year1)
    year_all1 = helper.top_bowler(selected_year)
    st.dataframe(year_all1)

if user_menu == 'Players':
    st.header('Players')
    list_batter = helper.batter()
    selected_batter = st.sidebar.selectbox('Players', list_batter)
    per_batter = helper.top_batsman_player(selected_batter)
    st.dataframe(per_batter)
    pre_batter = helper.performance(selected_batter)
    st.title("Information")
    st.dataframe(pre_batter)

    grf = helper.top_batsman_player(selected_batter)
    fig = px.line(grf, x='Season', y='total_run')
    st.title(selected_batter + " Run over year")
    st.plotly_chart(fig)

if user_menu == 'Teams':
    st.header('Teams')
    list_team = helper.all_teams()
    selected_teams = st.sidebar.selectbox('slected_teams', list_team)
    if selected_teams == 'Chennai Super Kings':
        img = Image.open(r"C:\Users\Akashay\Desktop\IPL project\csk_logo.jpeg")
        st.image(img, width=800)
    if selected_teams == 'Mumbai Indians':
        img = Image.open(r"C:\Users\Akashay\Desktop\IPL project\mi_logo.jpeg")
        st.image(img, width=800)

    t_info = helper.teams_info(selected_teams)
    st.dataframe(t_info)
    if selected_teams == 'Chennai Super Kings':
        img = Image.open(r"C:\Users\Akashay\Desktop\IPL project\csk_info(2).jpeg")
        st.image(img, width=800)
    if selected_teams == 'Mumbai Indians':
        img = Image.open(r"C:\Users\Akashay\Desktop\IPL project\mi_info.jpeg")
        st.image(img, width=800)

if user_menu == 'Ground':
    st.header('Ground')
    list_ground = helper.ground_name()
    st.dataframe(list_ground)
    st.header('Percentage of winning match on winning toss')
    ground_if = helper.ground_win_info()
    st.dataframe(ground_if)

if user_menu == 'Batting records':
    st.header('Batting records')
    list_bati_re = helper.list_batting_record()
    selected_bat_re = st.sidebar.selectbox("Batting records", list_bati_re)
    if selected_bat_re == 'High_run':
        z = helper.high_run_f()
        st.dataframe(z)
    if selected_bat_re == 'High strike rate':
        x = helper.strike_rate_f()
        st.dataframe(x)
    if selected_bat_re == 'High avg':
        c = helper.high_avg_f()
        st.dataframe(c)
    if selected_bat_re == 'Most hundreds':
        v = helper.Most_hundreds_f()
        st.dataframe(v)
    if selected_bat_re == 'most sixes':
        b = helper.most_sixes_f()
        st.dataframe(b)
    if selected_bat_re == 'most ducks':
        n = helper.most_ducks_f()
        st.dataframe(n)

if user_menu == 'Bowling records':
    st.header('Bowling records')
    list_bolli_re = helper.list_bolling_record()
    selected_bolli_rec = st.sidebar.selectbox("Bowling records", list_bolli_re)
    if selected_bolli_rec == 'Most_wickets':
        m = helper.most_wickets_f()
        st.dataframe(m)

    if selected_bolli_rec == 'Best_economy_rates':
        a = helper.best_economy_rates_f()
        st.dataframe(a)
    if selected_bolli_rec == 'Best_strike_rates':
        s = helper.best_strike_rates_f()
        st.dataframe(s)
    if selected_bolli_rec == 'Five_wickets_in_an_innings':
        d = helper.five_wickets_in_an_innings_f()
        st.dataframe(d)
    if selected_bolli_rec == 'Best_bowling_fig_in_an_innings':
        f = helper.best_bowling_fig_in_an_innings_f()
        st.dataframe(f)

if user_menu == 'Wicketkeeping records':
    st.header('Wicketkeeping records')
    list_dis_re = preprocess.list_dis_record()
    selected_dis_rec = st.sidebar.selectbox('Wicketkeeping records', list_dis_re)
    if selected_dis_rec == 'Most dismissals in a series':
        g = preprocess.Most_dismissals_in_a_series_f()
        st.dataframe(g)
    if selected_dis_rec == 'Most dismissals':
        h = preprocess.Most_dismissals_f()
        st.dataframe(h)
    if selected_dis_rec == 'Most dismissals in an innings':
        j = preprocess.Most_dismissals_in_an_innings_f()
        st.dataframe(j)

if user_menu=='Fielding records':
    st.header('Fielding records')
    list_fild_rec=preprocess.list_filding_re()
    selected_fild_rec=st.sidebar.selectbox('Fielding records',list_fild_rec)
    if selected_fild_rec=='Most catches in a match':
        k=preprocess.Most_catches_in_a_match_f()
        st.dataframe(k)
    if selected_fild_rec=='Most catches':
        l=preprocess.Most_catches_f()
        st.dataframe(l)

if user_menu=='Partnership records':
    st.header('Partnership records')
    list_par_re=preprocess.list_partnership_re()
    selected_par_re=st.sidebar.selectbox('Partnership records',list_par_re)
    if selected_par_re=='Highest partnerships by runs':
        p=preprocess.Highest_partnerships_by_runs_f()
        st.dataframe(p)
    if selected_par_re=='Highest partnerships by wicket':
        o=preprocess.Highest_partnerships_by_wicket_f()
        st.dataframe(o)

