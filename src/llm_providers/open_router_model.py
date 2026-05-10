from langchain_openrouter import OpenRouter
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class OpenRouterConnector(ProviderHandler):
    """
    Connector class for OpenRouter's language model using the langchain_openrouter library.
    """
    model_name: str = "openrouter-1"  # Default model name, can be overridden
    
    def __init__(self):
        super().__init__(client=OpenRouter())