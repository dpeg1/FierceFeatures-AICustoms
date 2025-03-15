import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

# Facial landmarks defining different face shapes
FACE_SHAPE_LANDMARKS = {
    "oval": [10, 338, 297, 332, 284, 251, 389, 356, 454, 323],
    "round": [152, 396, 175, 199, 164, 92, 205, 50, 209, 198],
    "square": [33, 263, 61, 291, 0, 17, 199, 200, 205, 424]
}

def detect_face_shape(image_path: str):
    """
    Detects facial landmarks in an image and determines face shape.
    
    :param image_path: Path to the image file.
    :return: Face shape category (e.g., "oval", "round", "square") or error message.
    """
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Failed to load image."}

    # Convert image to RGB (Mediapipe requires RGB input)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5) as face_mesh:
        results = face_mesh.process(image_rgb)

        if not results.multi_face_landmarks:
            return {"error": "No face detected in image."}

        face_landmarks = results.multi_face_landmarks[0]

        # Extract landmark coordinates
        landmarks = {}
        for idx, landmark in enumerate(face_landmarks.landmark):
            landmarks[idx] = (landmark.x, landmark.y)

        return classify_face_shape(landmarks)

def classify_face_shape(landmarks):
    """
    Determines the face shape based on landmark positions.
    
    :param landmarks: Dictionary of detected facial landmark coordinates.
    :return: Detected face shape category.
    """
    distances = {}

    for shape, points in FACE_SHAPE_LANDMARKS.items():
        distances[shape] = sum(
            np.linalg.norm(np.array(landmarks[points[i]]) - np.array(landmarks[points[i+1]]))
            for i in range(len(points) - 1)
        )

    best_match = min(distances, key=distances.get)
    return {"face_shape": best_match}

