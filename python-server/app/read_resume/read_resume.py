import re
import PyPDF2
import docx
import os

class ReadResume:
    def __init__(self, file) -> None:
        self.file = file
        self.file_type = file.filename.split(".")[-1]
        self.extracted_text = ""
        
        temp_filename = 'temp_file' + os.path.splitext(self.file.filename)[1]
        self.file.save(temp_filename)

        if self.file_type == 'txt':
            with open(temp_filename, 'r') as text_file:
                self.extracted_text = text_file.read()
        elif self.file_type == 'pdf':
            self.extracted_text = self.pdf_to_text(temp_filename)
        elif self.file_type == 'docx':
            self.extracted_text = self.docx_to_text(temp_filename)
        else:   
            self.extracted_text = {'error': 'Unsupported file type'}, 400

        os.remove(temp_filename)

    def clean_text(self, text):
        cleaned_text = ' '.join(text.split())
        cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
        cleaned_text = re.sub(r'\s+([.,!?])', r'\1', cleaned_text)
        cleaned_text = re.sub(r'http\S+|www\S+', '', cleaned_text)
        return cleaned_text

    def pdf_to_text(self, pdf_file):
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            all_text = ""

            for page in pdf_reader.pages:
                all_text += page.extract_text()

        return self.clean_text(all_text)
    
    def docx_to_text(self, docx_file):
        doc = docx.Document(docx_file)
        all_text = ""

        for para in doc.paragraphs:
            all_text += para.text + "\n"

        return all_text