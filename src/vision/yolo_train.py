from pathlib import Path
from ultralytics import YOLO

def train(data_yaml: str, model: str = "yolov8m.pt", epochs: int = 100, imgsz: int = 640):
    net = YOLO(model)
    return net.train(data=data_yaml, epochs=epochs, imgsz=imgsz, project="runs/steel_defects", seed=42)

if __name__ == "__main__":
    train("configs/steel_defects.yaml")
