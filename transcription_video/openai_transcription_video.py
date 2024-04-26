from ai.transcription_video.transcription_video import TranscriptionVideo
from ai.ai_connection import AiType, AIConnection
import os
class OpenaiTranscriptionVideo(TranscriptionVideo):
    def __init__(self):
        AIConnection().configuration(AiType.OPENAI)

    def transcription(self, audio_file):
        import openai
        with open(audio_file, 'rb') as audio:
            print("Comenzando la transcripción...")
            transcription = openai.audio.transcriptions.create(model="whisper-1", file=audio)
            print("Hecho!!!")

            nombre, extension = os.path.splitext(audio_file)
            transcription_nombre = f"transcription_{nombre}.txt"
            with open(transcription_nombre, "w") as file:
                file.write(transcription.text)

            return transcription_nombre