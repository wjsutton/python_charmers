import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

# Load csv
df = pd.read_csv('data\\autos_random_50k_cleaned.csv')

# ProfileReport will build a report of your dataset and write it as a html file
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("car_report.html")

# We can dive into the data created by investigating the keys (column names)
profset = profile.description_set
print(profset.keys())

# for example we can the correlations data we can select this from profset
attributes = profset["correlations"]
print(attributes.keys())

# and then select the auto correlations and print that data
auto_correlations = attributes["auto"]
print(auto_correlations)

# You can also compare two datasets
# Here we will divide the data into two, the test and control based on the column 'ab_test' 
test_df = df.loc[df['ab_test'] == 'test']
ctrl_df = df.loc[df['ab_test'] != 'test']

# create a report for both test and control data
test_report = ProfileReport(test_df, title="AB Test Group")
ctrl_report = ProfileReport(ctrl_df, title="AB Control Group")

# create a comparison report and write to html
comparison_report = ctrl_report.compare(test_report)
comparison_report.to_file("comparison.html")

