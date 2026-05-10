# Langchain ChatBot

A conversational AI chatbot built with **Langchain** and **Streamlit**, supporting multiple LLM providers and equipped with tool access capabilities.

## Features

- 🤖 **Multi-Provider LLM Support**
  - Ollama (Local Models)
  - OpenAI
  - Anthropic
  - Mistral AI
  - NVIDIA

- 💬 **Conversational Interface**
  - Built with Streamlit for interactive UI
  - Real-time chat interactions
  - Conversation history management

- 🛠️ **Tool Integration**
  - Access to external tools and functions
  - Chainable operations with Langchain
  - Enhanced contextual responses

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Langchain-ChatBot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

Configure your API keys and preferences in `.env` file.

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The chatbot will open in your default browser at `http://localhost:8501`

## Configuration

### LLM Provider Selection

Configure your preferred LLM provider in the Streamlit interface or `.env` file:

- **Ollama**: Requires local Ollama installation
- **OpenAI**: Requires `OPENAI_API_KEY`
- **Anthropic**: Requires `ANTHROPIC_API_KEY`
- **Mistral AI**: Requires `MISTRAL_API_KEY`
- **NVIDIA**: Requires NVIDIA API credentials

### Available Tools

The chatbot has access to various tools for enhanced functionality:
- Web search
- Code execution
- Data processing
- And more...

## Requirements

- Python 3.8+
- Streamlit
- Langchain
- API keys for selected providers (where applicable)

## Project Structure

```
Langchain-ChatBot/
├── app.py              # Main Streamlit application
├── ui/                 # Streamlit application ui
├── apis/               # FastAPI apis
├── config.py           # Configuration settings
├── llm_providers/      # LLM provider integrations
├── tools/              # Tool implementations
├── utils/              # Utility functions
├── prompt_templates/    # Prompt templates
└── requirements.txt    # Project dependencies
```

## License

MIT License - See LICENSE file for details
