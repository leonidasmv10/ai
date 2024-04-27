from ai.automatic_speech_recognition.automatic_speech_recognition import AutomaticSpeechRecognition
import soundfile as sf
from transformers import pipeline

class FacebookAutomaticSpeechRecognition(AutomaticSpeechRecognition):
    def __init__(self):
        # self.pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")
        self.pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-xlsr-53-spanish")

    def generate(self, path_audio):
        audio_input, _ = sf.read(path_audio)
        return self.pipe(audio_input)['text']
