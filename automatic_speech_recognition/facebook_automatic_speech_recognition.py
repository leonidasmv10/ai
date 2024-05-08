from ai.automatic_speech_recognition.automatic_speech_recognition import AutomaticSpeechRecognition
import base64
from transformers import pipeline

class FacebookAutomaticSpeechRecognition(AutomaticSpeechRecognition):
    def __init__(self):
        # self.pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")
        self.pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-xlsr-53-spanish")

    def generate(self, audio_base64):
        audio_binary = base64.b64decode(audio_base64)
        return self.pipe(audio_binary)['text']
