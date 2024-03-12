# 26AS to Excel Converter

This Streamlit application allows users to upload their Form 26AS text file, exported from the government's website, and converts it into a downloadable Excel file. It provides a simple and user-friendly interface to process the 26AS file without any hassle.

## Instructions

1. **Export Your 26AS Text File**: Log in to the government's tax filing website and download your Form 26AS as a text file.
2. **Upload Your 26AS File**: On the application's interface, use the file uploader to select and upload your 26AS text file.
3. **Download Excel File**: After uploading, the application will process the file and provide a preview of the data. You can then download the data in Excel format using the 'Download Excel' button.

## How to Run

To run this application on your local machine, you'll need to have Python installed. Follow these steps:

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the application files.
3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
Once the dependencies are installed, run the application with the following command:
```bash
streamlit run 26as2xl.py
```
The application will start, and your default web browser will open a new tab pointing to the local server where the application is running (usually http://localhost:8501).

Enjoy converting your 26AS text files to Excel with ease!

To run the application, you'll need a few Python packages, most notably `streamlit`, `pandas`, and `xlsxwriter`. Create a `requirements.txt` file with the following contents to manage these dependencies:

streamlit==1.8.0
pandas==1.3.4
xlsxwriter==1.4.3

These versions are just examples; you might want to use the latest versions of these packages or adjust them based on compatibility and testing. Users will install these dependencies using the command provided in the README instructions.

This setup provides users with everything they need to run your Streamlit application locally, offering a straightforward guide from installation to usage.

