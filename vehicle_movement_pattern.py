import cv2
import numpy as np
import pytesseract
import pandas as pd
from datetime import datetime
import os
from collections import Counter

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize data storage(excel sheet)
data = {}
excel_file = 'vehicle_log.xlsx'

if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
    data = df.set_index('License Plate').to_dict('index')
else:
    df = pd.DataFrame(columns=['License Plate', 'Entry Time', 'Exit Time'])

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 10, 200)
    return edges

def find_license_plate_candidates(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if 2.0 < aspect_ratio < 5.5 and w > 100:
            candidates.append((x, y, w, h))
    return candidates

def extract_plate_number(image, candidate):
    x, y, w, h = candidate
    roi = image[y:y+h, x:x+w]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(threshold, config='--psm 8 --oem 3')
    return ''.join(e for e in text if e.isalnum())

# Buffer to store recent license plate readings
recent_plates = []

def process_frame(frame):
    global recent_plates
    edges = preprocess_image(frame)
    candidates = find_license_plate_candidates(edges)
    
    for candidate in candidates:
        plate_number = extract_plate_number(frame, candidate)
        
        if len(plate_number) > 5:
            recent_plates.append(plate_number)
            
            # Keep only the last 30 readings (approximately 10 seconds at 3 FPS)
            if len(recent_plates) > 30:
                recent_plates.pop(0)
            
            # Find the most common plate number in the recent readings
            plate_counts = Counter(recent_plates)
            most_common_plate, count = plate_counts.most_common(1)[0]
            
            # Only process if this plate number appears at least 3 times
            if count >= 3:
                x, y, w, h = candidate
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, most_common_plate, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                current_time = datetime.now()
                if most_common_plate not in data:
                    data[most_common_plate] = {'Entry Time': current_time, 'Exit Time': None}
                    print(f"New vehicle entered: {most_common_plate}")
                else:
                    data[most_common_plate]['Exit Time'] = current_time
                    print(f"Vehicle exited: {most_common_plate}")
                
                # Update Excel file
                df = pd.DataFrame.from_dict(data, orient='index').reset_index()
                df.columns = ['License Plate', 'Entry Time', 'Exit Time']
                
                # Convert timestamps
                df['Entry Time'] = pd.to_datetime(df['Entry Time']).dt.strftime('%Y-%m-%d %H:%M:%S')
                df['Exit Time'] = pd.to_datetime(df['Exit Time']).dt.strftime('%Y-%m-%d %H:%M:%S')
                
                df.to_excel(excel_file, index=False)
    
    return frame

# Main execution
cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    processed_frame = process_frame(frame)
    cv2.imshow('License Plate Detection', processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
