##Based on this survey, what will be the most desired programming language for the year 2020

import pandas as pd

# Load the dataset into a pandas DataFrame
survey_data = pd.read_csv("survey_results_public.csv")  # Replace "survey_data.csv" with the actual filename/path

# Filter the data for the year 2020
survey_data_2020 = survey_data[survey_data["LanguageDesireNextYear"] == 2020]  # Replace "Column_Representing_Year" with the actual column name

# Extract the "LanguageDesireNextYear" column and split the strings into lists of programming languages
languages_desired = survey_data_2020["LanguageDesireNextYear"].dropna().str.split(";")

# Flatten the lists of programming languages
all_languages = [language.strip() for sublist in languages_desired for language in sublist]

# Count the occurrences of each programming language
language_counts = pd.Series(all_languages).value_counts()

# Print the most desired programming language for 2020
most_desired_language = language_counts.idxmax()
print("The most desired programming language for 2020 is:", most_desired_language)
