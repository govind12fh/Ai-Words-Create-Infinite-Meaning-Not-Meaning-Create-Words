 import torch
import clip
from PIL import Image

model, preprocess = clip.load("ViT-B/32")

def analyze_image(image_path, text_prompt):
    image = preprocess(Image.open(image_path)).unsqueeze(0)
    text = clip.tokenize([text_prompt])
    with torch.no_grad():
        logits_per_image, logits_per_text = model(image, text)
        similarity = logits_per_image.softmax(dim=-1)
    return similarity

if __name__ == "__main__":
    print(analyze_image("example.jpg", "A spiritual guru meditating"))
    src/multimodal_ai.py
