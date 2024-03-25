import json
import traceback
from io import StringIO
import pandas as pd
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenrator import generate_and_evaluate_quiz

with open('response.json', 'r') as f:
    RESPONSE_JSON = json.load(f)


st.title("MCQ Generator using LangChain")

if 'mcqs_ready' not in st.session_state:
    st.session_state['mcqs_ready'] = False
if 'mcqs_data' not in st.session_state:
    st.session_state['mcqs_data'] = []


with st.form("user_inputs"):
    upload_file = st.file_uploader("Upload a file pdf or text", type=["pdf", "txt"])

    mcq_count = st.number_input("Number of MCQs to generate", min_value=3, max_value=50)

    subject = st.text_input("Input the subject of the text", max_chars=50)

    tone = st.text_input("Complexity of the MCQs", max_chars=20, placeholder="Simple")

    button = st.form_submit_button("Generate MCQs")

    if button and upload_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text = read_file(upload_file)
                with get_openai_callback() as cb:
                    response = generate_and_evaluate_quiz(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("An error occurred while generating MCQs")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    quiz = response.get("quiz", None)
                    st.session_state['mcqs_ready'] = True
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        st.session_state['mcqs_data'] = table_data
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)

                            st.text_area(label="Review", value=response['review'])
                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)


if st.session_state.mcqs_ready:
    # Convert stored MCQ data to CSV
    df = pd.DataFrame(st.session_state.mcqs_data)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_string = csv_buffer.getvalue()
    
    # Display download button
    st.download_button(
        label="Download MCQs as CSV",
        data=csv_string,
        file_name="mcqs.csv",
        mime='text/csv',
    )