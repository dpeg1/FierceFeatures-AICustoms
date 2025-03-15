import shutil
import os

# Define source and destination directories
source_dir = "/home/danellpegeese6/Downloads/Lashes-GLB/"  # Change this to where the real images are
dest_dir = "/home/danellpegeese6/PycharmProjects/FierceFeatures-AICustoms/backend/assets/static/images/"

# Ensure destination folder exists
os.makedirs(dest_dir, exist_ok=True)

# Move all image files
for file in os.listdir(source_dir):
    if file.endswith((".png", ".jpg", ".jpeg")):  # Only move images
        shutil.copy(os.path.join(source_dir, file), os.path.join(dest_dir, file))

print("✅ Lash images uploaded successfully!")
