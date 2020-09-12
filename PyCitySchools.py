#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Add the dependency.
import pandas as pd
import os
import csv
# Files to load
school_data_to_load = os.path.join("schools_complete.csv")
student_data_to_load = os.path.join("students_complete.csv")
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[4]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[5]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[6]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[7]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[8]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[9]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[10]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[11]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[12]:


# Add the Pandas dependency.
import pandas as pd
# Files to load
file_to_load = "missing_grades.csv"

# Read the CSV into a DataFrame
missing_grade_df = pd.read_csv(file_to_load)
missing_grade_df


# In[13]:


# Fill in the empty rows with "85".
missing_grade_df.fillna(85)


# In[14]:


# Determine data types for the school DataFrame.
school_data_df.dtypes


# In[15]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[ ]:




