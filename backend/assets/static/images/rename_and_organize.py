import os
import shutil
import re

# Define the base directory where the images are stored
base_dir = "backend/assets/static/images/"
destination_dir = base_dir  # Keep the images in the same structure

# Define regex pattern to extract lash type, length, and curl
pattern = re.compile(r"(\d+mm).*?(J|B|C|D|DD|L|M|U|V) curl", re.IGNORECASE)

# Map lash types to their categories
lash_categories = {
    "Classic": "classic",
    "Volume": "volume",
    "Mega Volume": "mega_volume",
    "Hybrid": "hybrid",
    "Russian Volume": "russian_volume",
    "Extreme Volume": "extreme_volume",
    "Kitten": "kitten",
    "Hawaii Classic": "hawaii_classic",
    "Daphne Volume": "daphne_volume",
}

# Get all files in the directory
for filename in os.listdir(base_dir):
    if filename.startswith("DALL·E") and filename.endswith(".webp"):
        match = pattern.search(filename)
        if match:
            length, curl = match.groups()
            lash_type = None

            # Identify lash type from the filename
            for key in lash_categories:
                if key in filename:
                    lash_type = key
                    break

            if lash_type:
                new_filename = f"{lash_categories[lash_type]}_{length}_{curl}.webp"
                new_category_dir = os.path.join(destination_dir, lash_categories[lash_type])

                # Create category directory if it doesn't exist
                os.makedirs(new_category_dir, exist_ok=True)

                # Move and rename the file
                old_path = os.path.join(base_dir, filename)
                new_path = os.path.join(new_category_dir, new_filename)

                shutil.move(old_path, new_path)
                print(f"Renamed and moved: {old_path} → {new_path}")

print("✅ Renaming and organization completed!")
