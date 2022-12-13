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
**jellyfish** is a library for approximate & phonetic matching of strings. We'll be using soundex today, to match words with a similar sound, you can learn more about jellyfish's matching here: [jamesturk/jellyfish](https://github.com/jamesturk/jellyfish)

In this task we'll be working through [Preppin' Data Challenges Week 4 2022](https://preppindata.blogspot.com/2022/01/2022-week-4-prep-school-travel-plans.html) and two datasets [students]() and [travel]()

### Load packages and data
```
import pandas as pd
import numpy as np
import jellyfish

# Input both data sets
students = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/students.csv')
travel = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/travel.csv')
```
