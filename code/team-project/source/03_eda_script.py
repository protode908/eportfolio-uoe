import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
AB_dataset = pd.read_csv('AB_NYC_2019.csv')
print(AB_dataset.head())
print(AB_dataset.info())
print(AB_dataset.isna().sum())
print(AB_dataset.isna().sum().sort_values(ascending=False))
print(AB_dataset.describe())
print(AB_dataset['room_type'].value_counts())
print(AB_dataset['neighbourhood_group'].value_counts())
print(AB_dataset['price'].describe(percentiles=[0.5,0.75,0.95,0.99]))
sns.boxplot(x= 'room_type', y= 'price',data= AB_dataset)
plt.ylim(0,500)
plt.show()
sns.boxplot(x='neighbourhood_group', y= 'price', data = AB_dataset)
plt.ylim(0,500)
plt.show()
AB_dataset.loc[AB_dataset['number_of_reviews']== 0, 'reviews_per_month']=0
AB_dataset = AB_dataset[AB_dataset['name'].notna() & AB_dataset['host_name'].notna()]
AB_dataset = AB_dataset[AB_dataset['price']>0]
AB_dataset['log_price']= np.log1p(AB_dataset['price'])
room_type_map = {'Entire home/apt':1, 'Private room':2, 'Shared room': 3}
AB_dataset['room_type_code']=AB_dataset['room_type'].map(room_type_map)

ng_map = {
    'Manhattan': 1,
    'Brooklyn': 2,
    'Queens': 3,
    'Bronx': 4,
    'Staten Island': 5
    }
AB_dataset['neighbourhood_group_code']= AB_dataset['neighbourhood_group'].map(ng_map)
q99 = AB_dataset['minimum_nights'].quantile(0.99)
AB_dataset['minimum_nights']= AB_dataset['minimum_nights'].clip(upper=q99)
print(AB_dataset.isna().sum())
AB_dataset.to_csv("AB_NYC_2019_cleaned.csv", index = False)
  
modelling_cols = [
    'log_price',
    'room_type_code',
    'neighbourhood_group_code',
    'latitude',
    'longitude',
    'minimum_nights',
    'number_of_reviews',
    'reviews_per_month',
    'availability_365',
    'calculated_host_listings_count'
    ]
with open ("step2_cleaning.log", "w") as log:

    print("=== Step 2 Cleaning Final Log ===", file=log)
    print("", file=log)

    print(f"Final row count:{len(AB_dataset)}", file= log)
    print(f"Final columns: {list(AB_dataset.columns)}", file=log)

    print("", file=log)


    print("Nan per modelling column:", file=log)
    for col in modelling_cols:
        print(f"{col}: {AB_dataset[col].isna().sum()}", file=log)
        print("", file=log)
        print(f"room_type_map:{room_type_map}", file = log)
        print(f"neighbourhood_group_map:{ng_map}", file = log)
        print(f"q99 threshold minimum_nights:{q99}", file = log)
        print("step2_cleaning.log created")



  


