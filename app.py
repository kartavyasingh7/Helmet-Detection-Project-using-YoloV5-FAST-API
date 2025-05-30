from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io

app = FastAPI()


model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\Users\Acer\Desktop\Project\yolov5runs\train\exp6\weights\best.pt', force_reload=True)

@app.post("/detect")
async def detect_helmet(file: UploadFile = File(...)):
   
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

 
    results = model(image)


    detections = results.pandas().xyxy[0].to_dict(orient="records")


    filtered = [det for det in detections if det['confidence'] > 0.4]

    return JSONResponse(content={"detections": filtered})