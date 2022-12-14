<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 08: Data Prep Part 2: Join & Pivots 

Today we’ll be tidying up some dirty data with python, performing pivots, joins and using the jellyfish package.

**Task: Pip Install jellyfish**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install jellyfish
```
**jellyfish** is a library for approximate & phonetic matching of strings. We'll be using Soundex today, to match words with a similar sound, you can learn more about jellyfish's matching here: [jamesturk/jellyfish](https://github.com/jamesturk/jellyfish)

In this task, we'll be working through [Preppin' Data Challenges Week 4 2022](https://preppindata.blogspot.com/2022/01/2022-week-4-prep-school-travel-plans.html) and two datasets [students]() and [travel]()

### Load packages and data
```
import pandas as pd
import numpy as np
import jellyfish

# Input both data sets
students = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/students.csv')
travel = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/travel.csv')
```
### pd.merge() - Joins

After inputting both datasets, which show details about students and their travel methods, we want to join them.

In python we'll use the pandas function `pd.merge`, which takes the form:

```
pd.merge(left_dataset,right_dataset,how=(left|right|inner|outer|cross), on = 'common_id')

# or if matching on different named columns
pd.merge(left_dataset,right_dataset,how=(left|right|inner|outer|cross), left_on='id',right_on='id_by_another_name')

# or if matching on multiple columns (add terms as lists)
pd.merge(left_dataset,right_dataset,how=(left|right|inner|outer|cross), left_on=['id_a','id_b],right_on=['id_c','id_d])
```


We'll use an inner join to filter out data for students without travel data, and reduce our dataframe to the student id with the days of the week.

```
import pandas as pd
import numpy as np
import jellyfish

# Input both data sets
students = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/students.csv')
travel = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/travel.csv')

df = pd.merge(students,travel,how='inner',left_on='id',right_on='Student ID')
df = df[['Student ID', 'M','Tu', 'W', 'Th','F']]
print(df)

```
### pd.melt() - Pivots

Next for our data we want to have a column for the weekdays ('M','Tu', 'W', 'Th','F'), with another column for the different Travel Modes, for which we'll use the `melt` function.

```
# to pivot our dataframe 'df' keeping 1 column fixed
pivot = pd.melt(df,id_vars='field_not_to_pivot, var_name='column_for_column_headers', value_name='column_for_column_contents')

# note you can remove the 'pd' at the front and replace it with the dataframe to pivot
pivot = df.melt(id_vars='field_not_to_pivot, var_name='column_for_column_headers', value_name='column_for_column_contents')

```
For more complex pivots please check the [pandas melt documentation page](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)

Ok let's pivot the student data as follows

```
pivot = df.melt(id_vars='Student ID', var_name='Weekday', value_name='Travel Mode')
print(pivot)
```
### Soundex lookup table

However, when we look at the different travel modes, there are some typos in the data.

```
methods = pivot['Travel Mode'].unique()
methods = sorted(methods)
print(methods)
```
To fix this we're going to build a lookup table of the correct spellings using a Soundex from the **jellyfish** package.

```
# Apply soundex function to travel mode
pivot['soundex'] = pivot['Travel Mode'].apply(lambda x: jellyfish.soundex(x))

# print unique soundex and travel modes
methods_w_soundex = pivot[['Travel Mode','soundex']].drop_duplicates()
methods_w_soundex = methods_w_soundex.sort_values(by = ['Travel Mode'])
print(methods_w_soundex)

# find the most frequently occuring travel mode per soundex (we hope this is the correct spelling!)
travel_map = pivot.groupby(['soundex','Travel Mode']).agg(count = ('soundex','count')).reset_index()
travel_map['count_max'] = travel_map.groupby(['soundex'])['count'].transform(max)

# filter for most frequently occuring travel mode per soundex
travel_lookup = travel_map.loc[travel_map['count'] == travel_map['count_max']]

# Manually remove Scoter as equal to max count for correct spelling
travel_lookup = travel_lookup.loc[travel_map['Travel Mode'] != 'Scoter']

print(pivot)
print(travel_lookup)
```

### Task

Up to this point in the script [08_data_prep2.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/08_data_prep2.py) , we've got a pivoted dataset: `pivot` and a lookup table of travel modes: `travel_lookup`, please could you:

- Join pivot and travel_lookup
- Reduce the number of columns to just Student Id, Weekday and Travel Mode (with correct spelling)
- Rename the columns to match: 'Student ID','Weekday','Travel Mode
- Output the data to a csv file

Check your answer against the solution here: [08_data_prep2_solution.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/solutions/08_data_prep2_solution.py)
