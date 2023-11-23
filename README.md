# datasci_9_data_prep
HHA 507- Assignment Week #9

## Datasets:
- [Leadblood levels]:
This dataset presents information on lead blood levels in Michigan for the year 2017, organized by the Metropolitan Statistical Area (MSA). Elevated blood lead levels (EBLL) are defined as exceeding 4.5 micrograms of lead per deciliter of blood (μg/dL). The data, sourced from the Michigan Department of Health and Human Services, was aggregated and anonymized by Data Driven Detroit. Null values in certain areas indicate a lack of blood lead level testing or suppressed numbers (fewer than 6) to safeguard individual privacy.
- [Peds ED visits data]:
This dataset, managed by the Record Research Request Service (R3) at the University of Pittsburgh, focuses on UPMC clinical data for pediatric populations (ages 0-17) in Allegheny County. It covers emergency department (ED) categorized by Census Block Group geography using 2010 U.S. Census data. The ED data includes total visits, specific to asthma, injury, low-acuity, and respiratory tract infections. Low-acuity visits refer to less-serious or less-urgent cases discharged to normal residence. Primary care visit data includes total visits, well-child visits, and asthma diagnoses. It also includes estimated block group populations from the U.S. Census Bureau's 2015-19 American Community Survey.

## p1_extract.py:
- After creating a ```datasets``` folder which I divided into raw and processed data folders, I loaded in the datasets in the first py file named ```p1_extract.py```.
- Inside that py file I included the dataset loading process for both datasets while also saving and creating a pickle format for both and saving them inside the raw folder within the datasets.
## p2_transform.py:
- In this py file I worked on each dataset cleaning seperately.
- In this first one my plan was to run some basic cleaning by substituting the spaces with underscores, and replace any capital letters with lower case to ease the computing process later on.
- Then in the first dataset I decided to drop 2 columns the shape_area, and shape_length of the curve, columns since they did not provide any insight that would be useful to me for my analysis of lead levels in the blood.
- After doing so I ensured that all columns were recognized as numerical columns since they were not any categorical columns or values within this dataset.
- Then I also dropped any rows that consisted of missing, NaN, values within the dataset to ensure uniformity.
- Lastly, I decided to not run a z-score analysis since this dataset already contained a limited amount of data and did not want to create further limitations in my analysis.
- Finally, I saved the new processed clean dataset in a csv format under the processed folder in my datasets folder.

