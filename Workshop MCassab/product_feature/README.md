# Product Categorization Project

This project aims to categorize products based on their descriptions using LLMs. It leverages the Pydantic library for data validation along with the LangChain and OpenAI's GPT models for processing and categorizing product descriptions.

## Environment Setup

Set up a virtual environment and install the required dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Configuration

Create a .env file in the project root directory with the following content:
> OPENAI_API_KEY="your_openai_api_key_here"

## Running the Notebook
The main logic of the product categorization is contained within the categorize.ipynb Jupyter notebook.

## Project Structure
- .env: Contains environment variables.
- categorize.ipynb: Jupyter notebook with the categorization logic.
- examples.csv: CSV file with example product descriptions for categorization.
- EXEMPLO PADRONIZAÇÃO DESCRITIVO CERVEJAS.xlsx: Example dataset (not directly used in the notebook).
- product_model.py: Defines the Pydantic model for product data.
- requirements.txt: Lists the Python package dependencies for the project.