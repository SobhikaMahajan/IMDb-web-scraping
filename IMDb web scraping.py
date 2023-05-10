#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


webpage=requests.get('https://www.imdb.com/chart/top/').text
soup=BeautifulSoup(webpage,'lxml')


# In[3]:


print(soup.prettify())


# In[4]:


scraped_movies=soup.find_all('td',class_="titleColumn")
scraped_movies


# In[5]:


#extracting the movies
movies=[]
for movie in scraped_movies:
    movie=movie.get_text().replace('\n '," ")
    movie.strip(" ")
    movies.append(movie)
movies


# In[6]:


scraped_ratings=soup.find_all('td', class_='ratingColumn imdbRating')
scraped_ratings


# In[7]:


ratings=[]
for rating in scraped_ratings:
    rating=rating.get_text().replace('\n'," ")
    rating.strip(" ")
    ratings.append(rating)
ratings


# In[8]:


data=pd.DataFrame()

data['MovieTitle']=movies
data['Ratings']=ratings

data


# In[9]:


data.to_csv('IMDb dataset.csv')


# In[ ]:




