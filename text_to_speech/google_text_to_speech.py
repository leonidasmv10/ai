from ai.text_to_speech.text_to_speech import TextToSpeech
from gtts import gTTS

class GoogleTextToSpeech(TextToSpeech):
    def __init__(self):
        super().__init__()
    
    def generate(self, text, out_path, language="en"):
        tts = gTTS(text=text, lang=language)
        tts.save(out_path)
        print("Downloaded!")
    
 