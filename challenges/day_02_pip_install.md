<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 02: Pip install...

The python community develop and maintain packages of code allowing you to perform several different tasks easily. 

For example:

- `pandas.read_csv()` will let you read csv files 

Numpy and pandas are two incredibly helpful packages for data manipulation. Today we’ll install them and start using them.


Let's get started

- Open VS Code
- Top Menu  Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:

```
pip install pandas
pip install numpy 
```

“Pip” is python’s package installer. If you receive errors, it may be that pip isn’t installed, in which case try running: 

```
python -m pip install --upgrade pip 
```

Often when working with python you'll need to pick up another person's script to fix a problem or adapt it to your own needs. 

So today we'll be working through:

- installing required packages
- executing the script
- modifying the script

### The Script

We'll be working through a [python script](https://github.com/wjsutton/python_charmers/blob/main/scripts/02_pip_install.py) that modifies our [Bike Sales data](https://github.com/wjsutton/python_charmers/blob/main/data/PD%202021%20Wk%201%20Input%20-%20Bike%20Sales.csv). 

The script reads the data, modifies the columns, filters out some orders, writes the data to a csv file locally, and then prints "data prepped" to the terminal window. 

```
import pandas as pd
import numpy as np

# Load csv
data = pd.read_csv('data\\PD 2021 Wk 1 Input - Bike Sales.csv')

# Split the 'Store-Bike' into 'Store' and 'Bike'
data[['Store','Bike']] = data['Store - Bike'].str.split(' - ', expand=True)

# Clean up the 'Bike' field to: Mountain, Gravel, Road
data['Bike'] = data['Bike'].str.lower()
data['Bike'] = data['Bike'].str[0]
data['Bike'] = np.where(data['Bike']=='m','Mountain',np.where(data['Bike']=='r','Road','Gravel'))

# Create a 'Quarter' and 'Day of Month' fields
data['Date'] = pd.to_datetime(data['Date'], format="%d/%m/%Y")
data['Quarter'] = data['Date'].dt.quarter 
data['Day of Month'] = data['Date'].dt.day 

# Remove the first 10 orders
data = data.loc[(data['Order ID'] >= 11)]

# Output the data as a csv
data = data.drop(['Store - Bike','Date'], axis=1)
data.to_csv('output\\PD 2021 Wk 1 Output - Bike Sales.csv', index=False)

print("data prepped!")
```
Source: my solution to [Week 2021 Preppin' Data Challenge](https://preppindata.blogspot.com/2021/01/2021-week-1.html)


A few notes

- a `#` indicates a comment, meaning everything on the line after `#` will not be executed by python
- packages are included in a script using `import packagename`
- `import packagename as pk` meaning you only need to state `pk.` before a package function rather than the full package name


### The Task

Run the [python script](https://github.com/wjsutton/python_charmers/blob/main/scripts/02_pip_install.py) locally so it outputs a dataset. 

Areas to watch out for
- ensure you have the required packages installed using `pip install ...`
- check where your data is stored, note the `data\\` prefix indicates the file is stored in a folder named "data"
- check where your script is being run from (working directory) in the terminal, you can change this using the `cd path/to/my/script` 


#### Bonus Task

We'll be covering data transformations in a later project if you have time:

- Check what the transformations are doing against the [pandas](https://pandas.pydata.org/docs/reference/general_functions.html) and [numpy](https://numpy.org/doc/stable/reference/routines.math.html) docs 
- Remove the filter on orders
- Change the Store column output in uppercase 
