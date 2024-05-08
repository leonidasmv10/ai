from ai.random_image.random_image import RandomImage
import os
import requests

class PexelsRandomImage(RandomImage):
    def __init__(self):
        super().__init__()

    def search(self, query, quantity):
        url = f"https://api.pexels.com/v1/search?query={query}&per_page={quantity}"
        headers = {"Authorization": os.environ.get("PEXEL_API_KEY")}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['photos']
        else:
            print("Error searching for images:", response.text)
            return None
        
    def get_data(self, image):
        return image['src']['original']