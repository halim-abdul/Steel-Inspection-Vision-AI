from ultralytics import YOLO

def predict(source, weights="weights/steel_yolov8.pt", conf=0.25, iou=0.5):
    model = YOLO(weights)
    return model.predict(source=source, conf=conf, iou=iou, save=False)
