#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q9 

import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)

