from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()

# Serve Static Files with Caching Enabled
app.mount(
    "/static",
    StaticFiles(directory="assets/static"),
    name="static"
)

# Enable Caching for Images
@app.get("/static/images/{path:path}")
async def get_image(path: str):
    return FileResponse(
        f"assets/static/images/{path}",
        headers={"Cache-Control": "public, max-age=31536000, immutable"}
    )
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Serve Static Files
app.mount("/static", StaticFiles(directory="assets/static"), name="static")

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
