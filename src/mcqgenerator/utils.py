import os
import PyPDF2
import json
import traceback
import pandas as pd

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
    

def get_table_data(quiz):
    try:
        quiz_dict = json.loads(quiz)
        quize_table_data=[]

        for key, value in quiz_dict.items():
            mcq=value['mcq']
            option = ", ".join(
                [
                    f"{option}: {option_value}" for option, option_value in value["options"].items()
                ]
            )

            correct = value["correct"]
            quize_table_data.append(
                {
                    "MCQ": mcq,
                    "Options": option,
                    "Correct Option": correct
                }
            )
        return quize_table_data
    except Exception as e:
        traceback.exception(type(e), e, e.__traceback__)
        return False
