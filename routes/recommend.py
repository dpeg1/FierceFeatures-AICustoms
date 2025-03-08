import json
import os
from fastapi import APIRouter, HTTPException
from backend.services.recommendations import recommend_lash_styles, classify_face_shape

router = APIRouter()
UPLOAD_DIR = "backend/uploads"

@router.get("/recommend/{filename}")
async def get_recommendation(filename: str):
    """
    Load facial landmarks and return lash style recommendations.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Ensure the file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found.")

    # Check if landmarks JSON exists
    landmarks_path = file_path.replace(".jpg", ".json").replace(".png", ".json")
    if not os.path.exists(landmarks_path):
        raise HTTPException(status_code=500, detail="Facial landmarks not found.")

    # Load landmarks
    try:
        with open(landmarks_path, "r") as f:
            landmarks = json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding landmarks JSON.")

    # Get recommendations
    try:
        face_shape = classify_face_shape(landmarks)
        recommendations = recommend_lash_styles(landmarks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing recommendations: {str(e)}")

    return {"face_shape": face_shape, "recommendations": recommendations}

