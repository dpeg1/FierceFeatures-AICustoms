import sqlite3
import os

# Ensure the database directory exists
db_path = "backend/database/fierce_features.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Recreate the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS lash_styles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    image_path TEXT NOT NULL,
    face_shape TEXT NOT NULL
)
""")

# Insert sample data (replace later with real data)
sample_data = [
    ("Test Lash 1", "Basic test lash.", "test/test_1.png", "oval_shape"),
    ("Test Lash 2", "Another test style.", "test/test_2.png", "round_shape")
]

cursor.executemany("INSERT INTO lash_styles (name, description, image_path, face_shape) VALUES (?, ?, ?, ?)", sample_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database recreated & sample data inserted!")
