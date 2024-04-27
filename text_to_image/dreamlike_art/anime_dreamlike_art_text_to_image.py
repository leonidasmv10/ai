from ai.text_to_image.dreamlike_art.dreamlike_art_text_to_image import DreamlikeArtTextToImage
from diffusers import StableDiffusionPipeline
import torch

class AnimeDreamlikeArtTextToImage(DreamlikeArtTextToImage):
    def __init__(self):
        super().__init__()
        self.model_id = "dreamlike-art/dreamlike-anime-1.0"
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, use_safetensors=True)
        self.pipe = self.pipe.to("cuda")
    
    def generate(self, prompt, params = {}):
        return self.generate_image(self.pipe, prompt, params)
    
 