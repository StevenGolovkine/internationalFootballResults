
# coding: utf-8

# # International football results from 1872 to 2017 
# 
# This dataset is provided by MartJ on [Kaggle](https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017).
# 
# ## Content
# 
# This dataset includes 38,361 results of international football matches starting from the very first official math in 1872 up to 2017. The matches range from World Cup to Baltic Cup to regular friendly matches. The matches are strictly men's full internationals and the data do not include Olympic Games or matches where at least one of the teams was the nation's B-team, U-23 or a league select team.
# 
# It includes the following columns:
# * date: the date the match has been played;
# * home_team: the team which played at home;
# * away_team: the team which played away;
# * home_ft: the score for the home team;
# * away_ft: the score for the away team;
# * tournament: friendly, world cup, copa america, etc;
# * city: the city where the match has been played;
# * country: the country where the match has been played.
# 
# ## Acknowledgements
# 
# The data is gathered from several sources including but not limited to wikipedia.com, fifa.com, rsssf.com and individual football associations' websites.
# 
# ## Code
# 
# The entire code of this analysis is on my Github repository.
# 
# -----

# ## Load the used libraries 

# In[1]:


get_ipython().magic('matplotlib inline')
import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# ## Import the data

# In[3]:


results = pd.read_csv("results.csv", sep=',', header=0)


# In[5]:


# Let's look at the data
results.head()


# In[12]:


# Do the data have missing/null values?
print("There is", results.isna().sum().sum(), "missing value.")
print("There is", results.isnull().sum().sum(), "null value.")


# In[44]:


print("Since ", results.date[0], ", there were ", len(results), " international football matches (until ", results.date[len(results) - 1], ").", sep='')


# ## Exploration of the data

# In[ ]:





# In[42]:


help(print)

