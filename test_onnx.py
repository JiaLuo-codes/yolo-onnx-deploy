import cv2
import numpy as np
import onnxruntime as ort

# 加载 ONNX 模型
session = ort.InferenceSession('yolov8n.onnx', providers=['CPUExecutionProvider'])

# 读取并预处理图片
img = cv2.imread('test.jpg')
img = cv2.resize(img, (640, 640))
img = img[:, :, ::-1].transpose(2, 0, 1) / 255.0
input_tensor = np.expand_dims(img, axis=0).astype(np.float32)

# 推理
outputs = session.run(None, {'images': input_tensor})
print(f"ONNX 推理成功，输出 shape: {outputs[0].shape}")