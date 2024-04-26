import os
import google.generativeai as genai
import openai

from enum import Enum

class AiType(Enum):
    GEMINI = 1,
    OPENAI = 2,
    ME = 3

class AIConnection:
    _instance = None
    _map_ai = {
        AiType.GEMINI: 0,
        AiType.OPENAI: 0,
        AiType.ME: 0
    }

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def configuration(self, ai_type):
        AIConnection._map_ai[ai_type] += 1 
        if AIConnection._map_ai[ai_type] > 0:
            if ai_type == AiType.GEMINI:
                genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
            elif ai_type == AiType.OPENAI:
                openai.api_key=os.environ.get("OPENAI_API_KEY")
            elif ai_type == AiType.ME:
                pass
       
    def show_conections(self):
        for clave, valor in AIConnection._map_ai.items():
            print(clave, valor)
