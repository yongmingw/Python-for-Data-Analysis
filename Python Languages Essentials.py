#!/usr/bin/env python
# coding: utf-8

# In[5]:


#The Basics - Language semantics - Variables and pass-by-reference#


# In[9]:


a = [1, 2, 3]


# In[10]:


a


# In[11]:


b = a


# In[12]:


a.append(4)


# In[13]:


b


# In[18]:


def f(x, y):
    x.append(y**2)


# In[19]:


data = [1, 2, 3]


# In[20]:


f(data, 4)


# In[21]:


data


# In[22]:


#The Basics - Language semantics - Dynamic references, strong types#


# In[23]:


a = 5


# In[24]:


type(a)


# In[25]:


a = "matt"


# In[26]:


type(a)


# In[27]:


a = 4.5


# In[28]:


b = 2


# In[116]:


print 'a is %s, b is %s' % (type(a), type(b))


# In[33]:


a/b


# In[34]:


a = 5


# In[35]:


isinstance(a, (int))


# In[38]:


#The Basics - Language semantics - Mutable and immutable objects#


# In[40]:


list_a = ["foo", 2, [4.5]]


# In[42]:


list_a[2] = (3, 4)


# In[43]:


list_a


# In[44]:


list_a[2] = (2, 4)


# In[45]:


list_a


# In[46]:


from datetime import datetime, date, time


# In[47]:


dt = datetime(2011, 10, 29, 20, 30, 21)


# In[48]:


dt.day


# In[49]:


dt.date()


# In[51]:


dt.strftime('%m/%d/%Y %H:%M')


# In[52]:


a = [1, 5, 6]


# In[53]:


for x in a:
    print(x)


# In[59]:


sequence = [1, 2, None, 4, None, 5]


# In[60]:


total = 0


# In[61]:


for value in sequence:
    if value is None:
        continue
    total += value


# In[62]:


total


# In[68]:


a = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in a: 
    if value == 5:
        break 
    total_until_5 += value


# In[69]:


total_until_5


# In[83]:


#The Basics - Control Flow - range and xrange#


# In[88]:


sum = 0
for i in range(10000):
    if x % 3 == 0 or x % 5 == 0:
        sum += i


# In[89]:


sum


# In[91]:


a = ['petit', 'coucou', 'riri']


# In[92]:


mapping = dict((v, i) for i, v in enumerate(a))


# In[93]:


mapping


# In[94]:


enumerate(a)


# In[109]:


a = ['apple', 'bat', 'bar', 'atom', 'book']


# In[110]:


b = {}


# In[111]:


for i in a:
    c = i[0]
    if c not in b:
        b[c] = [i]
    else:
        b[c].append(i)


# In[112]:


b


# In[114]:


states = ['   Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']


# In[ ]:





# In[ ]:




