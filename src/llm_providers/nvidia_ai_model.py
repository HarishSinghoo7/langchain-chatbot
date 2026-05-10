from langchain_nvidia_ai_endpoints import ChatNvidiaAIEndpoints
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class NvidiaAIEndpointsConnector(ProviderHandler):
    """
    Connector class for NVIDIA AI Endpoints' language model using the langchain_nvidia_ai_endpoints library.
    """
    model_name: str = "nvidia-1"  # Default model name, can be overridden
    
    def __init__(self):
        super().__init__(client=ChatNvidiaAIEndpoints())