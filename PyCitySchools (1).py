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


# In[18]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
student_data_df


# In[19]:


# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[21]:


# Get the total number of students.
student_count = school_data_complete_df["Student ID"].count()
student_count


# In[22]:


# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# In[23]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[24]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[25]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[26]:


passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# In[27]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[29]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
print (passing_math_count)
print (passing_reading_count)


# In[30]:


# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100
print (passing_math_percentage)
print (passing_reading_percentage)


# In[31]:


# Calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

passing_math_reading.head()


# In[32]:


# Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count

# Calculate the overall passing percentage.
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


# In[33]:


# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[34]:


# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]


# In[35]:


# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]


# In[36]:


# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[37]:


district_summary_df


# In[38]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# In[ ]:




