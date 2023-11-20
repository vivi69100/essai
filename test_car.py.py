#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data= pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
data.head(1)


# In[11]:


data.shape


# In[5]:


sns.heatmap(data.corr(), center = 0, cmap = "vlag", annot=True)


# # "mpg" est négativement corrélé avec "cylinders", "cubicinches", "hp" et "weightlbs", ce qui signifie que plus ces valeurs augmentent, la consommation de carburant diminue.
# # "mpg" est positivement corrélé avec "time-to-60" et "year", indiquant une légère tendance à une meilleure consommation de carburant au fil du temps.
# 

# In[ ]:





# In[9]:


data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()


# In[12]:


plt.boxplot(data['cylinders'])


# In[14]:


data['cylinders'].describe()


# In[16]:


data['weightlbs'].describe()


# la plupart de voiture pese environ 2000LBS

# In[19]:


plt.figure(figsize= (12,5))
sns.lineplot(x=data['year'],y=data['weightlbs'])


# le poids a tendance de diminuer au fil du temps.

# In[ ]:




