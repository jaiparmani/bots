from llmconfig.GeminiConfig import GeminiModel


class LLMModel:
    def __init__(self):
        self.model = GeminiModel()  
    def generate(self, prompt: str) -> str:
        return self.model.generate(prompt)