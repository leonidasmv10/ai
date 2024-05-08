from ai.random_video.random_video import RandomVideo
import os
import requests

class PexelsRandomVideo(RandomVideo):
    def __init__(self):
        super().__init__()

    def search(self, query, quantity):
        url = f"https://api.pexels.com/videos/search?query={query}&per_page={quantity}"
        headers = {"Authorization": os.environ.get("PEXEL_API_KEY")}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['videos']
        else:
            print("Error searching for videos:", response.text)
            return None
        
    def get_data(self, video):
        return video['video_files'][0]['link']