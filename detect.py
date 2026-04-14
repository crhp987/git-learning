from ultralytics import YOLO

# ✅ Use pretrained model (VERY IMPORTANT)
model = YOLO("yolov8n.pt")

def detect_vehicles(frame):
    results = model(frame, conf=0.3)

    count = 0
    vehicle_classes = [2, 3, 5, 7]  # car, bike, bus, truck

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls in vehicle_classes:
                count += 1

    return count, frame