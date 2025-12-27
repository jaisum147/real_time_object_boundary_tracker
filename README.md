OVERVIEW:
This project implements a real-time computer vision system to detect and track the boundary of a moving object using a webcam. The solution follows a classical computer vision pipeline using only OpenCV and NumPy, as required. No deep learning models or high-level tracking APIs are used.The system detects object boundaries, isolates the main moving object, and visualizes its geometric properties along with its motion trajectory.
Features:
1.Live webcam video processing
2.Canny edge-based boundary detection
3.Morphological edge stabilization
4.Largest contour-based object isolation
5. it also helps in the visualization of :
      a)Object contour
      b)Bounding box
      c )Convex hull
      d)Centroid trajectory across frames
>>APPROACH:
-->The tracking pipeline follows these steps:

         a)Frame Acquisition:
                       in this step video frame is capturesd using webcame of the system
         b)Preprocessing:
                       in this step captured frame is converted into grayscale and blurred to reduce the noise
         c)Edge Detection:
                       in this step boundary of the object is highlighted using canny edge detection

         d)Edge Stabilization:
                       here in this step Morphological closing is used to connect fragmented edges and smooth contours.

         e)Object Isolation:
                     here in this step external contours are extracted, and the largest contour is assumed to be the moving object.
         d)Contour Analysis & Visualization:
                    here in this step The system draws the object’s contour, bounding box, convex hull, and tracks the centroid position over time to visualize motion.

TECHNOLOGIES USED HERE ARE:
-->python
-->opencv
-->numpy

