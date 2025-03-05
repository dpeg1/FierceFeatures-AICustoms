from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS Configuration
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

# Function to Get Image Paths Dynamically
def get_image_paths():
    base_dir = "assets/static/images"
    image_paths = {}
    for category in os.listdir(base_dir):
        category_dir = os.path.join(base_dir, category)
        if os.path.isdir(category_dir):
            image_paths[category] = []
            for image in sorted(os.listdir(category_dir)):
                image_paths[category].append(f"images/{category}/{image}")
    return image_paths

@app.get("/get-lash-images/")
async def get_lash_images():
    image_paths = get_image_paths()
    return JSONResponse(content=image_paths)

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
