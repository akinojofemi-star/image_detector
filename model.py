from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import io

# Load pretrained model
processor = AutoImageProcessor.from_pretrained("trpakov/vit-face-expression")
model = AutoModelForImageClassification.from_pretrained("trpakov/vit-face-expression")

def predict_emotion(image_input):
    # Handle Streamlit uploaded file
    if hasattr(image_input, "getvalue"):
        image_bytes = image_input.getvalue()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    else:
        image = Image.open(image_input).convert("RGB")

    # Preprocess image
    inputs = processor(images=[image], return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)[0]
        predicted_class_idx = probabilities.argmax().item()
        confidence = probabilities[predicted_class_idx].item() * 100

    label = model.config.id2label[predicted_class_idx]
    return label, confidence
