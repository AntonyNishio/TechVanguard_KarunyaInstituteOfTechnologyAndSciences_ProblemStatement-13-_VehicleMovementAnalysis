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
3. [Features](#features)
4. [Configuration](#configuration)
5. [Screenshots/Demo](#screenshotsdemo)
6. [API Reference](#api-reference)
7. [Contributing](#contributing)
8. [Testing](#testing)
9. [License](#license)
10. [Authors and Acknowledgments](#authors-and-acknowledgments)
11. [Contact Information](#contact-information)
12. [Changelog](#changelog)
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
Parking Occupancy Monitoring: Real-time monitoring of parking lots.
Vehicle Database Matching: Identify unauthorized vehicles by matching against the approved database.
# Solutions<br/>
The system should be able to analyze the frequency and timing of vehicle movement in and out of a campus. It should be able to identify peak times and patterns of vehicle movement. This could be useful for improving traffic flow and security. The system should be able to monitor the occupancy of parking lots in real time. It should be able to identify which parking lots are frequently occupied and at what times. This could be useful for helping drivers find parking spots more easily. The system should be able to match captured vehicle images and license plates to an approved vehicle database. It should be able to identify unauthorized vehicles. This could be useful for security purposes.<br />
#

