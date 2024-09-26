import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Property_Price_Register_Ireland.csv') # reads the csv

columns = df.columns # Columns of the dataset

unfiltered_data = df.copy() #Copy of the original csv before changes

df.drop('ADDRESS', axis=1, inplace=True) # Get rid of unnecessary columns
sale_price_mean = df['SALE_PRICE'].mean() #Sale Price Mean = 259040.30628275065 = 259040.31
print(sale_price_mean)


#plt.hist(td['Country'], bins=30, edgecolor='black') # Histogram showing the countries most travelled to
#plt.show()

#isnull = ds.isna().sum() #Checking for null values
#print(isnull)
#max_visitors = max(td['Visitors'])

#print(max_visitors)
#print(max_rating)
#print(max_revenue)