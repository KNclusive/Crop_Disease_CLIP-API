import pickle
import numpy as np
from pathlib import Path
from transformers import CLIPProcessor, CLIPModel

current_dir = Path(__file__).parent

top_k = 3
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("TonyStarkD99/CLIP-Crop_Disease-Large")

with open(current_dir.joinpath("data", "unique_classes.pkl"), "rb") as f:
    inference_text = pickle.load(f)
with open(current_dir.joinpath("data", "image_names.txt"), "r") as f:
    image_paths = [line.strip() for line in f]

embeddings = np.load(current_dir.joinpath("data", "inference_set_images_embeddings.npy"))