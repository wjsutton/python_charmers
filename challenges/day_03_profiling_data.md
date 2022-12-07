<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 03: Profiling Data

Today we’ll be getting python to help us understand new datasets using the package [pandas-profiling](https://pandas-profiling.ydata.ai/docs/master/index.html).

**Task: Pip Install pandas-profiling**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install -U pandas-profiling
```

We've been given a new dataset [autos_random_50k_cleaned.csv](https://github.com/wjsutton/python_charmers/blob/main/data/autos_random_50k_cleaned.csv) and asked to produce some analysis on it. We can use pandas-profiling to give us a headstart.

**Task: Add [autos_random_50k_cleaned.csv](https://github.com/wjsutton/python_charmers/blob/main/data/autos_random_50k_cleaned.csv) to your data folder so python can read it and follow the script [03_profiling_data.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/03_profiling_data.py)**

```
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

# Load csv
df = pd.read_csv('data\\autos_random_50k_cleaned.csv')

# ProfileReport will build a report of your dataset and write it as a html file
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("car_report.html")
```
Note the variable `df` is commonly used for data, is shortform for `dataframe`.

At this point a html report will be created locally detailing the data.

- Data types
- Data quality alerts
- Distributions of variables
- Scatter diagrams
- Correlations 

![Screenshot of pandas-profiling output](https://github.com/wjsutton/python_charmers/blob/main/challenges/images/03_pandas_profiling.png)

We can also extract data from this by filtering through the sections... 

```
# We can dive into the data created by investigating the keys (column names)
profset = profile.description_set
print(profset.keys())

# for example we can the correlations data we can select this from profset
attributes = profset["correlations"]
print(attributes.keys())

# and then select the auto correlations and print that data
auto_correlations = attributes["auto"]
print(auto_correlations)
```

And we can also create a report that compares datasets, check the comparison html file that is generated.

```
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
```

### Task

Having seen `pandas-profiling` in action it's over to you, please could you:

- Run the script [03_profiling_data.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/03_profiling_data.py) locally generating the report files
- Download the [Actors dataset](https://github.com/wjsutton/python_charmers/blob/main/data/actorfilms.csv) and create a data profile report for it (you will not need to create a comparison report)
- Please write the `auto correlation` table to a csv file, check [Day 02's script](https://github.com/wjsutton/python_charmers/blob/main/challenges/day_02_pip_install.md) for help with this

[A solution script is available here](https://github.com/wjsutton/python_charmers/blob/main/scripts/solutions/03_profiling_data_solution.py)
