<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 06: Build a fake dataset

Today we’ll be diving into Python's faker package to build a fake list of employees and their details.

**Task: Pip install faker**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install faker
```

### Faker basics

```
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
```

Rerunning this will return a different result. To keep the results consistent we add a seed with a number e.g. `Faker.seed(4321)`

```
import pandas as pd
import numpy as np
from faker import Faker

Faker.seed(4321)
fake = Faker()

print(fake.name())
print(fake.address())
```

There are a huge range of fake data fields you can use, either standard with the faker package or by installing community package:

- [Standard Providers](https://faker.readthedocs.io/en/master/providers.html)
- [Community Providers](https://faker.readthedocs.io/en/master/communityproviders.html)
- [Local Providers](https://faker.readthedocs.io/en/master/locales/en_GB.html#faker-providers-address)


### Loops

For our fake data, we want more than 1 record, and we can achieve this with a loop and range.

`range` returns a list of numbers, defaulting at zero, incrementing by one, up to but not including the variable given:
e.g. print(range(5)) will return 0 to 4

```
for a in range(5):
    print(a)
``` 
Ultimately we get 5 values returned, which we can use for generating our fake data

```
for a in range(5):
    print(fake.name())
```
Note we don't have to reference a when performing our loop.

### Write loops to dataframe

To do this we can add our loop returns to a list, then add that list to a data.frame

In python  [] indicates the contents are in a list, you can combine lists [a] + [b] = [a,b]

```
names = []

for a in range(5):
    names = names + [fake.name()]
    
print(names)
```
We should then see a list containing 5 fake names.

alternative we can write 
```
names = names + [fake.name()]
```
as
```
names += [fake.name()]
```
Where += says, take the list `names` and add `[fake.name()]`

Now get the list to a dataframe

```
df = pd.DataFrame(
    {
        'name': names
    })
```
Where `names` is our list of fake names, and `'name'` is the column header.

### To recap. 

```
import pandas as pd
import numpy as np
from faker import Faker

Faker.seed(4321)
fake = Faker()

for a in range(5):
    names += [fake.name()]
    
df = pd.DataFrame(
    {
        'name': names
    }) 

print(df)
```

### Task 

We trying to replace the personal details of 50 employees with some fake data. 

Take the script [06_fake_data.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/06_fake_data.py) and make the following changes:

- add male and female names based on the Gender use `np.where(statement,True condition,False condition)`
- add a start date from last 10 years
- add a date of birth so the employee's minimum age is 16

Check your answer against the solution here: [06_fake_data_solution.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/solutions/06_fake_data_solution.py)
