# -*- coding: utf-8 -*-
"""my_streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBDg--xFeyTAj_-zfTuPA7mitrpgeIBS
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data= pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
data.head(1)

st.title('Analyse de correlation')

data.shape

viz_correlation = sns.heatmap(data.corr(), center = 0, cmap = "vlag", annot=True)
st.pyplot(viz_correlation.figure)

"""# "mpg" est négativement corrélé avec "cylinders", "cubicinches", "hp" et "weightlbs", ce qui signifie que plus ces valeurs augmentent, la consommation de carburant diminue.
# "mpg" est positivement corrélé avec "time-to-60" et "year", indiquant une légère tendance à une meilleure consommation de carburant au fil du temps.

"""



st.title('Analyse de distribution')

data.hist(figsize=(10, 8))
plt.tight_layout()

st.pyplot()

plt.boxplot(data['cylinders'])

data['cylinders'].describe()

data['weightlbs'].describe()

"""la plupart de voiture pese environ 2000LBS"""

plt.figure(figsize=(12, 5))
sns.lineplot(x=data['year'], y=data['weightlbs'])

st.pyplot()

"""le poids a tendance de diminuer au fil du temps."""

