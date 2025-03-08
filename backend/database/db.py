import sqlite3

DB_PATH = "backend/database/styles.db"

def create_tables():
    """Initialize the database and create tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lash_styles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            face_shape TEXT NOT NULL,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()

def get_recommended_styles(face_shape: str):
    """Fetch recommended lash styles based on detected face shape."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name, description FROM lash_styles WHERE face_shape = ?", (face_shape,))
    styles = cursor.fetchall()

    conn.close()

    return [{"name": row[0], "description": row[1]} for row in styles]

# Initialize tables when the script runs
create_tables()
