In the code provided, various techniques are applied for handling missing 
values and outliers in a dataset. First, the dataset `attendance.csv` is loaded 
into a DataFrame `df` using Pandas. The code handles missing values with 
four options: removing rows with missing values, filling missing numerical 
values with their mean or median, and filling categorical columns with the 
mode (most frequent value). Outliers are identified using the Interquartile 
Range (IQR) method, where numeric columns' lower and upper bounds are 
calculated as `Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`, respectively. Outliers can 
then be managed by either removing them, capping them to the IQR bounds, 
or imputing them with the mean or median values of the respective columns. 
The processed DataFrame `df_imputed_outliers` is printed to show the result 
after handling both missing values and outliers. This preprocessing step is 
essential in machine learning to improve model performance by reducing 
noise and ensuring complete data.
