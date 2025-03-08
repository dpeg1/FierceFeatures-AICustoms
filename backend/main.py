kfrom fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import cv2
import numpy as np
from pathlib import Path

app = FastAPI()

# CORS Configuration (Allows frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve Static Files
app.mount("/static", StaticFiles(directory="assets/static"), name="static")

# Enable Caching for Images
@app.get("/static/images/{path:path}")
async def get_image(path: str):
    return FileResponse(
        f"assets/static/images/{path}",
        headers={"Cache-Control": "public, max-age=31536000, immutable"}
    )

# Upload Image API
UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)  # Ensure the uploads directory exists

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    """Handles image uploads"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename, "message": "File uploaded successfully"}

# Facial Detection API
@app.post("/detect-face/")
async def detect_face(file: UploadFile = File(...)):
    """Handles facial detection in an uploaded image"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Load the image for processing
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load OpenCV pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Return face detection results
    face_data = [{"x": x, "y": y, "width": w, "height": h} for (x, y, w, h) in faces]
    return {"faces_detected": len(faces), "face_locations": face_data}

# Root route to check if API is running
@app.get("/")
def read_root():
    return {"message": "Fierce Features AI Customs API is running!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

