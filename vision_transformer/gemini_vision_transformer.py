from ai.vision_transformer.vision_transformer import VisionTransformer
from ai.ai_connection import AiType, AIConnection
import google.generativeai as genai

class GeminiVisionTransformer(VisionTransformer):
    def __init__(self):
        super().__init__()
        AIConnection().configuration(AiType.GEMINI)
        self.model = genai.GenerativeModel('gemini-pro-vision')

    def generate_content(self, image):
        response = self.model.generate_content(image)
        return response.text