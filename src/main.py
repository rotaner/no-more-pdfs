import pdfplumber

path = input("Ingresa la ruta del pdf a leer: ")

with pdfplumber.open(path) as pdf:
    for n_page, page in enumerate(pdf.pages, start=1):
        texto = page.extract_text()
        if texto is None:
            continue
        else:
            print(f"=====\n{n_page}\n=====\n{texto}")
            
        