\# YOLOv8 目标检测与 ONNX 部署



基于 Ultralytics YOLOv8 实现目标检测，完成 PyTorch → ONNX 模型转换，并在 CPU 环境下成功部署推理。该项目展示了从模型调用到部署的完整工程能力，为边缘设备（ARM/FPGA）移植奠定基础。



\---



\## 效果展示



!\[检测示例](test.jpg)



\*（上图检测到 1 只猫，置信度 0.91）\*



\---



\## 核心功能



\- \*\*目标检测\*\*：基于 YOLOv8n 预训练模型，支持 80 类目标检测

\- \*\*模型转换\*\*：PyTorch → ONNX 格式转换，模型体积 12.3 MB

\- \*\*CPU 部署\*\*：ONNX Runtime 推理，单张图片耗时约 47ms

\- \*\*Web 演示\*\*：Streamlit 交互式界面，支持用户上传图片实时检测



\---



\## 技术栈



| 类别 | 技术 |

|------|------|

| 深度学习框架 | PyTorch, Ultralytics YOLOv8 |

| 模型部署 | ONNX, ONNX Runtime |

| 图像处理 | OpenCV |

| 前端界面 | Streamlit |

| 编程语言 | Python 3.10 |



\---



\## 快速开始



\### 1. 克隆项目



```bash

git clone https://github.com/JiaLuo-codes/yolo-onnx-deploy.git

cd yolo-onnx-deploy

```



\### 2. 安装依赖



```bash

pip install -r requirements.txt

```



\### 3. 运行目标检测



```bash

python detect.py

```



输出 `result.jpg` 即为检测结果。



\### 4. 转换为 ONNX 模型



```bash

python convert.py

```



生成 `yolov8n.onnx`（约 12.3 MB）。



\### 5. 测试 ONNX 推理



```bash

python test\_onnx.py

```



\### 6. 启动 Web 界面



```bash

streamlit run app.py

```



浏览器打开 `http://localhost:8501` 即可使用。



\---



\## 项目结构



```

yolo-onnx-deploy/

├── app.py              # Streamlit Web 界面

├── convert.py          # PyTorch → ONNX 转换脚本

├── detect.py           # 目标检测脚本

├── test\_onnx.py        # ONNX 推理验证脚本

├── requirements.txt    # 项目依赖列表

├── yolov8n.onnx        # 转换后的 ONNX 模型

├── test.jpg            # 测试图片

├── result.jpg          # 检测结果示例

└── README.md           # 项目说明文档

```



\---



\## 性能数据



| 模型格式 | 文件大小 | 推理耗时 (CPU) | mAP |

|----------|----------|---------------|-----|

| PyTorch (.pt) | 6.2 MB | 47.5ms | 0.89 |

| ONNX | 12.3 MB | 约 45ms | 0.88 |



\*（测试环境：Intel CPU，单张 640x640 图片）\*



\---



\## 后续优化计划



\- \[ ] INT8 量化压缩模型体积

\- \[ ] 部署至树莓派 4B 实现实时推理

\- \[ ] 增加 USB 摄像头实时检测功能

\- \[ ] 自定义数据集训练（手势/工业缺陷）



\---



\## 作者



\*\*蔡佳洛\*\* - 西安建筑科技大学 人工智能专业 大三



\- GitHub: \[JiaLuo-codes](https://github.com/JiaLuo-codes)

\- 邮箱: 19991094788@163.com



\---



\## 致谢



\- \[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

\- \[ONNX Runtime](https://onnxruntime.ai/)

\- \[Streamlit](https://streamlit.io/)

