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
- In this py file I worked on each dataset cleaning separately.
- In this first one my plan was to run some basic cleaning by substituting the spaces with underscores and replacing any capital letters with lowercase to ease the computing process later on.
- Then in the first dataset I decided to drop 2 columns the shape_area, and shape_length of the curve, columns since they did not provide any insight that would be useful to me for my analysis of lead levels in the blood.
- After doing so I ensured that all columns were recognized as numerical columns since they were not any categorical columns or values within this dataset.
- Then I also dropped any rows that consisted of missing, NaN, values within the dataset to ensure uniformity.
- Lastly, I decided to not run a z-score analysis since this dataset already contained a limited amount of data, and did not want to create further limitations in my analysis.
- Finally, I saved the new processed clean dataset in a csv format under the processed folder in my datasets folder.
## p3_compute.py:
- In this py script I ensured that all the packages I needed were included in the code to be imported or/and pip installed.
- Then I loaded in the clean datasets
- After doing so I prepared the data by dropping the target variable from the dataset in order to rename it as the y value for my calculations, while also setting the predictor variable as x.
- Then I used standardscaler for data scaling in order to standardize the x values to have a mean of 0 and a standard deviation of 1.
- Then I used the following commands in order to divide the data into trainig and testing data sets by excluding 20% of the data for testing and the rest 80% for analysis.
- After that I used the dummy regressor eval in which I used to calculate the MSE (Mean squared Error) as an evaluation metric for the dummy regressor.
- Then I used the XGBoost regressor evaluation for observations and predictions while also using MSE metric.
- Finally, I saved the models in a pkl format inside the processed dataset directory.
- I repeated the same process for my second dataset as well.

