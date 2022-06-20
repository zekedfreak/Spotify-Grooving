#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('C:/Users/Bhargav/Desktop/charts.csv')


# In[3]:


df_india_top200_2020 = df[(df['region'].str.contains("India")) & (df['chart'].str.contains("top200")) & (df['date'].str.contains("2020"))]
df_india_top200_2020


# In[4]:


songsJan = df_india_top200_2020[(df_india_top200_2020['date'].str.contains("2020-01"))]
janRange = songsJan.date.unique()
print(janRange)


# In[10]:


import matplotlib.animation as animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(15,8))

colors = ['#1B9E77','#6890F0','#CD7F32','#C0C0C0','#FFD700']

#Bar Chart Loop
def draw_barchart(current_date):
    top5 = songsJan[songsJan['date'].eq(current_date)].sort_values(by='streams', ascending=True).tail(5)
    ax.clear()
    ax.barh(top5['title'], top5['streams'],color=colors)
    
    for i,(streams, title) in enumerate(zip(top5['streams'],top5['title'])):
        ax.text(streams, i, f'  {title}  ', size=15, weight=600, ha='right', va='center') 
        ax.text(streams, i, f'  {streams:,.0f} ',size=15, weight=300, ha='left',  va='center')

    ax.tick_params(axis='x', colors='#363430', labelsize=12 , length=10, pad=10)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    
     #For Title of Chart
    ax.set_title('Top 5 Streamed Songs of January ' + current_date + ' in India' ,fontsize= 25)
    
    #For Current Date
    #ax.text(0.4, 1.05, current_date, transform=ax.transAxes, size=15, ha='left', weight=600)
    
plt.box(False)
plt.title('What was India grooving to in 2020 ?', fontsize=20)   
animator = animation.FuncAnimation(fig, draw_barchart, frames=(janRange))
HTML(animator.to_jshtml())
#animator.save("BarchartTest.gif",dpi=500)


# In[ ]:




