from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.upload import router as upload_router
from backend.routes.analyze import router as analyze_router
from backend.routes.recommendations import router as recommendations_router

app = FastAPI(
    title="Fierce Features AI Customs",
    description="AI-powered lash & brow mapping API",
    version="1.0.0"
)

# Include API routes
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
app.include_router(recommendations_router, prefix="/recommend", tags=["Recommendations"])

# Enable CORS to prevent frontend request issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; adjust for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from backend/assets/static/
app.mount("/static", StaticFiles(directory="backend/assets/static"), name="static")

@app.get("/")
async def root():
    return {"message": "Welcome to Fierce Features AI Customs API!"}

# Debugging route to list available images
import os

@app.get("/list-images")
async def list_images():
    images_dir = "backend/assets/static/images"
    if os.path.exists(images_dir):
        return {"images": os.listdir(images_dir)}
    return {"error": "Images directory not found"}

