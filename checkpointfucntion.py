#!/usr/bin/env python
# coding: utf-8

# In[8]:


#question 1 :
def max_of_three(x,y,z):
    Max = x
    if y > Max:
        Max = y
    if z > Max:
        Max =z
    print ("the maximum is " ,Max)

max_of_three(12,5,11)
    


# In[15]:


#question 2 :
def calculation(a ,b) :
    Add = a + b
    Sub = a - b
    return(Add,Sub)

calculation(12,2)


# In[29]:


#question 3 :
L = [1,2,3,4,5,6] #we can use any given list 
def summ(L) :
    sum(L)
    return(sum(L))
def multiple(L) :
    mul = L[0]
    for i in range (0 , len(L)) :
        mul = mul * L[i]
    print(mul)
summ(L)
multiple(L)


# In[34]:


#question 4 :
items=[n for n in input().split('-')]#this allows us to input hyphen-separated sequence of words from the user
items.sort()
print('-'.join(items))


# In[85]:


#question 5 :
import math
def func(D ,C = 50 , H = 30) :
    Q = math.sqrt((2 *C *D)/H)
    return(int(Q))


# In[91]:


a = int(input())
b = int(input())
c = int(input())
print( func(a),func(b),func(c))


# # 

# In[ ]:




