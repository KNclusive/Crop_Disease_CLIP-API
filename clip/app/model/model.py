from PIL import Image
from app.model.similarity_matcher import similarity, embedding_index
from app.model.config import processor, model, top_k, inference_text

index = embedding_index()
model.eval()
processor.tokenizer.clean_up_tokenization_spaces = True

def all_image(payload: str | Image.Image) -> list[str]:
    if isinstance(payload, str):
        input = processor(text=payload, return_tensors="pt", truncation=True, max_length=processor.tokenizer.model_max_length)
        output = model.get_text_features(**input).detach().cpu().numpy()
    elif isinstance(payload, Image.Image):
        input = processor(images=payload, return_tensors="pt", do_convert_rgb=False)
        output = model.get_image_features(**input).detach().cpu().numpy()
    else:
        raise ValueError("Unsupported type")

    return similarity(index, output, top_k)

def image_text(payload: Image.Image) -> str:
    input = processor(images=payload, text=inference_text, return_tensors="pt", padding='longest', truncation=True, 
                        max_length=processor.tokenizer.model_max_length, do_convert_rgb=False)
    logits = model(**input).logits_per_image #logits_per_text
    prediction = logits.softmax(dim=1).argmax(dim=-1)
    return inference_text[prediction.item()] #Convert to scalar