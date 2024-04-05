from ai.transformer.transformer import Transformer
import os
import google.generativeai as genai

class GeminiTransformer(Transformer):
    def __init__(self):
        super().__init__()

    def configure(self):
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

    def generate_content(self, message):
        self.model = genai.GenerativeModel('gemini-pro')
        response = self.model.generate_content(message)
        return response.text