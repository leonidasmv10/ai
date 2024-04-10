from enum import Enum

class LanguageType(Enum):
    ALL = 0,
    SPANISH_TO_ENGLISH = 1,
    ENGLISH_TO_SPANISH = 2

class Translate():
    def __init__(self, language_type):
        self.language_type = language_type
        self.model = None

    def set_language(self, language_type):
        pass
        
    def translation(self, message):
        return ""
