from fastapi import APIRouter, HTTPException
import json
import os
from backend.services.facial_mapping import process_image

router = APIRouter()  # ✅ This line initializes the router

UPLOAD_DIR = "backend/uploads"

@router.get("/analyze-face/{filename}")
async def analyze_face(filename: str):
    """
    Runs AI facial mapping on an uploaded image.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found.")

    # Run AI facial mapping
    result = process_image(file_path)

    # Save landmarks to JSON file if successful
    if "landmarks" in result:
        json_path = file_path.replace(".jpg", ".json").replace(".png", ".json")
        with open(json_path, "w") as f:
            json.dump(result["landmarks"], f)

    return result

