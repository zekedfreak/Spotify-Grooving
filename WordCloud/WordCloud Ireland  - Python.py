#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv('C:/Users/Bhargav/Desktop/charts.csv')


# In[6]:


df_ire_top200_2020 = df[(df['region'].str.contains("Ireland")) & (df['chart'].str.contains("top200")) & (df['date'].str.contains("2020"))]


# In[7]:


text = " ".join(review for review in df_ire_top200_2020.title.astype(str))


# In[15]:


mask = np.array(Image.open("IrelandFinal.jpg"))


# In[16]:


stopwords = set(STOPWORDS)
stopwords.update(["Title", "Track", "feat", "Dancing"])

wcIreland = WordCloud(background_color="#D3D3D3", max_words=300, mask=mask,
                    contour_width=1, contour_color='black',stopwords=stopwords).generate(text)

plt.figure(figsize=[15,8])
plt.title('What was Ireland grooving to in 2020 ?')
plt.imshow(wcIreland, interpolation='bilinear')
plt.axis("off")
plt.savefig("IrelandGrooving.png",dpi=500)
plt.show()


# In[ ]:




