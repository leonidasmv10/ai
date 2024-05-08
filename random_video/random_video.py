from abc import ABC, abstractmethod
class RandomVideo(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def search(self, query, quantity):
        pass

    @abstractmethod
    def get_data(self, video):
        pass