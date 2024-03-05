from PyPDF2 import PdfReader

def process_files(files):

    text = ""

    for file in files:
        pdf = PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()
    
    return text


