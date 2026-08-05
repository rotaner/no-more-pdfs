from pypdf import PdfReader, PdfWriter

def extract_pdf_pages(origin_path, selected_pages, destination_path):
    reader = PdfReader(origin_path)
    writer = PdfWriter()
    for given_page in selected_pages:
        index_page = given_page - 1
        extracted_page = reader.pages[index_page]
        writer.add_page(extracted_page)
    with open(destination_path, "wb") as output_file:
        writer.write(output_file)
