import pandas as pd
import numpy as np
from datetime import datetime

# Load csv
df = pd.read_csv('data\\PD2021_Wk2_Input_Bike_Model_Sales.csv')

# Clean up the Model field to leave only the letters to represent the Brand of the bike
df['Model'] = df['Model'].str.extract(r'([a-zA-Z]+)')

# Workout the Order Value using Value per Bike and Quantity
df['Order Value'] = df['Quantity'] * df['Value per Bike']

# Calculate Days to ship by measuring the difference between when an order was placed and when it was shipped as 'Days to Ship'
df['Shipping Date'] = pd.to_datetime(df['Shipping Date'], format="%d/%m/%Y")
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")

df['Days to Ship'] = df['Shipping Date'].sub(df['Order Date'], axis=0)
df['Days to Ship'] = df['Days to Ship']/ np.timedelta64(1, 'D')

# Aggregate Value per Bike, Order Value and Quantity by Brand and Bike Type to form:
# - Quantity Sold
# - Order Value
# - Average Value Sold per Brand, Type
output_1 = df.groupby(
     ['Model','Bike Type']
 ).agg(
     Quantity_Sold = ('Quantity','sum'),
     Order_Value = ('Order Value','sum'),
 ).reset_index()

output_1['Average Value Sold'] = output_1['Order_Value'] / output_1['Quantity_Sold']

# Round any averaged values to one decimal place to make the values easier to read
output_1['Average Value Sold'] = output_1['Average Value Sold'].round(1)

# renaming columns
new_output_1_columns = output_1.columns.values
new_output_1_columns = ['Brand', 'Bike Type', 'Quantity Sold', 'Order Value', 'Avg Bike Value per Brand']
output_1.columns  = new_output_1_columns

# writing data to csv
output_1.to_csv('output\\PD2021_Wk2_Output_1.csv', index=False)

# Aggregate Order Value, Quantity and Days to Ship by Brand and Store to form:
# - Total Quantity Sold
# - Total Order Value
# - Average Days to Ship
output_2 = df.groupby(
     ['Model','Store']
 ).agg(
     Total_Quantity_Sold = ('Quantity','sum'),
     Total_Order_Value = ('Order Value','sum'),
     Average_Days_to_Ship = ('Days to Ship','mean'),
 ).reset_index()

# Round any averaged values to one decimal place to make the values easier to read
output_2['Average_Days_to_Ship'] = output_2['Average_Days_to_Ship'].round(1)

# Output File 2. Sales by Brand and Store
# 5 Data Fields: Brand, Store, Total Quantity Sold, Total Order Value, Avg Days to Ship
# 25 Rows (26 including headers)

# renaming columns
new_output_2_columns = output_2.columns.values
new_output_2_columns = ['Brand', 'Store', 'Total Quantity Sold', 'Total Order Value', 'Avg Days to Ship']
output_2.columns  = new_output_2_columns

# writing data to csv
output_2.to_csv('output\\PD2021_Wk2_Output_2.csv', index=False)

print("data prepped!")