import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Spaceship Titanic: Анализ пассажиров')

df = pd.read_csv("train.csv")
st.dataframe(df)

option = st.selectbox('Выбрать планету', (df['HomePlanet'].unique()), index=None, placeholder="Выберите планету...",)

st.text('Выбрать пассажиров, которые были в криосне:')
crio = st.checkbox('Криосон')

age = st.slider("Диапазон возрастов:", 0.0, 100.0,(18.0, 50.0))

vip = st.radio('Выбрать класс пассажиров:', ('Все пассажиры', 'Только VIP', 'Только не-VIP'))


filter_df = df.copy()
if option:
    filter_df = filter_df[filter_df['HomePlanet'] == option]

if crio:
    filter_df = filter_df[filter_df['CryoSleep'] == True]

filter_df = filter_df[(filter_df['Age']>=age[0])&(filter_df['Age']<=age[1])]

if vip == 'Только VIP':
    filter_df = filter_df[filter_df['VIP'] == True]
elif vip == 'Только не-VIP':
    filter_df = filter_df[filter_df['VIP'] == False]

if st.button("Отфильтровать"):
    st.dataframe(filter_df)
    fig, ax = plt.subplots()
    ax.hist(filter_df['Age'], bins=20, color='skyblue', edgecolor='black')
    st.pyplot(fig)


