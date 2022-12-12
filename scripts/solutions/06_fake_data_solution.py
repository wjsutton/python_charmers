import pandas as pd
import numpy as np
from faker import Faker

# set faker seed
Faker.seed(4321)
fake = Faker()

# define lists
employee_id = []
names = []
gender = []
address = []
job_title = []
start_date = []
date_of_birth = []

# loop to create 50 records
for a in range(50):
    # add number to list
    employee_id += [a]
    
    # define boolean True/False to determine gender
    boolean = fake.boolean()
    gender += [np.where(boolean,'Female','Male')]
    names += [np.where(boolean,fake.name_female(),fake.name_male())]

    address += [fake.address()]
    job_title += [fake.job()]
    start_date += [fake.date_this_decade()]
    date_of_birth += [fake.date_of_birth(minimum_age = 16)]

# add lists to dataframe, with column names
df = pd.DataFrame(
    {
        'employee_id': employee_id,
        'name': names,
        'gender': gender,
        'address': address,
        'start_date': start_date,
        'date_of_birth': date_of_birth
    }
    )

# write datasets to csv
df.to_csv('output\\fake_dataset.csv', index=False)
