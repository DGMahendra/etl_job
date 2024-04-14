import pandas as pd
# Load the dataset into a pandas DataFrame
survey_data = pd.read_csv("survey_results_public.csv")  # Replace "survey_data.csv" with the actual filename/path

# Extract relevant columns
survey_data = survey_data[["Gender", "Hobbyist", "Country"]]

# Convert gender values to three categories: MAN, WOMAN, and OTHERS
def categorize_gender(gender):
    if pd.isna(gender):
        return "OTHERS"
    elif gender.lower() == "man":
        return "MAN"
    elif gender.lower() == "woman":
        return "WOMAN"
    else:
        return "OTHERS"

survey_data["Gender"] = survey_data["Gender"].apply(categorize_gender)

# Filter data for people who code as a hobby
hobbyist_data = survey_data[survey_data["Hobbyist"] == "Yes"]

# Group the data by gender and continent, count the number of hobbyist coders
report = hobbyist_data.groupby(["Gender", "Country"]).size().reset_index(name="Count")

# Print the report
print("Report for People Who Code as a Hobby Based on Gender and Continent:")
print(report)
