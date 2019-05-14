#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[8]:


names1880 = pd.read_csv('C:/Users/Hector Landes/Desktop/Thesis/names/yob1880.txt', names=['name', 'sex', 'births'])


# In[9]:


names1880


# In[11]:


names1880.groupby('sex').births.sum()


# In[18]:


years = range(1880, 2019)


# In[19]:


pieces = []


# In[20]:


columns = ['name', 'sex', 'births']


# In[21]:


for year in years:
    path = 'C:/Users/Hector Landes/Desktop/Thesis/names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)
    frame['year'] = year
    pieces.append(frame)
    names = pd.concat(pieces, ignore_index = True)


# In[23]:


names.tail


# In[69]:


total_births = names.pivot_table('births', index = 'year', columns = 'sex', aggfunc = sum)


# In[33]:


total_births.tail()


# In[35]:


total_births.plot(title = 'Total births by sex and year')


# In[37]:


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


# In[40]:


names = names.groupby(['year', 'sex']).apply(add_prop)


# In[41]:


names


# In[57]:


def get_top1000(group):
    return group.sort_values(by='births', ascending = False)[:1000]


# In[58]:


grouped = names.groupby(['year', 'sex'])


# In[59]:


top1000 = grouped.apply(get_top1000)


# In[60]:


top1000


# In[ ]:





# In[61]:


boys = top1000[top1000.sex == 'M']


# In[62]:


boys


# In[65]:


total_births = top1000.pivot_table('births', index = 'year', columns = 'name', aggfunc = sum)


# In[67]:


subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
sub.plot(subplots = True, figsize = (12, 10), grid = False, title = "Number of births per year")


# In[70]:


table = top1000.pivot_table('prop', index = 'year', columns = 'sex', aggfunc = sum)


# In[71]:


top1000


# In[72]:


df = boys[boys.year == 2010]


# In[73]:


df


# In[76]:


prop_cumsum = df.sort_values(by = 'prop', ascending = False).prop.cumsum()


# In[75]:


prop_cumsum


# In[77]:


prop_cumsum.searchsorted(0.5)


# In[78]:


def get_quantile_count(group, q = 0.5):
    group = group.sort_values(by = 'prop', ascending = False)
    return group.prop.cumsum().searchsorted(q) + 1


# In[79]:


diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)


# In[80]:


diveristy = diversity.unstack('sex')


# In[81]:


get_last_letter = lambda x: x[-1]


# In[82]:


last_letters = names.name.map(get_last_letter)


# In[84]:


last_letters.name = 'last_letter'


# In[90]:


table = names.pivot_table('births', index = last_letters, columns = ['sex', 'year'], aggfunc = sum)


# In[92]:


table


# In[94]:


subtable = table.reindex(columns=[1910, 1960, 2010], level = 'year')


# In[95]:


subtable


# In[96]:


subtable.sum()


# In[97]:


letter_prop = subtable / subtable.sum().astype(float)


# In[98]:


letter_prop


# In[99]:


import matplotlib.pyplot as plt


# In[122]:


fig, axes = plt.subplots(2, 1, figsize = (10,8))
letter_prop['M'].plot(kind = 'bar', rot = 0, ax = axes [0], title = 'Male')
letter_prop['F'].plot(kind = 'bar', rot = 0, ax = axes [1], title = 'Female', legend = False)


# In[124]:


letter_prop = table / table.sum().astype(float)


# In[126]:


dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T


# In[128]:


dny_ts


# In[130]:


dny_ts.plot()


# In[131]:


all_names = top1000.name.unique


# In[133]:


mask = np.array(['lesl' in x.lower() for x in all_names])


# In[134]:


lesley_like = all_names[mask]


# In[136]:


lesley_like


# In[137]:


filtred = top1000[top1000.name.isin(lesley_like)]


# In[138]:


filtered = groupby('name').births.sum()


# In[139]:


table = filtered.pivot_table('births', index = 'year', columns = 'sex', aggfunc = 'sum')


# In[140]:


table = table.div(table.sum(1), axis = o)


# In[141]:


table.plot(styles={'M' : 'k-', 'F' : 'k--'})


# In[ ]:




