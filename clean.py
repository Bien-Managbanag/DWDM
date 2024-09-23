import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

td = pd.read_csv('tourism_dataset.csv')
#tourism_data = tourism_data[['Country', 'Category', 'Visitors', 'Rating', 'Revenue', 'Accomadation_Available']]

remove = ['Location']
td.drop(columns=remove, inplace=True)

#plt.hist(td['Country'], bins=30, edgecolor='black')
#plt.hist(td['Category'], bins=30, edgecolor='black')
#plt.hist(td['Accommodation_Available'], bins=30, edgecolor='black')
#plt.show()

isnull = td.isna().sum() #Checking for null values
#print(isnull)
max_visitors = max(td['Visitors'])
max_rating = max(td['Rating'])
max_revenue = max(td['Revenue'])

print(max_visitors)
print(max_rating)
print(max_revenue)