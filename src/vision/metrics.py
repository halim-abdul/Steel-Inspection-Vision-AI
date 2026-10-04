import numpy as np

def defect_area_ratio(mask: np.ndarray) -> float:
    mask = np.asarray(mask) > 0
    return float(mask.mean())

def severity_score(confidence: float, area_ratio: float, class_weight: float) -> float:
    return float(np.clip(confidence * (1 + 4 * area_ratio) * class_weight, 0, 5))
