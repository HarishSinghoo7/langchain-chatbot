from langchain_openai import ChatOpenAI
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class OpenAIConnector(ProviderHandler):
    """
    Connector class for OpenAI's language model using the langchain_openai library.
    """
    model_name: str = "gpt-4"  # Default model name, can be overridden
    
    def __init__(self):
        super().__init__(client=ChatOpenAI())