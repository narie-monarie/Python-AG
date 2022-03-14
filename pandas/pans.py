import pandas as pd
# How would you access the first-row and first column in the dataframe df? df.ix[0,0]
# What is the proper way to load a CSV file using pandas?  pandas.read_csv(‘data.csv’)


csv_path = 'file1.csv'
df = pd.read_csv(xlsx_path)
df.head()
