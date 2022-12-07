import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

# Load csv
df = pd.read_csv('data\\actorfilms.csv')

# ProfileReport will build a report of your dataset and write it as a html file
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("actors_report.html")

# We can dive into the data created by investigating the keys (column names)
profset = profile.description_set
print(profset.keys())

# for example we can the correlations data we can select this from profset
attributes = profset["correlations"]
print(attributes.keys())

# and then select the auto correlations and write that data to csv
auto_correlations = attributes["auto"]
auto_correlations.to_csv('output\\Actors - Correlations.csv', index=False)
