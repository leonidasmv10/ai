from ai.random_image.random_image import RandomImage
import os
import requests

class UnsplashRandomImage(RandomImage):
    def __init__(self):
        super().__init__()

    def search(self, query, quantity):
        key = os.environ.get("UNSPLASH_API_KEY")
        url = f"https://api.unsplash.com/photos/random/?query={query}&count={quantity}&client_id={key}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error searching for images:", response.text)
            return None
        
    def get_data(self, image):
        return image['urls']['full']
