from ai.text_to_image.text_to_image import TextToImage

class DreamlikeArtTextToImage(TextToImage):
    def __init__(self):
        super().__init__()

    def generate_image(self, pipe, prompt, params):
        imgs = pipe(prompt, **params).images
        num_images = len(imgs)
        for i in range(num_images):
            self.add_image(imgs[i])

        return self.get_images()
