import sys
import os
import pandas as pd

def main():
    # Check if the user has provided the input file
    if len(sys.argv) < 2:
        print("Usage: python3 cleaning_with_stats.py <input_file.xlsm>")
        return

    input_file = sys.argv[1]

    # Load the input file
    try:
        data = pd.read_excel(input_file, engine='openpyxl')
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # implement here:

if __name__ == "__main__":
    main()
