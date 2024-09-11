import io
from PIL import Image
from fastapi import FastAPI, UploadFile, File
from app.model.model import all_image, image_text

app = FastAPI()

@app.get("/")
def home():
    return {"Health check": "OK.",
            "API Info": "This API is developed by D for inferencing on Crop-diseases from  FT'd -CLIP.",
            "CLIP INFO": "More information can be found here HERE"}

@app.post("/textreturnsImg")
def predict_image(payload: str):
    return {"image": all_image(payload)}

@app.post("/ImgreturnsImg")
def predict_image(payload: UploadFile = File(...)):
    contents = payload.file.read()
    image = Image.open(io.BytesIO(contents))
    return {"image": all_image(image)}

@app.post("/ImgreturnsText")
async def predict_text(payload: UploadFile = File(...)):
    contents = await payload.read()
    image = Image.open(io.BytesIO(contents))
    return {"text": image_text(image)}