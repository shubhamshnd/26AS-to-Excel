import streamlit as st
import pandas as pd
from io import BytesIO
import xlsxwriter

def parse_26as_text_file(file_content):
    normalized_content = file_content.replace('^', '\t')
    lines = normalized_content.split("\n")
    data = []  # List to hold all rows for the dataframe

    # Detect delimiter by checking the first non-empty line

    current_deductor_name = ""  # Variable to hold the deductor's name
    current_deductor_tan = ""  # Variable to hold the deductor's TAN
    
    # Attempt to extract header information, ensuring we don't cause an index error
    if len(lines) > 3:
        header_info_line = lines[3].strip()  # Assuming the 4th line contains the header values
        header_info = header_info_line.split('\t')
        # Adjusting for the actual number of header columns based on the structure
        header_info_adjusted = header_info[:13]  # Adjust to match the number of header columns
    else:
        # Default to empty if the expected header isn't present
        header_info_adjusted = ["N/A"] * 13  # Adjust based on the expected number of header columns

    # Define the header columns based on the user's description
    header_columns = [
        'File Creation Date', 'Permanent Account Number (PAN)', 'Current Status of PAN', 
        'Financial Year', 'Assessment Year', 'Name of Assessee', 
        'Address Line 1', 'Address Line 2', 'Address Line 3', 
        'Address Line 4', 'Address Line 5', 'Statecode', 'Pin Code'
    ]

    # Process each line in the file for transaction and deductor summary
    for line in lines:
        line = line.strip()

        # Skip empty lines and header lines for transaction details
        if not line or ('Sr. No.' in line and 'Section' in line):
            continue

        parts = line.split('\t')

        # Check if this line is a deductor summary line
        if len(parts) > 7 and parts[2] and parts[6] == '':
            current_deductor_name = parts[1]
            current_deductor_tan = parts[2]
        # Check if this line is a transaction detail line
        elif len(parts) > 8 and parts[0].isdigit():
            # Append the current deductor details and transaction details, including header info
            transaction_data = [current_deductor_name, current_deductor_tan] + parts[1:9] + header_info_adjusted
            data.append(transaction_data)

    # Define the dataframe with the correct columns, including the new header info columns
    columns = [
        'Name of Deductor', 'TAN of Deductor', 'Section', 'Transaction Date',
        'Status of Booking', 'Date of Booking', 'Remarks',
        'Amount Paid / Credited(Rs.)', 'Tax Deducted(Rs.)', 'TDS Deposited(Rs.)'
    ] + header_columns
    
    df = pd.DataFrame(data, columns=columns)
    
    return df





def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.book.close()  # Properly close the workbook
    output.seek(0)  # Go to the start of the stream
    return output.getvalue()

# Streamlit application starts here
st.title("26AS Text File Processor")

text_file_26as = st.file_uploader("Upload 26AS File (Text)", type=['txt'])

if text_file_26as:
    # Process the 26AS text file
    file_content = text_file_26as.getvalue().decode("utf-8")
    as26_df = parse_26as_text_file(file_content)

    st.write("Preview of Processed 26AS Data:")
    st.dataframe(as26_df)

    # Provide a download button for the processed Excel file
    st.download_button(
        label="Download Excel",
        data=to_excel(as26_df),
        file_name="26AS_Data.xlsx",
        mime="application/vnd.ms-excel"
    )
