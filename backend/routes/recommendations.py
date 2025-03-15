from fastapi import APIRouter
import sqlite3
from backend.database.db import get_recommended_styles  # Ensure this function exists

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.get("/{face_shape}")
def recommend_styles(face_shape: str):
    """
    Get recommended lash styles based on the detected face shape.
    """
    try:
        # Normalize face shape input
        face_shape = face_shape.lower()

        # Fetch recommended styles from the database
        recommendations = get_recommended_styles(face_shape)

        if not recommendations:
            return {"error": f"No styles found for face shape: {face_shape}"}

        return {"recommended_styles": recommendations}

    except sqlite3.OperationalError as e:
        return {"error": f"Database error: {str(e)}"}

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
