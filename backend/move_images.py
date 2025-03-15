import shutil
import os

# Corrected Source Folder (check this path!)
source_folder = "/home/danellpegeese6/Downloads/LASHES_GLB/"  # Change this!

# Correct Destination Folder
destination_folder = "/home/danellpegeese6/PycharmProjects/FierceFeatures-AICustoms/backend/assets/static/images/"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Move all image files
for file in os.listdir(source_folder):
    if file.endswith((".png", ".jpg", ".jpeg")):
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))

print("✅ Images moved successfully!")
