Handwriting Comparison:

Allows users to compare two images containing handwriting and calculate the similarity between them.
Uses the ORB (Oriented FAST and Rotated BRIEF) algorithm to detect and match features between images.
Provides a percentage similarity score to show how closely the handwriting matches between the two selected images.
Utilizes Tesseract OCR to ensure that both images contain handwritten text before performing the comparison.
Handwriting to Text:

Extracts handwritten text from an image and converts it into editable text.
Includes preprocessing steps like contrast enhancement, sharpening, Gaussian blur, and thresholding to improve OCR accuracy.
Saves the extracted text into a .txt file for further use.
Uses Tesseract OCR with custom configurations for accurate text recognition.
User Interface:

A user-friendly GUI built with Tkinter that integrates the different functionalities of the tool.
Provides buttons for selecting images, comparing handwriting, and extracting text.
Includes visual enhancements like a background image, styled buttons, and responsive design.
Integration:

The main script (main.py) serves as a launcher for individual tools (comparison and text extraction), using subprocesses to execute separate Python scripts.
Technical Highlights:
Image Processing: OpenCV and PIL are used for image manipulation and preprocessing.
OCR Engine: Tesseract OCR extracts text from images, ensuring robust performance.
Feature Matching: ORB and BRIEF algorithms provide efficient keypoint detection and description for handwriting comparison.
Tkinter GUI: Offers an intuitive way for users to interact with the tool.
File Handling: Outputs extracted text into a .txt file for saving and editing.
Use Case Scenarios:
Forensic Handwriting Analysis: Comparing handwritten notes for similarity.
Document Digitization: Converting handwritten notes into digital text for storage and processing.
Educational Tools: Helping students or educators analyze and digitize handwritten materials.
