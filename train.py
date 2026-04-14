from ultralytics import YOLO

# 🚦 Load pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# 🚀 Train on your dataset
model.train(
    data="dataset/ready_yolo_dataset/data.yaml",  # dataset config file
    epochs=30,                 # training iterations
    imgsz=640,                # image size
    batch=16,                 # batch size
    name="traffic_model"      # output folder name
)

print("✅ Training completed successfully!")

