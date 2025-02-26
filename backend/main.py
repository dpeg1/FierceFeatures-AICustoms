from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import cv2
import io

app = FastAPI()

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # Read the uploaded image
    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    img_np = np.array(img)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    # Load pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img_np, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Convert back to PIL Image
    result_img = Image.fromarray(img_np)
    byte_array = io.BytesIO()
    result_img.save(byte_array, format='JPEG')
    encoded_img = byte_array.getvalue()

    return JSONResponse(content={"message": "Image processed successfully"})

