from ai.translate.translate import *
from transformers import pipeline

class HelsinkiTranslate(Translate):
    def __init__(self, language_type):
        super().__init__(language_type)
        self.pipe = self.set_language(self.language_type)

    def set_language(self, language_type):
        pipe = None
        if language_type == LanguageType.SPANISH_TO_ENGLISH:
            pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
        elif language_type == LanguageType.ENGLISH_TO_SPANISH:
            pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
        return pipe

    def translation(self, message):
        result = self.pipe(message)
        return result[0]['translation_text']
    
    