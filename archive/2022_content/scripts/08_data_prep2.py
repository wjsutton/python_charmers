import pandas as pd
import numpy as np
import jellyfish

# Input both data sets
students = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/students.csv')
travel = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/travel.csv')

df = pd.merge(students,travel,how='inner',left_on='id',right_on='Student ID')
df = df[['Student ID', 'M','Tu', 'W', 'Th','F']]
print(df)

pivot = df.melt(id_vars='Student ID', var_name='Weekday', value_name='Travel Mode')
print(pivot)

methods = pivot['Travel Mode'].unique()
methods = sorted(methods)
print(methods)

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
