import pandas as pd

# List of files to merge
files = [
    'cleaned_cleaned_architect-engineer.xlsx',
    'cleaned_cleaned_consultant.xlsx',
    'cleaned_cleaned_design-graphic.xlsx',
    'cleaned_cleaned_lifestyle_category.xlsx',
    'cleaned_cleaned_marketing-advertising.xlsx',
    'cleaned_cleaned_photography-video.xlsx',
    'cleaned_cleaned_web-programming.xlsx',
    'cleaned_cleaned_writing-translation.xlsx'
]

# Desired column order
columns_order = [
    'category_id',
    'title',
    'namefreelance',
    'web-scraper-order',
    'web-scraper-start-url',
    'link',
    'rating_comment',
    'Num_comment',
    'cost',
    'percentsuccess',
    'num_sold',
    'repeat hired'
]

# Initialize an empty list to store DataFrames
dfs = []

# Read each file
for file in files:
    try:
        df = pd.read_excel(file, engine='openpyxl')

        # Ensure the DataFrame has the columns in the specified order
        df = df[columns_order]

        # Append the DataFrame to the list
        dfs.append(df)
    except Exception as e:
        print(f"Error loading file {file}: {e}")

# Check if there are DataFrames to concatenate
if dfs:
    # Concatenate all DataFrames
    merged_df = pd.concat(dfs, ignore_index=True)

    # Add the Post_ID column
    merged_df.insert(0, 'Post_ID', range(1, len(merged_df) + 1))

    # Save the merged DataFrame to a new Excel file
    output_file = "merged_data.xlsx"
    try:
        merged_df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Merged data has been saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")
else:
    print("No DataFrames to concatenate")
