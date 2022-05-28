#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question n°1

from array import *
def array_list(array_num):
    num_list = array_num.tolist() 
    print(num_list)
  

array_num = array('i', [45,34,67]) 
array_list(array_num)


# In[6]:


# Question n°5

import numpy as np
print("Matrice originale\n")
X = np.random.rand(5, 10)
print(X)
print("\nSoustraire la moyenne de chaque ligne de la matrice.\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# In[9]:


# Question n°3

import numpy as np
x = np.array([[1, 2], [3, 5]])
print("Le tableau original : ")
print(x)
print("Les nombres superieure a 2 =", x[x>2])
print("Leurs indices sont ", np.nonzero(x > 2))


# In[10]:


# Question n°2

import numpy as np
  
n_array = np.array([[6, 8, 7],
                    [4, 2, 1],
                    [5, 9, 3]])

print("La matrice Numpy est :")

print(n_array)
  
trace = np.trace(n_array)
  
print("\nTrace d'une matrice 3X3 :")
print(trace)


# In[ ]:


# Question n°4

get_ipython().show_usage()

