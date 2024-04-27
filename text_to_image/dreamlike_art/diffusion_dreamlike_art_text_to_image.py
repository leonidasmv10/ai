from ai.text_to_image.dreamlike_art.dreamlike_art_text_to_image import DreamlikeArtTextToImage
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch

class DiffusionDreamlikeArtTextToImage(DreamlikeArtTextToImage):
    def __init__(self):
        super().__init__()
        self.model_id = "dreamlike-art/dreamlike-diffusion-1.0"
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, use_safetensors=True)
        self.pipe = self.pipe.to("cuda")
    
    def generate(self, prompt):
        return self.pipe(prompt).images[0]