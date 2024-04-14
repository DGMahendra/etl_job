##Deduce the percentage of developers who knew python in each country.
import pandas as pd

survey_data = pd.read_csv('survey_results_public.csv')   #loading the dataset

# Filter the DataFrame to include only developers
developers = survey_data[survey_data['MainBranch'] == 'I am a developer by profession']

# Count the number of developers who know Python for each country
python_developers_count = developers.groupby('Country')['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

# Count the total number of developers for each country
total_developers_count = developers['Country'].value_counts()

# Calculate the percentage of developers who know Python for each country
python_percentage = (python_developers_count / total_developers_count) * 100

# Print the result
print(python_percentage)
