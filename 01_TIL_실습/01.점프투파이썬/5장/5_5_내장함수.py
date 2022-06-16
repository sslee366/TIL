#!/usr/bin/env python
# coding: utf-8

# In[2]:


abs(3)


# In[5]:


abs(-3)


# In[6]:


abs(-1.2)


# In[8]:


all([1,2,3])


# In[9]:


all([1,2,3,0])


# In[10]:


all([])


# In[13]:


any([0,""])


# In[14]:


any([])


# In[15]:


chr(97)


# In[16]:


chr(44032)


# In[17]:


dir([1,2,3])


# In[18]:


dir({'1':'a'})


# In[19]:


dir([])


# In[22]:


divmod(7,3)


# In[23]:


for i, num in enumerate(['body','foo','bar']):   #인덱스값포함하여 출력
    print(i,num)


# In[24]:


for i, num in enumerate(['body','foo','bar'], start = 1):   #start 값 정할 수 있음
    print(i,num)


# In[26]:


eval('1+3')


# In[27]:


eval('1+3, "hi"+"a", divmod(4,3)')  # 여러 결과값을 할 경우


# In[32]:


type(eval('1+3, "hi"+"a", divmod(4,3)'))  # 결과는 튜플로 나옴


# In[28]:


eval([1+3, "hi"+"a", divmod(4,3)]) # 1개의 인수(str)만 되며 튜플 1개의 결과로 나옴. 즉 list는 안됨


# In[30]:


eval(str([1+3, "hi"+"a", divmod(4,3)])) # 리스트는 str으로 묶어주면 결과는 list로 나옴


# In[31]:


type(eval(str([1+3, "hi"+"a", divmod(4,3)])))


# In[46]:


#positive.py

def positive(a):
    result = []
    for i in a:
        if i > 0:
            result.append(i)
    return result
    
print(positive([1,-3,2,0,-5,6]))


# In[47]:


print(positive([1,2,3,4, -4,5,6]))


# In[52]:


#filter1.py
def positive2(x):
    return x>0

list(filter(positive2, [1,-3,2,0,-5,6]))


# In[50]:


list(filter(lambda x:x>0, [1,-3,2,0,-5,6]))


# In[53]:


hex(234)


# In[54]:


hex(3)


# In[55]:


a =3
id(3)


# In[56]:


id(a)


# In[57]:


b=a
id(b)


# In[58]:


a= input()


# In[59]:


b = input('Enter: ')


# In[60]:


b


# In[65]:


int('33', 16)


# In[66]:


int(2.8)


# In[67]:


int('A', 16)


# In[69]:


int('11',2)


# In[70]:


class Person: pass
a=Person()
isinstance(a,Person)


# In[71]:


print(a)


# In[72]:


type(a)


# In[73]:


b=3
isinstance(b,Person)


# In[74]:


len('Life is wonderful')


# In[75]:


len([1,2,3])


# In[76]:


list('wonderful')


# In[77]:


str(list('wonderful'))


# In[89]:


a=""
a="".join(list('wonderful'))
a


# In[85]:


a=""
aa = ['w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l']
a = "".join(aa)
print(a)


# In[86]:


type(a)


# In[87]:


list(a)


# In[92]:


# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result


# In[93]:


two_times([1,2,3,4])


# In[95]:


def two2_times(x):
    return x*2

list(map(two2_times, [1,2,3,4]))


# In[96]:


a=[1,2,3,4]
a*2


# In[104]:


a3=""
a3 = "".join(list(map(two2_times, "1,2,3,4")))


# In[105]:


a3


# In[106]:


a3 = a3.replace(",,"," ")


# In[107]:


a3


# In[108]:


a4 = a3.split()


# In[109]:


a4


# In[110]:


str(a4)


# In[112]:


a5="".join(a4)


# In[113]:


a5


# In[115]:


list(map(two2_times,a5))


# In[119]:


a5List = list(a5)
print(a5List)
print(list(map(two2_times,a5List)))


# In[120]:


map(str,a5)


# In[122]:


"".join(map(str,a5List))


# In[123]:


a4


# In[149]:


s = ['3', '30', '34', '5', '9'] 
n = list(map(int,s))
n2 = list(map(lambda n: n*2,n))
s2 = list(map(str,n2))
print(n)
print(n2)
print(s2)


# In[150]:


max(1,2,3)


# In[151]:


max('python')


# In[152]:


min([1,2,3])


# In[153]:


oct(34)


# In[154]:


ord('a')


# In[155]:


chr(97)


# In[156]:


pow(2,4)


# In[157]:


pow(3,4)


# In[158]:


n


# In[159]:


n2


# In[161]:


list(zip(n,n2))


# In[162]:


list(zip(n,s))


# In[163]:


list(zip("abc",'def'))


# In[ ]:




