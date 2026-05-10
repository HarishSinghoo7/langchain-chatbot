from langchain_ollama import ChatOllama
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class OllamaConnector(ProviderHandler):
    """
    Connector class for Ollama's language model using the langchain_ollama library.
    """
    model_name: str = "ollama-2"  # Default model name, can be overridden
    
    def __init__(self):
        super().__init__(client=ChatOllama(model=self.model_name))