import pandas as pd
import os

# List of file names
files = [
    "cleaned_architect-engineer copy.xlsx",
    "cleaned_cleaned_architect-engineer.xlsx",
    "cleaned_cleaned_consultant.xlsx",
    "cleaned_cleaned_design-graphic.xlsx",
    "cleaned_cleaned_lifestyle_category.xlsx",
    "cleaned_cleaned_marketing-advertising.xlsx",
    "cleaned_cleaned_photography-video.xlsx",
    "cleaned_cleaned_web-programming.xlsx",
    "cleaned_cleaned_writing-translation.xlsx"
]

dfs = []

for file in files:
    try:
        df = pd.read_excel(file)
        # Check if the required columns are in the dataframe
        if 'category_d' in df.columns and 'link_href' in df.columns:
            dfs.append(df)
        else:
            print(f"Error loading file {file}: required columns not found")
    except Exception as e:
        print(f"Error loading file {file}: {e}")

# Check if there are dataframes to concatenate
if dfs:
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_excel("merged_output.xlsx", index=False)
    print("Merged file created successfully.")
else:
    print("No objects to concatenate")
