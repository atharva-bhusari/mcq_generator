import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
        
        except Exception as e:
            raise Exception(f"Error reading the file: {e}")
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("File format not supported")
    

def get_table_data(quiz_str):
    try:
        data_dict = json.loads(quiz_str)
        data = []

        for key,value in data_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
        
            correct = value["correct"]
            data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
