from backend.database.db import get_recommended_styles

def classify_face_shape(landmarks):
    """
    Analyze facial landmarks and classify face shape.
    """
    # Extract key facial points (e.g., jaw width, forehead width)
    jaw_width = landmarks[10]["x"] - landmarks[0]["x"]
    forehead_width = landmarks[50]["x"] - landmarks[20]["x"]
    face_length = landmarks[152]["y"] - landmarks[8]["y"]

    # Simple classification based on proportions
    if face_length > jaw_width * 1.3:
        return "Oval"
    elif jaw_width > forehead_width * 1.2:
        return "Square"
    elif forehead_width > jaw_width * 1.2:
        return "Heart"
    else:
        return "Round"

def recommend_lash_styles(landmarks):
    """
    Get best lash style recommendations based on face shape.
    """
    face_shape = classify_face_shape(landmarks)
    return get_recommended_styles(face_shape)
