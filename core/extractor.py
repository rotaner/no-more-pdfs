import pdfplumber
import pandas as pd


# Function 1: Extract raw text from a PDF

def extract_raw_text(path):
    # varaiable where every will be contained
    accumulated_raw_text=""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            extracted_raw_text = page.extract_text()
            if extracted_raw_text is None:
                continue
            accumulated_raw_text += f"\n=========\nPage {page.page_number}\n=========\n"
            accumulated_raw_text += extracted_raw_text
    # Return every that has been contained in just one variable
    return accumulated_raw_text


# Function 2: Extract raw tables from a PDF

def extract_raw_tables(path):
    # Empty list ready to contain all the raw tables, because tables are saved as lists
    all_raw_tables = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            extracted_raw_tables = page.extract_tables()
            # A for loop to make the first row of the table the header of the dataframe, and the rest rows as the content
            for table in extracted_raw_tables:
                header = table[0]
                rows = table[1:]
                df = pd.DataFrame(rows,columns=header)
                all_raw_tables.append(df)
    # Return all the tables in one list
    return all_raw_tables


# Function 3: Generate a Excel file (.xlsx) with all the extracted tables in funcion 2

def tables_to_excel(raw_tables_data, excel_path):
    # Define the starting row where the tables should be start written
    current_row = 0
    with pd.ExcelWriter(excel_path) as writer:
        for df in raw_tables_data:
            df.to_excel(writer, startrow = current_row, sheet_name = "df1", index = False)
            current_row += len(df) + 2
