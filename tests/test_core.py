import os
from pdf_analyzer import get_pdf_metadata

def test_get_pdf_metadata():
    sample = os.path.join(os.path.dirname(__file__), "sample.pdf")
    data = get_pdf_metadata(sample)
    assert "title" in data
    assert "num_pages" in data
