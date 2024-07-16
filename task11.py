import cv2
import mediapipe as mp

# Function to detect and localize clothing parts
def detect_clothing_parts(image_path):
    # Load MediaPipe Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

    # Read image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect pose
    results = pose.process(image_rgb)

    # Draw landmarks (for visualization)
    if results.pose_landmarks:
        # Define the landmarks for sleeves, collar, neck, and chest (based on MediaPipe landmarks)
        # Example: sleeves, collar, neck, chest indices from the pose_landmarks
        sleeves = []
        collar = []
        neck = []
        chest = []

        # Draw landmarks 
        mp_drawing = mp.solutions.drawing_utils
        annotated_image = image.copy()
        mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Highlight regions 
        for landmark in sleeves:
            # Example: Draw rectangle around sleeve area
            cv2.rectangle(annotated_image, (landmark[0], landmark[1]), (landmark[2], landmark[3]), (255, 0, 0), 2)

        for landmark in collar:
            # Example: Draw rectangle around collar area
            cv2.rectangle(annotated_image, (landmark[0], landmark[1]), (landmark[2], landmark[3]), (0, 255, 0), 2)

        for landmark in neck:
            # Example: Draw rectangle around neck area
            cv2.rectangle(annotated_image, (landmark[0], landmark[1]), (landmark[2], landmark[3]), (0, 0, 255), 2)

        for landmark in chest:
            # Example: Draw rectangle around chest area
            cv2.rectangle(annotated_image, (landmark[0], landmark[1]), (landmark[2], landmark[3]), (255, 255, 0), 2)

        # Display annotated image
        cv2.imshow('Clothing Parts Detection', annotated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("No pose landmarks detected in the image.")

    # Release resources
    pose.close()

image_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\2.jpg'

detect_clothing_parts(image_path)
