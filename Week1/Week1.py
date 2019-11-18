#!/usr/bin/env python
# coding: utf-8

# In this exercise you'll try to build a neural network that predicts the price of a house according to a simple formula.
# 
# So, imagine if house pricing was as easy as a house costs 50k + 50k per bedroom, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k etc.
# 
# How would you create a neural network that learns this relationship so that it would predict a 7 bedroom house as costing close to 400k etc.
# 
# Hint: Your network might work better if you scale the house price down. You don't have to give the answer 400...it might be better to create something that predicts the number 4, and then your answer is in the 'hundreds of thousands' etc.

# In[1]:


import tensorflow as tf
import numpy as np
from tensorflow import keras


# In[4]:


# GRADED FUNCTION: house_model
def house_model(y_new):
    xs = np.array([1,2,3,4,5,6,7,8,9,10])# Your Code Here#
    ys = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5])# Your Code Here#
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])# Your Code Here#
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs,ys,epochs=1000)
    return model.predict(y_new)[0]


# In[5]:

prediction = house_model([7.0])
print(prediction)


# In[ ]:




