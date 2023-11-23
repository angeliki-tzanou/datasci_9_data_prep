import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df1 = pd.read_pickle('datasets/raw/LeadBloodLevels_2017_byMSA.pkl')

## get column names
df1.columns
df1.head(10)

## do some data cleaning of colun names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df1.columns = df1.columns.str.lower().str.replace(' ', '_')
df1.columns

## get data types
df1.dtypes # nice combination of numbers and strings/objects 
len(df1)

## drop the two columns that we are not conserned with measuring the area of graph curve they had created
to_drop = ['shape__area', 'shape__length']
df1.drop(to_drop, axis=1, inplace=True, errors='ignore')

# keeping the rest of the columns that we want to include in the data measurements
to_keep = ['objectid', 'geoid10_msa', 'cnttested', 'ebll', 'under6cnttested',
       'under6ebll', 'under18cnttested', 'under18ebll', 'pctebll',
       'pctunder6ebll', 'pctunder18ebll']

# Ensure each column is recognized as numerical since this dataset has ONLY numerical columns:
df1_clean = df1[to_keep]
## Hence applying it all the columns:
df1_clean = df1_clean.apply(pd.to_numeric, errors='coerce')
## Dropping any rows with NaN values if present 
df1_clean.dropna(inplace=True)

df1_clean.head(10)
df1_clean.columns 

## Since the dataset is really small, made the decision to not z_score test so it wont limit the data provided further
### z_scores = np.abs(stats.zscore(df1[['cnttested', 'ebll', 'under6cnttested','under6ebll', 'under18cnttested', 'under18ebll']]))
### df1_clean_NO_outliers = df1[(z_scores < 3).all(axis=1)]


## save clean data to csv under processed in datasets
df1_clean.to_csv('datasets/processed/LeadBloodLevels_2017_byMSA.csv', index=False)

