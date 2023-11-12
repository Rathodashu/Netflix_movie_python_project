#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[36]:


data = pd.read_csv(r"C:\Users\Hp\Downloads\file.csv")


# In[37]:


data


# In[39]:


# head() funcation use for top 10 records of the data sets 

data.head(10)


# In[40]:


# tail() function show the top bottem records of the datasets 

data.tail()


# In[41]:


# shepe function show the number of the rows and columns 

data.shape


# In[42]:


# size function show No of total values elements in datasets

data.size


# In[44]:


# columns function show the each columns name

data.columns


# In[45]:


# dtypes funcations show the data type of each column

data.dtypes


# In[46]:


# info() funcation show the indexes, columns, data-types, of each columns memory at once

data.info()


# ### duplicate() funcation 
# 

# In[47]:


data.head()


# In[48]:


data.shape


# In[49]:


# duplicate function check row wise and detect the duplicate rows 

data.duplicated()


# In[50]:


data[data.duplicated()]


# In[52]:


# remove function use for remove the duplicate rows permanently 

data.drop_duplicates()


# In[53]:


# remove the rows permenatly 
data.drop_duplicates(inplace = True)


# In[54]:


data[data.duplicated()]


# In[55]:


data.shape


# In[56]:


# to shwo where  null values is persent

data.isnull()


# In[57]:


# To show the count of null values in each column

data.isnull().sum()


# In[59]:


# Using heatmap to show null values count

sns.heatmap(data.isnull())


# In[60]:


## For House of cards what is the show id and who is the director of this show


# In[61]:


#isig()
data.head()


# In[63]:


# To show all records of a particular item in any column
data[data['Title'].isin(['House of Cards'])]


# In[64]:


# In which year highest number of the TV shows & movies were related 


# In[65]:


# dtypes
data.dtypes


# In[66]:


# to_datetime

data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[68]:


data.head()


# In[69]:


data.dtypes


# In[71]:


## dt.year.value_counts()

data["Date_N"].dt.year.value_counts()


# In[72]:


# Bar Graph

data['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[73]:


## How many Movies and TV shows are in the dataset? show with bar graph


# In[74]:


# groupby()

data.head(5)


# In[75]:


data.groupby('Category').Category.count()


# In[76]:


## countplot()
sns.countplot(data['Category'])


# In[77]:


## Show all the Movies that were released in year 2000.


# In[78]:


# Creating new column

data.head(2)


# In[79]:


# data['Year'] = data['Date_N'].dt.year

data['Year'] = data['Date_N'].dt.year


# In[80]:


# data.head()

data.head(2)


# In[83]:


# Filtering

data[ (data['Category'] == 'Movie') & (data['Year']==2000) ]


# In[85]:


data[ (data['Category'] == 'Movie') & (data['Year']==2020) ]


# In[86]:


## Show only the Titles of all TV shows that were released in India only


# In[88]:


# filtering 
# data.head(2)

data.head(2)


# In[100]:


## Show top 10 Directors who gave the highest number of TV show & Movies to Netflix


# In[101]:


# Value_counts()

# data['Director'].value_counts().head(10)

data.head(2)


# In[103]:


data['Director'].value_counts(10)


# In[104]:


## Show all the records where category is movie and type is comedies or country is united kingdom


# In[105]:


# Filtering (And , Or Operators)

data.head(2)


# In[109]:


data [ (data['Category']=='Movie') & (data['Type']=='Comedies') ]


# In[114]:


data [ (data['Category']=='Movie') & (data['Type']=='Comedies')  | (data['Country']=='United Kingdom')]


# In[115]:


## In how many movies/shows, tom cruise was cast?


# In[116]:


# data.head()

data.head(2)


# In[118]:


# Filtering 

# data[data['Cast']=='Tom Cruise']

data[data['Cast']=='Tom Cruise']


# In[121]:


# Creating new data_frame

data_new = data.dropna()


# In[122]:


# data_new.head(2)

data_new.head(2)


# In[123]:


# data_new[data_new['Cast'].str.contains('Tom Cruise')]

data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[124]:


## What are the different ratings defined by netflix?


# In[126]:


# Nunique()

data.head(2)


# In[127]:


data['Rating'].nunique()


# In[128]:


# unique()

# data.Rating.unique()

data['Rating'].unique()


# In[129]:


## How many movies got the TV-14 rating in Canda?


# In[131]:


# data.Head(2)

data.head(2)


# In[132]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14')]


# In[134]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')]


# In[135]:


## How many TV shows got the R rating affter year 2018?


# In[136]:


data.head(2)


# In[139]:


data[(data['Category']=='TV Show') & (data['Rating']=='R')]


# In[140]:


data[(data['Category']=='TV Show') & (data['Rating']=='R') & (data['Year']> 2018)]


# In[141]:


## What is the maximum duration of a movie/Show on Netflix?


# In[143]:


# data['Duration'].unique()

data.Duration.unique()


# In[144]:


# data.Duration.dtypes
data.Duration.dtypes


# In[145]:


# str.split()

data.head(2)


# In[148]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ', expand = True)


# In[150]:


# data.head(2)

data.head(2)


# In[151]:


# Max()

# data.minutes.Max()

data['Minutes'].max()


# In[153]:


data['Minutes'].min()


# In[154]:


data['Minutes'].mean()


# In[155]:


data.dtypes


# In[156]:


## Which individual country has the highest NO. of TV shows


# In[157]:


# data.head(2)

data.head(2)


# In[158]:


# data_tvshow = data[data['Category']== 'TV Show']

data_tvshow = data[data['Category']== 'TV Show']


# In[160]:


data_tvshow.head(2)


# In[161]:


data_tvshow.Country.value_counts()


# In[164]:


data_tvshow.Country.value_counts().head(1)


# In[165]:


## How can we sort the dataset by Year? 


# In[166]:



data.head(2)


# In[167]:


data.sort_values(by = 'Year')


# In[168]:


data.sort_values(by = 'Year', ascending = False)


# In[169]:


## Find all the instances where: 

## Category is Movie and Type is Dramas

## Category is TV Show & Type is Kids TV


# In[170]:


data.head(2)


# In[171]:


data [ (data['Category']=="Movie") & (data['Type']=='Dramas')].head(2)


# In[175]:


data [ (data['Category']=='TV Show') & (data['Type']=="Kids' TV")]


# In[179]:


data [ (data['Category']=="Movie") & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids' TV") ]


# In[ ]:




