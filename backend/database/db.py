import sqlite3

DB_PATH = "backend/database/lash_styles.db"  # Adjust if needed

def get_recommended_styles(face_shape: str):
    """
    Fetch recommended lash styles based on the detected face shape.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name, description, image_path FROM lash_styles WHERE face_shape = ?", (face_shape,))
        rows = cursor.fetchall()

        recommendations = [
            {
                "name": row[0],
                "description": row[1],
                "image_url": f"/static/images/{row[2]}"
            }
            for row in rows
        ]

        return recommendations

    except sqlite3.Error as e:
        return {"error": f"Database error: {str(e)}"}

    finally:
        conn.close()
