class TextToImage():
    def __init__(self):
        self.__images = []
        self.__num_images = 0

    def add_image(self, image):
        self.__images.append(image)
        self.__num_images = self.__num_images + 1

    def get_images(self):
        return self.__images
    
    def get_image(self, index):
        return self.__images[index]

    def get_num_images(self):
        return self.__num_images
