>>Real-Time Moving Object Boundary Tracker:

-->Overview
This project implements a real-time computer vision system to detect and track the boundary of a moving object using a webcam. The solution follows a classical computer vision approach using OpenCV and NumPy only, without any machine learning or pre-trained models.
The system highlights object boundaries, isolates the main moving object, and visualizes its shape and motion across frames.

-->Features
1.Live webcam video processing

2.Canny edge-based boundary detection

3.Morphological edge stabilization

4.Largest contour-based object detection

5.Visualization of:
   a)Object contour
   b)Bounding box
   c)Convex hull
   d)Centroid trajectory (motion path)

>>Approach
-->The processing pipeline works as follows:

     1.Frame Acquisition:
         Frames are captured in real time from the system webcam.

     2.Preprocessing:
         Each frame is converted to grayscale and smoothed using Gaussian blur to reduce noise.
     3.Edge Detection:
         Canny edge detection is applied to extract object boundaries.
     4:Edge Stabilization
         Morphological closing is used to connect broken edges and improve contour continuity.
     5.Contour Detection
         External contours are extracted, and the largest contour is assumed to represent the moving object.

     6.Visualization
         The detected object’s contour, bounding box, convex hull, and centroid trajectory are drawn directly on the video feed.

>>Technologies Used
1.Python 3
2.OpenCV
3.NumPy
(note:No deep learning models, tracking APIs, or pre-trained frameworks are used.)

>>Setup Instructions

1.Clone the repository:
git clone https://github.com/jaisum147/real_time_object_boundary_tracker.git
cd real-time-object-boundary-tracker

2.Install required dependencies:
pip install opencv-python numpy

3.Run the program:
python object_tracker.py
4.Press q to exit the application.
6.Usage Notes
-->For best results, ensure that only one object is moving prominently in the camera view.
The system assumes the largest detected contour corresponds to the target object.
Parameters such as Canny thresholds and minimum contour area can be adjusted directly in the code.

Results
The application runs in real time and provides smooth visualization of object boundaries and motion trajectory. The centroid path helps visualize how the object moves across consecutive frames.
