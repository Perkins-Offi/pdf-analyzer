from PyPDF2 import PdfReader
import os

def get_pdf_metadata(filepath):
    reader = PdfReader(filepath)
    info = reader.metadata
    return {
        "title": info.title,
        "author": info.author,
        "producer": info.producer,
        "num_pages": len(reader.pages),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2)
    }
