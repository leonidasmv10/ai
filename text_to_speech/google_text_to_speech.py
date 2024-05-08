from ai.text_to_speech.text_to_speech import TextToSpeech
from gtts import gTTS
import base64
import io

class GoogleTextToSpeech(TextToSpeech):
    def __init__(self):
        super().__init__()
    
    def generate(self, text, language="en"):
        tts = gTTS(text=text, lang=language)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)   
        return base64.b64encode(audio_buffer.getvalue()).decode("utf-8")
    
 