from langchain_mistralai import ChatMistralAI
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class MistralAIConnector(ProviderHandler):
    """
    Connector class for Mistral AI's language model using the langchain_mistralai library.
    """
    model_name: str = "mistral-1"  # Default model name, can be overridden
    
    def __init__(self):
        super().__init__(client=ChatMistralAI())