# Building AI Systems & Agents This repository contains hands-on labs and builds

## Setup 

1. Create and activate a virtual environment 
2. Install dependencies (added later) 
3. Run scripts in the `scripts/` folder 

## Run ```bash python scripts/hello_ai.py-

##  CLI Assistant
 
Create a `.env` file in the project root:
 
OPENAI_API_KEY=your_key_here
 
Install dependencies:
pip install -r requirements.txt
 
Run:
python scripts/cli_assistant.py

## Document-Aware Assistant (RAG)
 
1) Add `.txt` documents to `data/docs/`
2) Build the index:
python scripts/rag_assistant.py --build-index
 
3) Ask questions:
python scripts/rag_assistant.py