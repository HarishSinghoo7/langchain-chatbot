from dataclasses import dataclass
from typing import Any

@dataclass
class ProviderHandler:
    """
    Handler class to manage interactions with different language model connectors.
    """
    client: Any

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the model connector based on the provided prompt.

        Args:
            prompt (str): The input prompt to send to the model.

        Returns:
            str: The generated response from the model.
        """
        response = self.client.invoke(prompt)
        return response.content