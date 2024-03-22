# MCQ Generator

This MCQ (Multiple Choice Question) generator is a tool developed using LangChain and OpenAI. It allows you to automatically generate multiple choice questions based on a given text or PDF file. The generator is built using Python and the Streamlit framework.

## Features

- Automatic generation of multiple choice questions
- Customizable question complexity level (tone)
- Support for PDF and text file inputs
- Ability to specify the number of MCQs to be generated
- Option to download the generated MCQs as a CSV file

## Installation

1. Clone the repository: `git clone https://github.com/your-username/mcq-generator.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your LangChain and OpenAI API credentials in the configuration file (`config.py` or `.env`).

## Usage

1. Provide the input PDF or text file for which you want to generate MCQs.
2. Specify the number of MCQs to be generated and the desired complexity level (tone).
3. Run the generator script: `streamlit run generate.py`
4. The generated MCQs will be displayed on the Streamlit web interface.
5. Optionally, you can download the generated MCQs as a CSV file.

## Configuration

In the `config.py` (or `.env`) file, you can customize various settings such as API credentials, default number of MCQs, and default complexity level.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [LangChain](https://langchain.com)
- [OpenAI](https://openai.com)