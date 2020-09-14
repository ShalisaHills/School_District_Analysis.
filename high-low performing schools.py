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


# In[39]:


# Determine the school type.
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_types


# In[40]:


# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(per_school_types)
df


# In[41]:


# Calculate the total student count.
per_school_counts = school_data_df["size"]
per_school_counts


# In[42]:


# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# In[43]:


# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts


# In[44]:


# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget


# In[45]:


# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[47]:


# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]
student_school_math


# In[48]:


# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages


# In[50]:


# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

per_school_math
per_school_reading


# In[53]:


# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
per_school_passing_math


# In[54]:


# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
per_school_passing_math
per_school_passing_reading


# In[55]:


# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

per_school_passing_math


# In[56]:


# Calculate the students who passed both math and reading.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

per_passing_math_reading.head()


# In[57]:


# Calculate the number of students who passed both math and reading.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
# Calculate the overall passing percentage.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100
per_overall_passing_percentage


# In[58]:


# Adding a list of values with keys to create a new DataFrame.

per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()


# In[59]:


# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# Display the data frame
per_school_summary_df.head()


# In[60]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[61]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[ ]:




