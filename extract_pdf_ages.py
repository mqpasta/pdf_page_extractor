import os
import fitz  # PyMuPDF

# Define input and output folders
input_folder = "../AllInvoices/"  # Folder containing the PDFs
output_folder = "../extracted_invoices"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

total_files = len(os.listdir(input_folder))
counter = 0
print("Total files to process:", total_files)
# Loop through all PDF files in the input folder
for filename in os.listdir(input_folder):
    print("Processing file:", filename)
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        doc = fitz.open(pdf_path)
        
        # Process each page
        for page_num in range(len(doc)):
            new_pdf = fitz.open()  # Create a new empty PDF
            new_pdf.insert_pdf(doc, from_page=page_num, to_page=page_num)
            
            # Output filename: original_name_page_number.pdf
            output_filename = f"{os.path.splitext(filename)[0]}_page_{page_num + 1}.pdf"
            output_path = os.path.join(output_folder, output_filename)
            
            new_pdf.save(output_path)
            new_pdf.close()
        
        doc.close()
        counter += 1
    print("Remaining files:", total_files - counter)


print("PDF pages extracted successfully!")
