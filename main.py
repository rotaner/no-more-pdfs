import os
from core.extractor import extract_raw_text, extract_raw_tables, tables_to_excel
from core.manipulator import extract_pdf_pages
from core.utils import string_to_pagelist_convertor


if __name__ == "__main__":

    # Menu setup

    while True:

        print("""
======================
Welcome to No More PDF
======================

What do we will do today?

Choose from the following tools (pick a number):
    1. Extract raw text
    2. Extract raw tables
    3. Turn raw tables into an Excel file
    4. Split a PDF
    5. Close the program
        """)

        chosen_tool = input("Enter your selection: ")

        # 1. Extract raw text
        if chosen_tool == "1":
            print("Extracting raw text...")

            path = input("Enter the PDF path: ")
            print(extract_raw_text(path))

        # 2. Extract raw tables
        elif chosen_tool == "2":
            print("Extracting raw tables...")
            
            path = input("Enter the PDF path: ")
            # Save the info of accumulated tables in a variable that can be used outside the local scope of the funcion 2
            raw_tables_data = extract_raw_tables(path)
            print(raw_tables_data)

        # 3. Turn raw tables (Function 2) into an Excel file
        elif chosen_tool == "3":
            print("Turning raw tables into a Excel file...")

            path = input("Enter the PDF path: ")
            # Save the info of the accumulated tables in a variable that can be used outside the local scope of the funcion 2
            raw_tables_data = extract_raw_tables(path)
                        
            # Define the path and the file name
            excel_file_path = input("Enter the path where the Excel will be saved: ")
            excel_file_name = input("Enter the Excel file name (add .xlsx): ")

            # Merge the path and the file name to make the excel save path
            excel_path = os.path.join(excel_file_path,excel_file_name)

            # Execute function 3
            tables_to_excel(raw_tables_data,excel_path)

        # 4. Split a PDF, enter a set of pages you would like to extract from the PDF.
        elif chosen_tool == "4":
            print("Spliting PDF...")

            # Provide the path of the pdf and its final destination
            origin_path = input("Enter the PDF path: ")
            destination_path = input("Enter the destination path: ")

            # Give the pages you want to extract
            wanted_pages = input("Select the pages you would like to extract: ")

            # Execute utils function to make the clean list
            # try:
            selected_pages = string_to_pagelist_convertor(wanted_pages)
            # except ValueError as error:
                # print(error)
                # continue
            # Execute de function 4, spliting the PDF
            pdf_elements = extract_pdf_pages(origin_path, selected_pages, destination_path)

            print(f"\nThe PDF was successfully created\n")

            # Exception
            # Returns the not foundt pages the user entered
            if pdf_elements:
                # Print all the not found pages in a suitable list
                not_found_pages = ", ".join([str(page) for page in pdf_elements])
                print(f"The following pages weren't found: {not_found_pages}")
            
        # 5. Close the program
        elif chosen_tool == "5":
            break
        
        else:
            print("Enter a valid option")
    print("Program closed")