
import PIL
import torch
from diffusers import DiffusionPipeline
from PIL import Image

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("mps")

prompt = "A rude guy who is abusive most of the time and is smart way beyond universe"

# run both experts
image = pipe(prompt=prompt).images[0]
image.save('new_img.png')