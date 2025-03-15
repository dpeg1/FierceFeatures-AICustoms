import os

# Update this path with your actual directory
image_dir = "backend/assets/static/images"

# Check if directory exists
if not os.path.exists(image_dir):
    print(f"Error: Directory {image_dir} not found!")
    exit()

# Dictionary to map original names to new names
rename_mapping = {
    "DALL·E 2025-03-01 16.00.09": "classic_8mm_J.webp",
    "DALL·E 2025-03-01 16.00.20": "classic_10mm_J.webp",
    "DALL·E 2025-03-01 16.04.00": "classic_9mm_C.webp",
    # Add more mappings here
}

for filename in os.listdir(image_dir):
    for original_name, new_name in rename_mapping.items():
        if original_name in filename:
            old_path = os.path.join(image_dir, filename)
            new_path = os.path.join(image_dir, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

print("✅ All files renamed successfully!")
