from swarmauri.llms.concrete.GroqModel import GroqModel

def initialize_llm(api_key):
    llm = GroqModel(api_key=api_key)
    approved_models = [
        "llama-3.3-70b-versatile",
        "llama-3.3-70b-specdec",
        "llama-3.1-70b-specdec",
        "llama-3.2-1b-preview",
        "llama-3.2-3b-preview",
        "llama-3.2-11b-vision-preview",
        "llama-3.2-90b-vision-preview",
    ]
    llm.allowed_models = [model for model in llm.allowed_models if model in approved_models]
    llm.name = llm.allowed_models[0]  # Set the default model
    return llm
