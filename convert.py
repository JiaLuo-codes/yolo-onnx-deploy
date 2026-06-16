from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.export(format='onnx', imgsz=640)
print("ONNX模型已生成：yolov8n.onnx")