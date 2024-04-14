#1. Find the average age of developers when they wrote their first line of code

# Age1stcode column actually defines the age at which the developers write their first line of code

import pandas as pd

# Load the dataset
df = pd.read_csv('survey_results_public.csv')

# Extract the 'Age1stCode' column
age_first_code = df['Age1stCode']

# Convert the values in the 'Age1stCode' column to numeric
age_first_code_numeric = pd.to_numeric(age_first_code, errors='coerce')

# Calculate the average age
average_age_first_code = age_first_code_numeric.mean()

print("Average age of developers when they wrote their first line of code:", average_age_first_code)
