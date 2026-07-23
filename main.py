import os
from core.extractor import extract_raw_text, extract_raw_tables, tables_to_excel


if __name__ == "__main__":

    # Funcion 1 and 2 input
    path = input("Enter the PDF path: ")

    # Save the info of the accumulated tables in a variable that can be used outside the local scope of the funcion 2
    raw_tables_data = extract_raw_tables(path)

    # Call function 1
    print(extract_raw_text(path))
    # Call function 2
    print(raw_tables_data)

    # Funcion 3

    # Define the path and the file name
    excel_file_path = input("Enter the path where the Excel will be saved: ")
    excel_file_name = input("Enter the Excel file name (add .xlsx): ")

    # Merge the path and the file name to make the excel save path
    excel_path = os.path.join(excel_file_path,excel_file_name)

    # Execute function 3
    tables_to_excel(raw_tables_data,excel_path)
