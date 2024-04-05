from ai.vision_transformer.vision_transformer import VisionTransformer
import os
import google.generativeai as genai

class GeminiVisionTransformer(VisionTransformer):
    def __init__(self):
        super().__init__()

    def configure(self):
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

    def generate_content(self, image):
        self.model = genai.GenerativeModel('gemini-pro-vision')
        response = self.model.generate_content(image)
        return response.text