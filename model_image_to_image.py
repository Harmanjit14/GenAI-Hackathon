import PIL
import torch
from diffusers import (EulerAncestralDiscreteScheduler,
                       StableDiffusionInstructPix2PixPipeline)

torch.mps.empty_cache()
model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id)
pipe.to("mps")
# pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

def get_image():
    image = PIL.Image.open("srastika.jpg")
    image = PIL.ImageOps.exif_transpose(image)
    image = image.convert("RGB")
    return image
image = get_image()

prompt = "turn her into cyborg"
images = pipe(prompt, image=image, height=128, width=128).images
images[0].save("srastika-new.jpg")
