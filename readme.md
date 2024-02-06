# Model 303 Data Extraction

This project is designed to extract specific information related to the Model 303 tax in Spain from PDF files. The extracted data is then written to an Excel file for further analysis.

## Project Structure

The project consists of several Python files and a CSV file:

- `definitive.py`: This is the main script that orchestrates the data extraction process.
- `intro_func.py`: This file contains various functions for reading PDF files and extracting data from them.
- `output.py`: This file contains functions for writing the extracted data to an Excel file.
- `support_regex.py`: This file contains regular expressions used for data extraction.
- `cabeceras.csv`: This CSV file contains the headers used in the output Excel file.

## How It Works

1. The `get_pdf_files` function in `intro_func.py` retrieves all PDF files in the current directory.
2. For each PDF file, the `extract_data_file` function reads the PDF and extracts the data from each page using the `extract_data_page` function.
3. The `extract_data_page` function uses various regular expressions from `support_regex.py` to match and extract the desired data.
4. The extracted data for each file is collected into a list of lists, where each inner list represents the data for one month.
5. The `write_to_xlsx` function in `output.py` writes the extracted data to an Excel file named "MODELO 303.xlsx". The headers for the Excel file are retrieved from the `cabeceras.csv` file using the `get_cabeceras` function.

## Usage

To run the project, execute the `definitive.py` script. Make sure that all the PDF files you want to extract data from are in the same directory as the script.
```sh
python definitive.py
```
After running the script, you will find the extracted data in the "MODELO 303.xlsx" file.

## Requirements

This project requires the following Python libraries:

- `os`
- `pdfplumber`
- `openpyxl`
- `csv`