import pandas as pd
import numpy as np

#Load the dataframes
facebook_df = pd.read_csv('facebook_dataset.csv', dtype=str, low_memory=False)
google_df = pd.read_csv('google_dataset.csv', dtype=str, low_memory=False)
website_df = pd.read_csv('website_dataset.csv', dtype=str, low_memory=False)

#Adding print statements to check the data after every step
#print(google_df.head())

#Data cleaning

#1. Standardize Column Names
facebook_df = facebook_df.rename(columns={'domain': 'company_name'})
google_df = google_df.rename (columns={'domain': 'company_name'})
website_df = website_df.rename(columns={'domain': 'company_name'})

#adding print statements to check the data after every step
#print(google_df.head())

#2. Handle Missing Values using numpy
#Replace empty strings with NaN values
facebook_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
google_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
website_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

#3. Ensure the Data Types
facebook_df['phone'] = facebook_df['phone'].astype(str)
google_df['phone'] = google_df['phone'].astype(str)
website_df['phone'] = website_df['phone'].astype(str)

#adding print statements to check the data after every step
# print(google_df.head())

#4. remove Duplicates
facebook_df.drop_duplicates(subset=['company_name'], keep='first', inplace=True)
google_df.drop_duplicates(subset=['company_name'], keep='first', inplace=True)
website_df.drop_duplicates(subset=['company_name'], keep='first', inplace=True)

#Adding print statements to check the data after every step
# print(google_df.head())

#Check if 'address' column exists in each DataFrame by adding if statements
if 'address' in facebook_df.columns:
    facebook_df['address'] = facebook_df['address'].str.strip()
if 'address' in google_df.columns:
    google_df['address'] = google_df['address'].str.strip()
if 'address' in website_df.columns:
    website_df['address'] = website_df['address'].str.strip()

#5. Merging the DataFrames using an outer join
common_column = 'company_name'

merged_df = pd.merge(facebook_df, google_df, on=common_column, how='outer')
merged_df = pd.merge(merged_df, website_df, on=common_column, how='outer')

#6. Clean Columns: Strip whitespace from 'category' column
merged_df['category'] = merged_df['category'].str.strip()

#7. Select final columns
final_columns = ['company_name', 'category', 'address', 'phone']

#8. filter out rows with missing data in any of the selected columns
merged_df.dropna(subset=final_columns, how='all', inplace=True)

#9. Save the final dataframe to a .csv file
merged_df.to_csv('final_dataframe.csv', index=False)

#10. Drop the unnamed columns:

#Load the 4th (final) dataframe
df = pd.read_csv('final_dataframe.csv', dtype=str, low_memory=False)

# Get the list of unnamed columns
unnamed_columns = [column for column in df.columns if column.startswith('Unnamed:')]

#Drop the unnamed columns
df.drop(unnamed_columns, axis=1, inplace=True)

#Save the modified DataFrame final_dataframe.csv
df.to_csv('final_dataframe.csv', index=False)

#Print the final dataframe
print(merged_df)
