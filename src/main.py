import pdfplumber
import pandas as pd
import os

path = input("Ingresa la ruta del PDF a leer: ")

all_the_tables = []

with pdfplumber.open(path) as pdf:
    for n_page, page in enumerate(pdf.pages, start=1):
        texto = page.extract_text()
        if texto is None:
            continue
        else:
            print(f"=====\n{n_page}\n=====\n{texto}")
            
        tables = page.extract_tables()
        print(tables)

        for table in tables:
            header = table[0]
            rows = table[1:]
            df = pd.DataFrame(rows, columns=header)
            all_the_tables.append(df)

            print(df)
    
current_row = 0

path_excel_save_file = input("Ingresa la ruta donde se guardará el excel: ")
name_excel_save_file = input("Ingresa el nombre del archivo excel: ")

excel_file = os.path.join(path_excel_save_file,name_excel_save_file)

print(len(all_the_tables))
print(all_the_tables[0])

with pd.ExcelWriter(excel_file) as writer:
    for n_df, df in enumerate(all_the_tables):
            df.to_excel(writer, startrow = current_row, sheet_name="dfs", index=False)
            current_row += len(df) + 2
    