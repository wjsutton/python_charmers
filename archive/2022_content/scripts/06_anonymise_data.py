import pandas as pd
import numpy as np
from faker import Faker

Faker.seed(4321)
fake = Faker()

employee_id = []
names = []
gender = []
address = []
job_title = []
start_date = []
date_of_birth = []

for a in range(50):
    employee_id += [a]
    
    boolean = fake.boolean()
    gender += [np.where(boolean,'Female','Male')]
    names += [np.where(boolean,fake.name_female(),fake.name_male())]

    address += [fake.address()]
    job_title += [fake.job()]
    start_date += [fake.date_this_decade()]
    date_of_birth += [fake.date_of_birth(minimum_age = 16)]

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

df.to_csv('output\\fake_dataset.csv', index=False)