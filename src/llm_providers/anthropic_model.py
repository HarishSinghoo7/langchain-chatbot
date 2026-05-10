from langchain_anthropic import ChatAnthropic
from dataclasses import dataclass
from llm_providers.provider_handler import ProviderHandler

@dataclass
class AnthropicConnector(ProviderHandler):
    """
    Connector class for Anthropic's language model using the langchain_anthropic library.
    """
    model_name: str = "claude-2"  # Default model name, can be overridden

    def __init__(self):
        super().__init__(client=ChatAnthropic(model=self.model_name))