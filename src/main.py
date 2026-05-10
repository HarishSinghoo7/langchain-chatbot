from llm_providers import ModelFactory
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def main(model_name: str):
    # Example usage of the ModelFactory to create a model connector
    model_connector = ModelFactory.create_model_connector(model_name)

    if model_connector:
        # Example of using the model connector to generate a response
        prompt = "What is the capital of France?"
        response = model_connector.generate_response(prompt)
        print(f"Response from {model_name}: {response}")
    else:
        print("Failed to create model connector.")


if __name__ == "__main__":
    # Specify the model name you want to use (e.g., "openai", "anthropic", etc.)
    model_name = "openai"  # Change this to the desired model
    main(model_name)