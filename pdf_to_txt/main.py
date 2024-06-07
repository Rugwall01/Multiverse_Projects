import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Create or open the text file to write the content
        with open(txt_path, 'w', encoding='utf-8') as text_file:
            # Iterate through each page in the PDF
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)  # Load the page
                text = page.get_text("text")  # Extract text with formatting

                # Write the text to the file
                text_file.write(f"--- Page {page_num + 1} ---\n")
                text_file.write(text)
                text_file.write("\n\n")
        
        print(f"PDF has been successfully converted to {txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_path = 'Austin_Casavant_Resume_2023 Suplemental.pdf'
    # Replace 'output.txt' with the desired output text file path
    txt_path = 'Austins_res_sup.txt'
    pdf_to_text(pdf_path, txt_path)
