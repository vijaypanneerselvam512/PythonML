#!/usr/bin/env python
# coding: utf-8

# In[22]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as pd


# In[23]:


print(sns.scatterplot(data=Ypoints))
print(plt.show())


# In[24]:


print(sns.barplot(data=Ypoints))
print(plt.show())


# In[27]:


#3-D plot
X=np.array([1,2,6,8,12,14,20])
Y=np.array([3,8,1,10,12,16,18])
Fig=plt.figure(figsize=(12,8))
Ax=plt.axes(projection="3d")
plt_3d=Ax.scatter3D(X,Y)
plt.colorbar(plt_3d)
plt.show()
#plotly package
X=np.array([10,80,100,120,150,180,250])
fig=px.scatter(X)
fig.show()


# In[ ]:




