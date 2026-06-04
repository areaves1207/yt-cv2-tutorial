from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

cap = cv2.VideoCapture("../Videos/ppe-1-1.mp4") #for video


model = YOLO("./best.pt")

classNames= ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']


while True:

    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:

            #bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # x1, y1, w, h = box.xywh[0]
            w, h = x2-x1, y2-y1
            bbox = (int(x1), int(y1), int(w), int(h))

            #Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            #class name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
            cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0,x1), max(35,y1)), scale=0.6, thickness=1, offset=3)

    
    cv2.imshow("Image", img)
    # cv2.imshow("Image", imgRegion)
    cv2.waitKey(0)
        