# Substituting the NaN values with the median
heart_data.fillna(heart_data.median(), inplace=True)

# Using the z scores for the columns age and cholesterol in order to manage the outliers
z_scores = np.abs(stats.zscore(heart_data[['age', 'chol']]))
heart_data_no_outliers = heart_data[(z_scores < 3).all(axis=1)]

# Saving the cleaned dataset
heart_data_encoded.to_csv('datasets/heart_disease_cleaned.csv', index=False)