import fitz

def convert_to_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        text=""
        for page in doc:
            text +=page.get_text()
    return text
