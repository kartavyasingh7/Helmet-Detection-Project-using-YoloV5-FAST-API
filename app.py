from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
model = None  
origins = [
    "http://localhost:3000",  
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


@app.on_event("startup")
def load_model():
    global model
    model = torch.hub.load(
    'ultralytics/yolov5', 
    'custom', 
    path='C:/Users/Acer/Desktop/Project/yolov5/runs/train/exp6/weights/best.pt', 
    force_reload=True
)
@app.post("/detect")
async def detect_helmet(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        results = model(image)
        detections = results.pandas().xyxy[0].to_dict(orient="records")
        filtered = [det for det in detections if det['confidence'] > 0.4]
        return JSONResponse(content={"detections": filtered})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

