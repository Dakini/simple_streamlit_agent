# AI Hero - Documentation Assistant

An AI-powered search agent that answers questions about documentation using intelligent chunking, vector embeddings

## Overview

This application ingests documentation data and creates a searchable knowledge base using both keyword and semantic search. The AI agent uses these indexes to find relevant information and provide accurate, context-aware answers to user questions.

## Installation

**Requirements:** Python 3.13+

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables (create `.env` file):
```
OPENAI_API_KEY=your_key_here
```

3. Prepare data: Place your documentation CSV file as `intelligent_chunking.csv` with columns: `filename`, `section`

## Usage

**CLI Mode:**
```bash
python main.py
```

**Web Interface (Streamlit):**
```bash
streamlit run app.py
```

Then ask questions about your documentation. The agent will search through indexed content and provide answers with source information.

## Features

- **Dual Indexing**: Combines keyword search (BM25) and vector search (embeddings)
- **Intelligent Chunking**: Works with pre-chunked documentation for better context
- **Streaming Responses**: Real-time AI-generated answers in the Streamlit UI
- **Interaction Logging**: Automatically logs all Q&A interactions for analysis
- **Multi-interface**: Use via CLI or interactive web dashboard

## Architecture

- `ingest.py` - Data loading and index creation
- `search_agent.py` - AI agent initialization 
- `search_tools.py` - Search tool implementation
- `app.py` - Streamlit web interface
- `main.py` - CLI interface
- `logs.py` - Interaction logging

## Testing

Run the CLI interface to test the agent:
```bash
python main.py
```

Type "stop" to exit. Check `logs/` directory for interaction history.

## License

MIT
