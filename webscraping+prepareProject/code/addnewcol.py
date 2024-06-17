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

    '''
Graphic_design
"Marketing_and_advertising
"
"Website_and_technology
"
"Lifestyle
"
Image_and_sound
"Business_and_consulting
"
"Write_and_translate
"
Architecture_and_Engineering
    '''

    # Add a new column filled with "hello"
    data['category_id'] = "Write_and_translate"

    # Save the cleaned data to an Excel file
    try:
        data.to_excel(output_file, index=False, engine='openpyxl')
        print(f"Cleaned data has been saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()

