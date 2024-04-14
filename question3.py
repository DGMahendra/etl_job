#Generate the report for the average salary of developers based on the continent

import pandas as pd

data = pd.read_csv('survey_results_public.csv')

developers = data[data['MainBranch'] == 'I am a developer by profession'] #grouping developers only
developers = developers[['Country', 'ConvertedComp']]

# Load the country to continent mapping data
country_continent_mapping = pd.read_csv("Countries-Continents.csv")  # Adjust the file path as needed

# Merge the country to continent mapping data with the developers salary data
developers= developers.merge(country_continent_mapping, how='left', on='Country')

# Group the data by continent and calculate the average salary for each continent
average_salary_by_continent = developers.groupby('Continent')['ConvertedComp'].mean()

# Generate the report
print(average_salary_by_continent)