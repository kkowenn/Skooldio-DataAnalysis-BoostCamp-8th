import sys
import os
import pandas as pd

def main():
    # Check if the user has provided the input file
    if len(sys.argv) < 2:
        print("Usage: python3 cleaning.py <input_file.xlsm>")
        return

    input_file = sys.argv[1]

    # Extract the directory and filename from the input file path
    directory, filename = os.path.split(input_file)

    # Create the output file name
    output_file = os.path.join(directory, "cleaned_" + filename)

    # Load the input file
    try:
        data = pd.read_excel(input_file, engine='openpyxl')
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Replace specific text in the num_sold column with empty data
    data['num_sold'] = data['num_sold'].replace(
        'มั่นใจ! ฟรีแลนซ์ในหมวดนี้มี "ประกาศนียบัตร" หรือ "ใบรับรองวิชาชีพ"', '')

    # Replace values containing percentages in the time respond column with a hyphen
    data['time respond'] = data['time respond'].apply(lambda x: '-' if '%' in str(x) else x)

    # Function to convert hours to minutes and clean up minutes
    def convert_time_to_minutes(time_str):
        if 'ชั่วโมง' in time_str:
            hours = float(time_str.split()[0])
            return int(hours * 60)
        elif 'นาที' in time_str:
            minutes = int(time_str.replace('นาที', '').strip())
            return minutes
        return time_str

    # Apply the conversion function to the time respond column
    data['time respond'] = data['time respond'].apply(lambda x: convert_time_to_minutes(str(x)))

    # Function to clean up "ครั้ง" and convert to integer
    def clean_times_column(column):
        def convert_value(x):
            x_str = str(x).replace('ครั้ง', '').replace('K', '000').strip()
            try:
                return int(float(x_str))
            except ValueError:
                return x
        return column.apply(convert_value)

    # Apply the cleanup function to num_sold and repeat hired columns
    data['num_sold'] = clean_times_column(data['num_sold'])
    data['repeat hired'] = clean_times_column(data['repeat hired'])

    # Replace NaN in the rating_comment column with zero
    data['rating_comment'] = data['rating_comment'].fillna('0 (0)')

    # Extract rating and number of comments
    data['Num_comment'] = data['rating_comment'].str.extract(r'\((\d+)\)').fillna(0).astype(int)
    data['rating_comment'] = data['rating_comment'].str.extract(r'([0-9.]+)').astype(float)

    # Drop duplicates based on both title and namefreelance columns
    df_cleaned = data.drop_duplicates(subset=["title", "namefreelance"])

    # Ensure columns are converted to numeric types
    df_cleaned['num_sold'] = pd.to_numeric(df_cleaned['num_sold'], errors='coerce').fillna(0).astype(int)
    df_cleaned['repeat hired'] = pd.to_numeric(df_cleaned['repeat hired'], errors='coerce').fillna(0).astype(int)

    # Clean up the 'cost' column by removing '฿' and ',' and converting to integer
    df_cleaned['cost'] = df_cleaned['cost'].replace({'฿': '', ',': ''}, regex=True).astype(int)

    # Reorder columns to have rating_comment next to Num_comment
    df_cleaned = df_cleaned[['web-scraper-order', 'web-scraper-start-url', 'title', 'rating_comment', 'Num_comment', 'cost', 'link', 'link-href', 'namefreelance', 'percentsuccess', 'num_sold', 'repeat hired', 'time respond']]

    # Calculate the total sum for num_sold and repeat hired
    total_num_sold = df_cleaned['num_sold'].sum()
    total_repeat_hired = df_cleaned['repeat hired'].sum()

    # Count rows where both num_sold and repeat hired are zero
    zero_sold_and_hired_count = df_cleaned[(df_cleaned['num_sold'] == 0) & (df_cleaned['repeat hired'] == 0)].shape[0]

    # Print the total sums and the count of zero rows
    print(f"Total num_sold: {total_num_sold}")
    print(f"Total repeat_hired: {total_repeat_hired}")
    print(f"Rows where both num_sold and repeat hired are zero: {zero_sold_and_hired_count}")

    # Check for any remaining duplicates
    duplicates = df_cleaned[df_cleaned.duplicated(subset=["title", "namefreelance"], keep=False)]

    # If there are any duplicates, print them out
    if not duplicates.empty:
        print("Duplicates found after cleaning:")
        print(duplicates)
    else:
        print("No duplicates found after cleaning.")

    # Save the cleaned data to an Excel file
    try:
        df_cleaned.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Cleaned data has been saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
