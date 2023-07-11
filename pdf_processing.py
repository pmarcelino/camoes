import os
import PyPDF2

def convert_pdf_files_to_text(raw_path):
    """
    Converts PDF files to text for files that match the target keyword in the specified folder.

    Args:
        raw_path (str): The path to the folder containing the PDF files.

    Returns:
        None
    """
    target_keyword = 'exam'

    for file_name in os.listdir(raw_path):
        if target_keyword in file_name.lower() and file_name.endswith('.pdf'):
            pdf_path = os.path.join(raw_path, file_name)
            txt_path = os.path.join(processed_path, file_name.replace('.pdf', '.txt'))
            with open(pdf_path, 'rb') as pdf_file, open(txt_path, 'w', encoding='utf-8') as txt_file:
                reader = PyPDF2.PdfReader(pdf_file)
                num_pages = len(reader.pages)

                text_content = ""
                for page_number in range(num_pages):
                    page = reader.pages[page_number]
                    text_content += page.extract_text()

                txt_file.write(text_content)
                print('Conversion successful. Saved to', txt_path)
            
def extract_text_between_keywords_in_files(processed_path):
    """
    Extracts text between keywords for files that match the target keyword in the specified folder.

    Args:
        processed_path (str): The path to the folder containing the text files.

    Returns:
        None
    """
    start_keyword = 'GRUPO III'
    end_keyword = 'FIM'
    target_keyword = 'exam'
    
    for file_name in os.listdir(processed_path):
        if target_keyword in file_name.lower() and file_name.endswith('.txt'):
            input_file = os.path.join(processed_path, file_name)
            output_file = os.path.join(processed_path, file_name.replace('.txt', '_essay_question.txt'))

            with open(input_file, 'r', encoding='utf-8') as input_txt, open(output_file, 'w', encoding='utf-8') as output_txt:
                content = input_txt.read()
                start_index = content.find(start_keyword)
                end_index = content.find(end_keyword)

                if start_index != -1 and end_index != -1:
                    extracted_text = content[start_index + len(start_keyword):end_index].strip()
                    output_txt.write(extracted_text)
                    print('Extraction successful. Saved to', output_file)
                else:
                    print('Start or end keyword not found in the input file.')

raw_path = './data/raw/'
processed_path = './data/processed/'

convert_pdf_files_to_text(raw_path)
extract_text_between_keywords_in_files(processed_path)