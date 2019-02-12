//https://www.digitalocean.com/community/tutorials/how-to-install-the-pandas-package-and-work-with-data-structures-in-python-3
# coding: utf-8

# In[1]:


# Render our plots inline
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)


# In[2]:


import pandas as pd


# In[3]:


broken_df = pd.read_csv('../data/bikes.csv')


# In[4]:


import numpy as np


# In[5]:


import pandas as pd


# In[6]:


s = pd.Series([0, 1, 4, 9, 16, 25], name='Squares')


# In[7]:


s


# In[8]:


avg_ocean_depth = pd.Series([1205, 3646, 3741, 4080, 3270], index=['Arctic',  'Atlantic', 'Indian', 'Pacific', 'Southern'])


# In[9]:


avg_ocean_depth


# In[10]:


avg_ocean_depth[2]


# In[11]:


avg_ocean_depth[2:4]


# In[12]:


avg_ocean_depth['Indian']


# In[13]:


avg_ocean_depth['Indian':'Southern']


# In[14]:


avg_ocean_depth = pd.Series({
                    'Arctic': 1205,
                    'Atlantic': 3646,
                    'Indian': 3741,
                    'Pacific': 4080,
                    'Southern': 3270
})

print(avg_ocean_depth)


# In[15]:


print(avg_ocean_depth['Indian'])
print(avg_ocean_depth['Atlantic':'Indian'])


# In[16]:


avg_ocean_depth = pd.Series({
                    'Arctic': 1205,
                    'Atlantic': 3646,
                    'Indian': 3741,
                    'Pacific': 4080,
                    'Southern': 3270
})


# In[17]:


max_ocean_depth = pd.Series({
                    'Arctic': 5567,
                    'Atlantic': 8486,
                    'Indian': 7906,
                    'Pacific': 10803,
                    'Southern': 7075
})


# In[18]:


ocean_depths = pd.DataFrame({
                    'Avg. Depth (m)': avg_ocean_depth,
                    'Max. Depth (m)': max_ocean_depth
})


# In[19]:


print(ocean_depths)


# In[20]:


print(ocean_depths.sort_values('Avg. Depth (m)', ascending=True))


# In[21]:


print(ocean_depths.describe())


# In[22]:


user_data = {'first_name': ['Sammy', 'Jesse', np.nan, 'Jamie'],
        'last_name': ['Shark', 'Octopus', np.nan, 'Mantis shrimp'],
        'online': [True, np.nan, False, True],
        'followers': [987, 432, 321, np.nan]}

df = pd.DataFrame(user_data, columns = ['first_name', 'last_name', 'online', 'followers'])

print(df)


# In[23]:


user_data = {'first_name': ['Sammy', 'Jesse', np.nan, 'Jamie'],
        'last_name': ['Shark', 'Octopus', np.nan, 'Mantis shrimp'],
        'online': [True, np.nan, False, True],
        'followers': [987, 432, 321, np.nan]}


# In[24]:


print(df)


# In[25]:


df_drop_missing = df.dropna()


# In[26]:


print(df_drop_missing)


# In[27]:


df_fill = df.fillna(0)


# In[28]:


print(df_fill)

