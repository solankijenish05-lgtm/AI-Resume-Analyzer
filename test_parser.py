from app.parsers import extract_pdf_text

text = extract_pdf_text("resume.pdf")

print(text)