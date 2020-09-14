#!/usr/bin/env python
# coding: utf-8

# In[ ]:


size = int(input("enter the number of values you want to enter "))


# In[ ]:


list = []


# In[ ]:


for x in range(size):
    list.append(int(input()))
    


# In[ ]:


list1=[]


# In[ ]:


for i in range(size):
    if list[i]>=0:
        list1.append(list[i])
    


# In[ ]:


print(list1)

