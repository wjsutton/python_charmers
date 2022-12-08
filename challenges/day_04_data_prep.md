<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 04: Data Prep

Today we’ll be modifying data with python and the pandas & datetime library

**Task: Pip Install datetime**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install datetime
```

We've been given a new dataset [PD2021_Wk2_Input_Bike_Model_Sales.csv](https://github.com/wjsutton/python_charmers/blob/main/data/PD2021_Wk2_Input_Bike_Model_Sales.csv) from the [Preppin' Data Challenges](https://preppindata.blogspot.com/2021/01/2021-week-2.html) to learn data prep. 

**Task: Add [PD2021_Wk2_Input_Bike_Model_Sales.csv](https://github.com/wjsutton/python_charmers/blob/main/data/PD2021_Wk2_Input_Bike_Model_Sales.csv) to your data folder so python can read it and run the following code**

In the following sections I'll show you some data transformations with python for today's challenge. The [Pandas library](https://pandas.pydata.org/docs/reference/index.html) is packed full of useful data prep operations should you need a transformation not mentioned here.
### Load packages and inspect the dataframe
```
import pandas as pd
import numpy as np
from datetime import datetime

# Load csv
df = pd.read_csv('data\\PD2021_Wk2_Input_Bike_Model_Sales.csv')

# see a snapshot of the dataframe
print(df.head())

# see summary info
print(df.info())

# see a the distribution of numerical variables
print(df.describe())

# see a list of the columns 
print(df.columns)

# see data in 1 or multiple columns
print(df['Order Date'])
print(df[['Model','Bike Type']])
```
### Selecting and modifying columns
```
# convert text to uppercase
df['Bike Type'] = df['Bike Type'].str.upper()
print(df['Bike Type'].head())

# round numeric data
df['Value per Bike'] = df['Value per Bike'].round(2)
print(df['Value per Bike'].head())

# convert date formats
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")
print(df['Order Date'].head())

# perform a regex extraction
df['Model'] = df['Model'].str.extract(r'([a-zA-Z]+)')
print(df['Model'].head())

# create a new column as the result of others
df['Order Value'] = df['Quantity'] * df['Value per Bike']
print(df['Order Value'].head())
```
### Aggregrating data
```
# single value result
max_value = df['Value per Bike'].max()
print(max_value)

# group by one column
bikes_sold = df.groupby('Bike Type').agg(Quantity_Sold = ('Quantity','sum'))
print(bikes_sold)

# group by multiple columns and aggregrate multiple columns
bike_rev = df.groupby(
     ['Model','Bike Type']
 ).agg(
     Quantity_Sold = ('Quantity','sum'),
     Order_Value = ('Order Value','sum'),
 ).reset_index()
print(bike_rev)
```
### Task: Finish Preppin' Data 2021 Week 2's challenge

In the [Preppin' Data 2021 Wk2 Challenge](https://preppindata.blogspot.com/2021/01/2021-week-2.html) they ask you to create two output files.

In the script [04_data_prep.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/04_data_prep.py) I have created the first output already, please could you create the second output. 

Use the previous code and the examples here to guide you, comments have been left to guide you if they are confusing please refer to the challenge instructions here: [Preppin' Data 2021 Wk2 Challenge](https://preppindata.blogspot.com/2021/01/2021-week-2.html)

Check your answer against the solution here: [04_data_prep_solution.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/solutions/04_data_prep_solution.py)

