class TextToSpeech():
    def __init__(self):
        self.__audios = []
        self.__num_audios = 0

    def add_audio(self, audio):
        self.__audios.append(audio)
        self.__num_audios = self.__num_audios + 1

    def get_audios(self):
        return self.__audios
    
    def get_audio(self, index):
        return self.__audios[index]

    def get_num_audios(self):
        return self.__num_audios
