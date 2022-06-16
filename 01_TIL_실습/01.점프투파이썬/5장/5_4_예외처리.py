#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


# In[2]:


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    e1 = e
    print(e1)
except IndexError as e:
    e2 = e
    print(e2)


# In[3]:


try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)


# In[7]:


try:
    4/0    
except ZeroDivisionError as e:
    print(e)
    
try:
    a = [1,2]
    print(a[3])  
except IndexError as e:
    print(e)


# In[9]:


## 오류 일부로 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError   ## 파이썬 내장오류로 구현되지 않았을 경우 일부처 오류를 일으키기 위해 사용됨


# In[11]:


class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()   #메서스 오버라이딩    


# In[13]:


class Eagle(Bird):
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly()   #메서스 오버라이딩 


# In[14]:


### 예외 만들기:


# In[15]:


class MyError(Exception):
    pass


# In[16]:


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# In[17]:


say_nick('천사')


# In[18]:


say_nick('바보')


# In[24]:


try:
    a1 = '천사'
    a2 = '바보'
    say_nick(a1)
    say_nick(a2)
except MyError:
    print('허용되지 않는 별명입니다')


# In[26]:


try:
    a1 = '천사'
    a2 = '바보'
    say_nick(a1)
    say_nick(a2)
except MyError as e:
    print(e)


# In[29]:


class MyError(Exception):
    def __str__(self):
        return '"바보"는 허용되지 않는 별명입니다'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    
try:
    a1 = '천사'
    a2 = '바보'
    say_nick(a1)
    say_nick(a2)
    
except MyError as e:
    print(e)


# In[ ]:




