import pandas as pd 

# Dataset 1: Lead blood levels
datalink1 = 'https://data.ferndalemi.gov/datasets/D3::leadbloodlevels-2017-bymsa-20181129.csv?where=1=1&outSR=%7B%22latestWkid%22%3A2898%2C%22wkid%22%3A2898%7D'

df = pd.read_csv(datalink1)
df.size
df.sample(5)

## save as csv to WK9/code/model_dev/data/raw
df.to_csv('WK9/code/model_dev/data/raw/crime_data.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('WK9/code/model_dev/data/raw/crime_data.pkl')

####################################
# Dataset 2: Peds ED and PC visits
