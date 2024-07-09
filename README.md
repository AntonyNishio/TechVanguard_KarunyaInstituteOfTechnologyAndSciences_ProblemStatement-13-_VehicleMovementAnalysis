# TechVanguard_KarunyaInstituteOfTechnologyAndSciences_ProblemStatement-13-_VehicleMovementAnalysis <br/>
Team Name - Tech Vanguard<br/>
Problem Statement Number - 13<br/>
Problem Statement - Vehicle Movement Analysis and Insight Generation in a College Campus using Edge AI <br/>
<br/>

# Description<br/>
## Overview <br/>
The Campus Vehicle Monitoring System is a comprehensive solution designed to enhance vehicle management and security within a campus. The system utilizes advanced computer vision and data analysis techniques to monitor vehicle movements, parking occupancy, and match vehicles against an approved database.<br/>
# Table of Contents
1. [Features](#Features)
2. [Benefits](#Benefits)
3. [Technologies Used](#Technologies_Used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Vehicle_movement_pattern](#Vehicle_movement_pattern)
7. [Contributing](#contributing)
8. [Testing](#testing)

# Features<br/>
## Vehicle Movement Patterns <br/>
Analysis of Frequency and Timing: The system analyzes the frequency and timing of vehicle movements in and out of the campus.<br/>
Peak Time Identification: It identifies peak times and movement patterns, providing valuable insights for traffic management.<br/>
## Parking Occupancy <br/>
Real-time Monitoring: The system monitors the occupancy of parking lots in real-time.<br/>
Frequent Occupancy Identification: It identifies which parking lots are frequently occupied and at what times, aiding in better parking space management.<br/>
## Vehicle Matching <br/>
Database Matching: Captured vehicle images and license plates are matched against an approved vehicle database.<br/>
Unauthorized Vehicle Identification: The system can identify unauthorized vehicles, enhancing campus security.<br/>
# Benefits<br/>
Improved Traffic Management: Helps in managing vehicle flow and reducing congestion by identifying peak times and patterns.<br/>
Enhanced Parking Management: Provides real-time occupancy data, aiding in efficient parking space allocation.<br/>
Increased Security: Matches vehicles against a database to identify unauthorized vehicles, improving campus safety.<br/>
# Technologies_Used<br/>
NumPy: For numerical operations and data manipulation.<br/>
OpenCV: For computer vision and image processing tasks.<br/>
Torch: For deep learning and model inference.<br/>
YOLO: For real-time object detection.<br/>
Pytesseract: For optical character recognition of license plates.<br/>
Collections: For efficient data handling and manipulation.<br/>

# Installation<br/>
## Install the required packages:<br/>
pip install numpy opencv-python torch pytesseract collections<br/>
## Install Tesseract OCR:<br/>
Download and install Tesseract from here - https://github.com/tesseract-ocr/tesseract<br/>
Set up the Tesseract executable path in the code: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
<br/>
# Usage<br/>
Vehicle Movement Monitoring: Run the main script to start analyzing vehicle movements.<br/>
Parking Occupancy Monitoring: Real-time monitoring of parking lots.<br/>
Vehicle Database Matching: Identify unauthorized vehicles by matching against the approved database.<br/>

# Vehicle_movement_pattern<br/>
The system captures video frames from a camera, detects and reads license plates, logs entry and exit times, and performs data analysis to identify movement patterns and peak times. Key functionalities include:<br/>

License Plate Detection: Uses OpenCV to preprocess images and detect potential license plate regions.<br/>
OCR for Plate Reading: Utilizes Tesseract OCR to extract text from detected license plates.<br/>
Data Logging: Stores vehicle entry and exit times in an Excel file for tracking.<br/>
Real-time Processing: Continuously processes video frames to update the log and overlay detected plates on the video feed.<br/>
Data Analysis and Visualization: Analyzes logged data to generate insights on vehicle movement patterns, peak times, and average duration of stay, with visualizations using Matplotlib and Seaborn.<br/>
<br/>
vehicle_movement_pattern.py : This code detects the license plate and enters the data into an excel sheet.<br/>
vehicle_movemnt_analysis : This code analyses the excel sheet produced by vehicle_movement_pattern.py and provides more detailed view of the data with visualizations.

