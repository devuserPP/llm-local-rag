# Local RAG with Ollama on macOS

### Setup
1. `git clone https://github.com/devuserPP/llm-local-rag`
2. `cd dir`
3. `pip install -r requirements.txt`
4. Install Ollama (https://ollama.com/download)
5. `ollama pull llama3.1` (etc https://ollama.com/library)
6. `ollama pull mxbai-embed-large`
7. `python3 upload.py` (pdf, .txt, JSON)
8. `python3 localrag.py` (with query re-write rephrases the original user query to make it clearer and more specific, while considering the context of the previous conversation)
9. `python3 localrag_no_rewrite.py` (no query re-write)


### What is RAG?
RAG is a way to enhance the capabilities of LLMs by combining their powerful language understanding with targeted retrieval of relevant information from external sources often with using embeddings in vector databases, leading to more accurate, trustworthy, and versatile AI-powered applications

### What is Ollama?
Ollama is an open-source platform that simplifies the process of running powerful LLMs locally on your own machine, giving users more control and flexibility in their AI projects. https://www.ollama.com
