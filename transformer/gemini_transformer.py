from ai.transformer.transformer import Transformer
from ai.ai_connection import AiType, AIConnection
import google.generativeai as genai

class GeminiTransformer(Transformer):
    def __init__(self):
        super().__init__()
        AIConnection().configuration(AiType.GEMINI)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_content(self, message):
        response = self.model.generate_content(message)
        return response.text