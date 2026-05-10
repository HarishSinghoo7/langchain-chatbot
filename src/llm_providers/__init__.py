from dataclasses import dataclass
from typing import Any, Dict, Optional
from model_connectors.open_router_model import OpenRouterConnector
from model_connectors.mistral_ai_model import MistralAIConnector
from model_connectors.openai_model import OpenAIConnector
from model_connectors.anthropic_model import AnthropicConnector
from model_connectors.nvidia_ai_model import NvidiaAIEndpointsConnector
from model_connectors.ollama_model import OllamaConnector

@dataclass
class ModelFactory:
    """
    Factory class to create instances of different model connectors based on the provided model name.
    """

    @staticmethod
    def create_model_connector(model_name: str, **kwargs) -> Optional[Any]:
        """
        Create an instance of a model connector based on the provided model name.

        Args:
            model_name (str): The name of the model connector to create.
            **kwargs: Additional keyword arguments to pass to the connector's constructor.

        Returns:
            An instance of the requested model connector, or None if the model name is not recognized.
        """
        connectors = {
            "open_router": OpenRouterConnector,
            "mistral_ai": MistralAIConnector,
            "openai": OpenAIConnector,
            "anthropic": AnthropicConnector,
            "nvidia_ai": NvidiaAIEndpointsConnector,
            "ollama": OllamaConnector
        }

        connector_class = connectors.get(model_name.lower())
        if connector_class:
            return connector_class(**kwargs)
        else:
            print(f"Model '{model_name}' not recognized. Available models: {list(connectors.keys())}")
            return None
