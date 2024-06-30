import requests
import os

CAPTION_IMAGES_MODEL = "nlpconnect/vit-gpt2-image-captioning"


def caption_image(filename):
    API_URL = f"https://api-inference.huggingface.co/models/{
        CAPTION_IMAGES_MODEL}"

    headers = {"Authorization": f"Bearer {os.getenv("HUGGING_FACE_TOKEN")}"}

    with open(filename, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers=headers, data=data)

    return list(map(lambda r: r["generated_text"], response.json()))
