import cv2
import numpy as np
from collections import deque

# Parameters 

CANNY_LOW = 50
CANNY_HIGH = 150
MIN_CONTOUR_AREA = 1200
TRAIL_LENGTH = 60

# Store centroid positions
centroid_history = deque(maxlen=TRAIL_LENGTH)

# Start webcam

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for smoother performance
    frame = cv2.resize(frame, (640, 480))
    output = frame.copy()
    
    # Preprocessing
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
   
    edges = cv2.Canny(gray, CANNY_LOW, CANNY_HIGH)

    # Edge stabilization
    
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours
    
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        # Pick the largest contour (assumed moving object)
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > MIN_CONTOUR_AREA:

            # Draw contour
            cv2.drawContours(output, [largest], -1, (0, 255, 0), 2)

            # Bounding box
            x, y, w, h = cv2.boundingRect(largest)
            cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Convex hull
            hull = cv2.convexHull(largest)
            cv2.drawContours(output, [hull], -1, (0, 0, 255), 2)

            # -----------------------------
            # Centroid calculation
            # -----------------------------
            M = cv2.moments(largest)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                centroid_history.append((cx, cy))
                cv2.circle(output, (cx, cy), 5, (0, 255, 255), -1)

    # Draw centroid trajectory
    
    for i in range(1, len(centroid_history)):
        cv2.line(
            output,
            centroid_history[i - 1],
            centroid_history[i],
            (0, 255, 255),
            2
        )

    # Display result
    
    cv2.imshow("Moving Object Boundary Tracker", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup

cap.release()
cv2.destroyAllWindows()

