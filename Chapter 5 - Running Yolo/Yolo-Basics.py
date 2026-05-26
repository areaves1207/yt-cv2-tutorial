from ultralytics import YOLO
import cv2

model = YOLO("../Yolo-Weights/yolov8n.pt")
results = model("./Images/3.png")

img = results[0].plot()      # get plotted frame as numpy array
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()