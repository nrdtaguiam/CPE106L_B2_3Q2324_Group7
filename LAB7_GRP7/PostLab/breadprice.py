import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'breadprice.csv'
bread_df = pd.read_csv(filepath)

# data cleaning
bread_df = bread_df.dropna(axis='columns', how='all')
bread_df = bread_df.dropna(axis='index', thresh=12)
bread_df = bread_df.iloc[:, 1:].mode(axis=1)

# average price of bread
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
average_column = []
for idx, row in bread_df.iterrows():
    if not row.empty:
        average = row.mean()
        average_column.append(average)
        print(f"Average of row {idx} : {average}")

dict = {
    'Years': years,
    'Average Bread Price': average_column
}
bread_avg_df = pd.DataFrame({
    'Average Bread Price': average_column
}, index=years)

# plotting of data
bread_avg_df.plot(kind='line', xlabel='Years', ylabel='Average Price of Bread', )
plt.show()
