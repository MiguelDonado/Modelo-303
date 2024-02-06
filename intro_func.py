import os
import pdfplumber
from support_regex import (
    fecha,
    ejercicio,
    periodo,
    extract_base_cuota_second_page,
    extract_base_cuota_third_page,
)


def get_pdf_files():
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    return pdf_files


def read_pdf(file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return text_file


def extract_data_page(page):
    if "realizada" in page:
        try:
            fecha_field = fecha.search(page).group(1)
            return [fecha_field]
        except AttributeError:
            return None
    elif "exonerado" in page:
        amounts_second_page = extract_base_cuota_second_page(page)
        return amounts_second_page
    elif "localizaci" in page:
        amounts_third_page = extract_base_cuota_third_page(page)
        return amounts_third_page


def extract_data_file(file):
    text_file = read_pdf(file)
    row = []
    rows = []
    for page in text_file:
        if provisional_row := extract_data_page(page):
            row.extend(provisional_row)
        if len(row) == 79:
            rows.append(row)
            row = []
    return rows
