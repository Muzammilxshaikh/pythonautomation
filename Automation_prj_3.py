#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[8]:


import requests


# In[11]:


from bs4 import BeautifulSoup


# In[12]:


url = 'http://quotes.toscrape.com/'


# In[13]:


response = requests.get(url)


# In[16]:


soup = BeautifulSoup(response.text,'lxml')


# In[19]:


qoutes = soup.find_all('span',class_='text')


# In[20]:


print(qoutes) ## getting html as well. Need to get only text.


# In[21]:


for quote in qoutes:
    print(quote.text)


# In[33]:


authors = soup.find_all('small', class_='author')
print(authors)


# In[34]:


for i in range(0, len(qoutes)):
    print(qoutes[i].text)
    print(authors[i].text)


# In[35]:


## Retrieving tag
tags = soup.find_all('div',class_='tags')


# In[39]:


for i in range(0, len(qoutes)):
    print(qoutes[i].text)
    print(authors[i].text)
    QouteTags = tags[i].find_all('a',class_='tag')
    for qoutetag in QouteTags:
        print(qoutetag.text)


# In[ ]:




