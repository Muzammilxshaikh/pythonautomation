#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 


# In[2]:


# reading a .csv file from url 


# In[3]:


df_premeir_league = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')


# In[4]:


df_premeir_league


# In[5]:


# rename  of column names for sample column


# In[6]:


df_premeir_league = df_premeir_league.rename(columns={'Date':'date',
                                                     'Time':'time',
                                                     'HomeTeam':'Home_team',
                                                     'AwayTeam':'Away_team',
                                                     'FTHG':'Home_goals',
                                                     'FTAG':'Away_goals'})


# In[7]:


df_premeir_league


# In[8]:


# Define directory path to store excel file
directory_path = r'D:\D drive new\D drive\Python_projects\Automation project\csv extract pj2'


# In[9]:


# ensure directory exists
os.makedirs(directory_path,exist_ok=True)


# In[10]:


# define file path to save excel file
excel_file_path = os.path.join(directory_path,'premier_league_data.xlsx')


# In[11]:


# df into excel file
df_premeir_league.to_excel(excel_file_path,index=False)


# In[12]:


print("excel file saved successfully in ",excel_file_path)

