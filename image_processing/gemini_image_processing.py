from ai.image_processing.image_processing import ImageProcessing
from ai.ai_connection import AiType, AIConnection
import google.generativeai as genai

class GeminiImageProcessing(ImageProcessing):
    def __init__(self):
        super().__init__()
        AIConnection().configuration(AiType.GEMINI)
        self.model = genai.GenerativeModel('gemini-pro-vision')
        # self.chat = self.model.start_chat(history=[])
    
    def send_message(self, message, image):
        response = self.model.generate_content([message, image])
        return response.text
    
    def get_history(self):
        return self.chat.history;
    
 