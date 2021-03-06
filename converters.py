"""
Module for converting generated data into
different file types.
"""
import pandas as pd


options = {
    0: "Return to Main Menu.",
    1: "Convert CSV to JSON.",
    2: "Convert CSV to Excel.",
}


# Convert CSV to JSON
def json_convert(filepath, filename):

    try:
        df = pd.read_csv(filepath)

        df.to_json(f'data/{filename}.json', orient='records')

    except FileNotFoundError:
        print("ERROR: File not found!")


# Convert CSV to Excel workbook
def excel_convert(filepath, filename):

    try:
        df = pd.read_csv(filepath)

        df.to_excel(f'data/{filename}.xlsx')
    
    except FileNotFoundError:
        print("ERROR: File not found!")


def converter_main():

    try:
        for key, val in options.items():

            print(key, val)

        # Prompt the user to make a choice
        u_choice = int(input("Make a choice based on the above options: "))

        if u_choice == 1:
            file_path = input("Enter the file path of the file you want to convert to a JSON file, without a file extension: ")
            file_name = input("Enter a name for your JSON file: ")
            json_convert(file_path, file_name)
        elif u_choice == 2:
            file_path = input("Enter the file path of the file you want to convert to a Excel file: ")
            file_name = input("Enter a name for your Excel file, without a file extension: ")
            excel_convert(file_path, file_name)
    
    except ValueError:
        
        print("Please enter an integer. Program terminated.")
