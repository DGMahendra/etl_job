import pandas as pd

# Load the dataset
survey_data = pd.read_csv('survey_results_public.csv')

# Filter the dataset to include only developers
developer_data = survey_data[survey_data['MainBranch'] == 'I am a developer by profession']

# Group the data by gender and continent
grouped_data = developer_data.groupby(['Gender', 'Country'])

# Calculate the average job and career satisfaction for each group
satisfaction_report = grouped_data.agg({
    'JobSat': 'mean',
    'CareerSat': 'mean'
}).reset_index()

# Generate the report
print("Report for Job and Career Satisfaction of Developers based on Gender and Continent:")
print(satisfaction_report)
