from pypdf import PdfReader, PdfWriter

# Extract pages from a PDF and then return it into a one file.
def extract_pdf_pages(origin_path, selected_pages, destination_path):

    # Create a empty list for pages not found
    pages_not_found = []


    # Open, analyze and extract data form the PDF
    reader = PdfReader(origin_path)
    # Create, write, modify and save things in a PDF format
    writer = PdfWriter()
    for given_page in selected_pages:
        # Substract one from the given page to get the actual value
        index_page = given_page - 1
        try:
            extracted_page = reader.pages[index_page]
        except IndexError:
            pages_not_found.append(given_page)
            continue
        writer.add_page(extracted_page)
    with open(destination_path, "wb") as output_file:
        writer.write(output_file)

    # Return the list with the pages that weren't found
    return pages_not_found