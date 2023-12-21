# Start by installing the seaborn package. You can do this by running the following command in your terminal or command prompt:

#`pip install seaborn`
# Next, open your Python interpreter or IDE and import the seaborn package, along with the pandas and matplotlib packages, which are required by seaborn:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Next, load your dataset into a pandas DataFrame. You can do this by using the read_csv() function from pandas, which takes a file path or URL as an argument:

data = pd.read_csv('https://raw.githubusercontent.com/wjsutton/python_charmers/main/data/player_shooting.csv')
# Once your data is loaded, you can use seaborn to create visualizations of your data. For example, you could create a scatter plot using the scatterplot() function, which takes the x and y variables as arguments:

sns.scatterplot(x='shots', y='shots_on_target', data=data)


sns.heatmap(data.corr())
# You can customize your plot by adding additional arguments to the function call. For example, you could change the color and size of the points, or add a title and axis labels:

#sns.scatterplot(x='column_1', y='column_2', data=data,
#                color='red', size='column_3',
#                title='My Scatter Plot', xlabel='Column 1', ylabel='Column 2')
# To display your plot, you can use the show() function from matplotlib, which will open a new window with your plot:

plt.show()
# This is just a simple example of what you can do with seaborn, and there are many other functions and options available for creating different types of plots and visualizations. I hope this helps and inspires you to explore seaborn further!