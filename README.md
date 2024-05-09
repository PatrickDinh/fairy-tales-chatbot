# Local Retrieval-Augmented Generation (RAG) chatbot powered by Llama3. 
This is a fairy tales chatbot.

## Prerequisites
- Python 3.12
- Ollama (https://ollama.com/)
- Llama3 (https://ollama.com/library/llama3)
- mxbai-embed-large (https://ollama.com/library/mxbai-embed-large)

## Install dependencies
Run the below command in the project root directory to create a Python virtual environment and install the required dependencies.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Load documents
To load the document into Chrome database, run the below command.

```bash
python load_documents.py
```

## Run the chatbot
To run the chatbot, run the below command.

```bash
streamlit run start_chatbot.py
```

Then open http://localhost:8501 in your web browser to see the chatbot in action.

Happy chatting!