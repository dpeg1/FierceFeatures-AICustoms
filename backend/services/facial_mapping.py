import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

def process_image(image_path: str):
    """
    Detects facial landmarks in an image and extracts eye, brow, and lash positions.
    """
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Failed to load image."}

    # Convert image to RGB (Mediapipe requires RGB input)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize FaceMesh Model
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5) as face_mesh:
        results = face_mesh.process(image_rgb)

        if not results.multi_face_landmarks:
            return {"error": "No face detected in image."}

        # Extract facial landmarks
        landmarks = []
        for face_landmarks in results.multi_face_landmarks:
            for i, landmark in enumerate(face_landmarks.landmark):
                landmarks.append({
                    "id": i,
                    "x": landmark.x,
                    "y": landmark.y,
                    "z": landmark.z
                })

        print(f"🔹 Detected {len(landmarks)} facial landmarks.")  # Debugging output

        return {
            "message": "Facial mapping successful.",
            "landmarks": landmarks
        }
