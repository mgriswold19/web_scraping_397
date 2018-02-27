
# coding: utf-8

# In[212]:


import matplotlib.pyplot as pyplot
from pandas import DataFrame
from datetime import datetime
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd


# In[215]:


df1 = pd.read_csv('wikileaksout2.csv')
df2 = DataFrame(df1)


# In[216]:


df1['dateindex'] = pd.to_datetime(df1['dateindex'])


# In[217]:


df1.index = df1['dateindex']
del df1['dateindex']
df1


# In[218]:


dfmon = df1['2010-1']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[219]:


dfmon = df1['2010-2']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[220]:


dfmon = df1['2010-3']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[221]:


dfmon = df1['2010-4']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[222]:


dfmon = df1['2010-5']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[223]:


dfmon = df1['2010-6']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[224]:


dfmon = df1['2012-1']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[225]:


dfmon = df1['2012-2']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[226]:


dfmon = df1['2012-3']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[227]:


dfmon = df1['2012-4']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[228]:


dfmon = df1['2012-5']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# # Spike in correspondence with Monica Handley - "Key Hillary Clinton aide repeatedly misplaced sensitive info"

# In[229]:


dfmon = df1['2012-6']
print (dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar())


# In[230]:


df2 = pd.read_csv('wikivalout.csv', header=None, index_col=0)
print (df2)


# In[231]:


df2.plot.bar()


# In[187]:


for i in range(2):
    try:
        dfmon = df1[('2010-'+str(i))]
        # print (dfmon)
        print (i)
        newdf = dfmon.groupby('otherhuman')['otherhuman'].count().plot.bar()
        print (newdf)
        # newdf.index.name = 'Month' + str(i)
    except:
        zero = True
    

