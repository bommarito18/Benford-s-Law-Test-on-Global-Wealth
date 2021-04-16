#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import pandas_datareader as web
from benfordslaw import benfordslaw


# In[14]:


bl = benfordslaw(alpha=0.05)


# In[15]:


df = pd.read_excel('../Data/WealthWorld.xlsx')
df


# In[16]:


X = df['Wealth in US Billions']
X


# In[17]:


results = bl.fit(X)


# In[20]:


bl.plot(title='Total Wealth per Country 2019')


# In[ ]:




