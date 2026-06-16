from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model('test.jpg')   # 改成你图片的文件名
annotated_frame = results[0].plot()
cv2.imwrite('result.jpg', annotated_frame)
print("检测完成")