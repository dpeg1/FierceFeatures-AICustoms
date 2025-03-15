import os
from fastapi import APIRouter

router = APIRouter()

IMAGE_DIR = "backend/assets/static/images"

@router.get("/list-images")
async def list_images():
    images = [f for f in os.listdir(IMAGE_DIR) if f.endswith((".png", ".jpg", ".jpeg", ".webp"))]
    return {"images": images}
