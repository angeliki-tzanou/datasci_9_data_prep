import pandas as pd 

# Dataset 1: Lead blood levels
datalink1 = 'https://data.ferndalemi.gov/datasets/D3::leadbloodlevels-2017-bymsa-20181129.csv?where=1=1&outSR=%7B%22latestWkid%22%3A2898%2C%22wkid%22%3A2898%7D'

df = pd.read_csv(datalink1)
df.size
df.sample(5)

## save as csv within the data folder under raw
df.to_csv('datasets/raw/LeadBloodLevels_2017_byMSA.csv', index=False)

## save as pickle within the data folder under raw
df.to_pickle('datasets/raw/LeadBloodLevels_2017_byMSA.pkl')

####################################
# Dataset 2: Peds ED visits

datalink2 = 'https://data.wprdc.org/dataset/6ff17545-2e53-4e51-a9e4-0c4681ad3e4b/resource/17c21e89-ad01-47f5-a8b2-29bdd493666b/download/r3_ed_opendata.csv'
df = pd.read_csv(datalink2)
df.size
df.sample(5)

## save as csv within the data folder under raw
df.to_csv('datasets/raw/Peds_ED_visits.csv', index=False)

## save as pickle within the data folder under raw
df.to_pickle('datasets/raw/Peds_ED_visits.pkl')