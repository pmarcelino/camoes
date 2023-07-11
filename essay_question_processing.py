import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]
folder_path = './data/processed/'

# Read essay question
def read_txt_file(file_path):
    """
    Reads the content of a text file and returns it as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

# Answer essay question through ChatGPT
def get_completion(prompt, model="gpt-4"):  # "gpt-3.5-turbo"
    """
    Generates a completion response for a given prompt using the OpenAI ChatGPT model.

    Args:
        prompt (str): The prompt text to generate a completion for.
        model (str, optional): The model to use for completion generation. Defaults to "gpt-4".

    Returns:
        str: The generated completion response.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Save essay answer to a text file
def save_answer_to_txt_file(answer_path, response):
    """
    Saves the given response as a string to a text file.

    Args:
        answer_path (str): The path to the output text file.
        response (str): The response string to be saved.

    Returns:
        None
    """
    with open(answer_path, 'w', encoding='utf-8') as file:
        file.write(response)
        print('Answer successful. Saved to', answer_path)

def process_essay_questions_in_folder(folder_path):
    """
    Process files in the specified folder and generate answers for essay questions.

    Args:
        folder_path (str): The path to the folder containing the files.

    Returns:
        None
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith('essay_question.txt'):
            question_path = os.path.join(folder_path, file_name)
            answer_path = os.path.join('./data/artificial/', file_name.replace('_question.txt', '_answer.txt'))
            
            file_content_string = read_txt_file(question_path)
            response = get_completion(file_content_string)
            save_answer_to_txt_file(answer_path, response)

process_essay_questions_in_folder(folder_path)