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


# In[3]:


# Add the Pandas dependency.
import pandas as pd
# Files to load
student_data_to_load = "students_complete.csv"
# Read the CSV into a DataFrame
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[4]:


# Put the student names in a list.
student_names = student_data_df["student_name"].tolist()
student_names


# In[9]:


name = "Mrs. Linda Santiago"

print (name)
name.split()


# In[10]:


# Split the student name and determine the length of the split name.
for name in student_names:
    print(name.split(), len(name.split()))


# In[12]:


# Create a new list and use it for the for loop to iterate through the list.
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)
print (students_to_fix)


# In[13]:


# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)


# In[14]:


# Add the suffixes less than or equal to 3 to a new list.
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])

print(suffixes)


# In[15]:


# Get the unique items in the "prefixes" list.
set(prefixes)


# In[16]:


# Get the unique items in the "suffixes" list.
set(suffixes)


# In[17]:


# Strip "Mrs." from the student names
for name in students_to_fix:
    print(name.strip("Mrs."))


# In[18]:


# Replace "Dr." with an empty string.
name = "Dr. Linda Santiago"
name.replace("Dr.", "")


# In[35]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[24]:


# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"]
student_data_df


# In[25]:


# Put the cleaned students' names in another list.
student_names = student_data_df["student_name"].tolist()
student_names


# In[33]:


# Create a new list and use it for the for loop to iterate through the list.
students_fixed = []

# Use an if statement to check the length of the name.

# If the name is greater than or equal to 3, add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_fixed.append(name)

# Get the length of the students' names that are greater than or equal to 3.
len(students_fixed)
print (students_to_fix)


# In[ ]:




