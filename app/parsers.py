import pdfplumber
from docx import Document

def extract_pdf_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text
def extract_pdf_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text
def extract_docx_text(docx_file):

    doc = Document(docx_file)

    text = ""

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text
def parse_resume(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    else:
        return "Unsupported File Format"