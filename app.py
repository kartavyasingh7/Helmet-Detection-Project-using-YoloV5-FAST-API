from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io
import pandas as pd

app = FastAPI()

# Load YOLOv5 model (using pretrained COCO model for demo)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.post("/detect")
async def detect_helmet(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Run inference
    results = model(image)

    # Extract detections as list of dicts
    detections = results.pandas().xyxy[0].to_dict(orient="records")

    return JSONResponse(content={"detections": detections})