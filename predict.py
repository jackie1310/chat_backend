from ultralytics import  YOLO
import numpy as np
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

def classify_img(url):
    model = YOLO('best.pt')
    with urlopen(url) as f:
        img = Image.open(BytesIO(f.read()))
    img = np.array(img)
    results = model(img)
    names_dict = results[0].names

    probs = results[0].probs.data.tolist()


    return names_dict[np.argmax(probs)]