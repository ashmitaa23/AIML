# Implement the missing value, and outlier handling data 
preprocessing techniques on the dataset imported. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# Load your dataset 
df = pd.read_csv('attendance.csv')  # loads the dataset from a CSV 
f
 ile into a DataFrame 'df' 
# Handling Missing Values 
# Option 1: Remove rows with missing values 
df_cleaned = df.dropna()  # removes all rows containing any missing 
values in 'df' and saves the result in 'df_cleaned' 
# Option 2: Fill missing values with the mean (for numerical 
columns) 
df_filled = df.fillna(df.select_dtypes(include=np.number).mean())  # 
f
 ills missing values in numerical columns with the mean of each 
column 
# Option 3: Fill missing values with the median (for numerical 
columns) 
df_filled_median = 
df.fillna(df.select_dtypes(include=np.number).median())  # fills 
missing values in numerical columns with the median of each 
column 
# Option 4: Fill missing values with the mode (for categorical 
columns) 
df_filled_mode = df.apply(lambda x: x.fillna(x.mode()[0]) if x.dtype == 
'O' else x)  # fills missing values in categorical columns with the 
mode (most frequent value) 
# Handling Outliers 
# Using the Interquartile Range (IQR) method 
Q1 = df.select_dtypes(include=np.number).quantile(0.25)  # 
calculates the 1st quartile (25th percentile) for numerical columns 
Q3 = df.select_dtypes(include=np.number).quantile(0.75)  # 
calculates the 3rd quartile (75th percentile) for numerical columns 
IQR = Q3 - Q1  # calculates the Interquartile Range (IQR) for each 
numerical column 
# Define outlier bounds 
lower_bound = Q1 - 1.5 * IQR  # sets the lower bound for outliers 
based on IQR 
upper_bound = Q3 + 1.5 * IQR  # sets the upper bound for outliers 
based on IQR 
# Identify outliers 
outliers = ((df.select_dtypes(include=np.number) < lower_bound) | 
(df.select_dtypes(include=np.number) > upper_bound))  # identifies 
cells that contain outliers in numerical columns 
# Option 1: Remove outliers 
df_no_outliers = df[~((df.select_dtypes(include=np.number) < 
lower_bound) | (df.select_dtypes(include=np.number) > 
upper_bound)).any(axis=1)]  # removes rows that have any outliers 
in numerical columns 
# Option 2: Cap outliers to the lower and upper bounds 
df_capped = df.copy()  # creates a copy of 'df' for capping outliers to 
upper and lower bounds 
numeric_df = df.select_dtypes(include=np.number)  # selects only 
numerical columns for further processing 
for col in numeric_df.columns: 
df_capped.loc[numeric_df[col] < lower_bound[col], col] = 
lower_bound[col]  # caps values below the lower bound to the 
lower bound 
df_capped.loc[numeric_df[col] > upper_bound[col], col] = 
upper_bound[col]  # caps values above the upper bound to the 
upper bound 
# Option 3: Impute outliers with mean/median 
df_imputed_outliers = df.copy()  # creates a copy of 'df' for 
imputation of outliers 
df_imputed_outliers[outliers] = np.nan  # replaces outliers in 'df' 
with NaN to prepare for imputation 
# Calculate the mean only for numeric columns 
numeric_df = df.select_dtypes(include=np.number)  # selects 
numeric columns from 'df' 
df_imputed_outliers = df_imputed_outliers.fillna(numeric_df.mean())  
# fills NaN values (outliers) with the mean of each numerical 
column 
print("Original DataFrame:\n", df)  # prints the original DataFrame 
for comparison 
print("DataFrame after handling missing values and outliers:\n", 
df_imputed_outliers)  # prints the DataFrame after handling missing 
values and outliers 
