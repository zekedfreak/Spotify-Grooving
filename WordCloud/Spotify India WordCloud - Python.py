#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv('C:/Users/Bhargav/Desktop/charts.csv')


# In[9]:


df_india_top200_2020 = df[(df['region'].str.contains("India")) & (df['chart'].str.contains("top200")) & (df['date'].str.contains("2020"))]


# In[10]:


text = " ".join(review for review in df_india_top200_2020.title.astype(str))


# In[11]:


wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[12]:


mask = np.array(Image.open("IndiaFinal.jpg"))


# In[13]:


stopwords = set(STOPWORDS)
stopwords.update(["Title", "Track"])

wcIndia = WordCloud(background_color="#D3D3D3", max_words=300, mask=mask,
                    contour_width=1, contour_color='black',stopwords=stopwords).generate(text)

#Create PNG
wcIndia.to_file("indiamap.png")

#Show Chart
plt.figure(figsize=[15,8])
plt.title('What was India grooving to in 2020 ?')
plt.imshow(wcIndia, interpolation='bilinear')
plt.axis("off")
plt.savefig("IndiaGrooving.png",dpi=500)
plt.show()


# In[ ]:




