from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.1.0',
    author='Atharva Bhusari',
    author_email='atharvabhusari99@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)