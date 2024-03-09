#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pandas


# In[26]:


import pandas as pd


# In[27]:


#muz_reads=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')


# In[28]:


#len(muz_reads)


# In[29]:


#muz_reads[1]


# In[30]:


## To get the files and save in locally
Tables=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')


# In[31]:


Tables[0]


# In[36]:


folder_path = 'D:\D drive new\D drive\Python_projects\Automation project\simson pj1'


# In[37]:


## iterate over each DataFrame and save it as a CSV file
for i, df in enumerate(Tables):
    #name the file based on each table
    file_name = f'simsons_episodes_table_{str(i+1)}.csv'
    # concatenate the folder path and file name to get the full file path
    full_file_path = folder_path + file_name
    #Save dataframe to csv
    df.to_csv(full_file_path, index=False)
    print(f"CSV file for the table {i+1} saved to {full_file_path}")


# In[ ]:




