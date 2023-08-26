# Big Data Engineer Project

Link to the datasets: https://drive.google.com/drive/folders/1Mrb-DvhIM8cj44Rjp1Aa92YZXEVWCebJ?usp=sharing

We have 3 dataframes: facebook, google, website.csv. 

Merge the 3 dataframes into a 4th one using Python. Below are the steps to achieve this:

1. Imported the necessary libraries, Pandas and NumPy.
2. Loaded the three datasets into DataFrames.
3. Standardized the column names in each DataFrame.
4. Handled missing values in each DataFrame by replacing empty strings with NaN values.
5. Ensured that the data types in each DataFrame were correct.
6. Removed duplicate rows from each DataFrame.
7. Checked if the address column exists in each DataFrame. If it does, you stripped whitespace from the column values.
8. Merged the three DataFrames using an outer join.
9. Cleaned the category column by stripping whitespace from the column values.
10. Selected the final columns that you wanted to keep.
11. Filtered out rows with missing data in any of the selected columns.
12. Saved the final DataFrame to a CSV file.
13. Dropped the unnamed columns from the final DataFrame.

Here is a more detailed explanation of each step:

- Importing the necessary libraries: I have imported the Pandas and NumPy libraries, which are both required for data manipulation and analysis in Python.
- Loaded the three datasets: I have loaded the three datasets into DataFrames using the read_csv() function from the Pandas library.
- Standardizing the column names: I have standardized the column names in each DataFrame by renaming them to make them more consistent.
- Handling missing values: Handled the missing values in each DataFrame by replacing empty strings with NaN values. This is important because NaN values can cause errors when you try to 
perform data analysis.
- Ensuring that the data types are correct: Ensured that the data types in each DataFrame were correct by converting any string columns to numeric columns if necessary. This is important 
because different data types can be used for different types of analysis.
- Removing duplicate rows: Removed duplicate rows from each DataFrame to avoid counting the same data multiple times.
- Checking if the address column exists in each DataFrame: Checked if the address column exists in each DataFrame because you only wanted to keep rows that have this column.
- Merging the three DataFrames using an outer join: Merged the three DataFrames using an outer join, which keeps all the rows from all the DataFrames, even if there are missing values. 
This is because I wanted to keep all the data about each company, even if some of the data was missing from one or more of the DataFrames.
- Cleaning the category column: Cleaned the category column by stripping whitespace from the column values. This is important because whitespace can cause errors when you try to 
perform text analysis on the column values.
- Selecting the final columns: Selected the final columns that you wanted to keep, which were company_name, category, address, and phone.
- Filtering out rows with missing data in any of the selected columns: Filtered out rows with missing data in any of the selected columns to avoid analyzing incomplete data.
- Saving the final DataFrame to a CSV file: Saved the final DataFrame to a CSV file so that you could easily access it later.
- Dropping the unnamed columns: Dropped the unnamed columns from the final DataFrame to make it easier to read and understand.
