from fastapi import APIRouter, HTTPException
from backend.services.facial_mapping import detect_face_shape
import os

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads/"

@router.get("/analyze/{filename}")
async def analyze_face(filename: str):
    """Analyzes a previously uploaded image by filename and returns face shape."""
    
    # Construct full file path
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    # Perform face shape analysis
    face_shape = detect_face_shape(file_path)
    
    if not face_shape:
        raise HTTPException(status_code=400, detail="No face detected in the image.")
    
    return {"filename": filename, "face_shape": face_shape}
