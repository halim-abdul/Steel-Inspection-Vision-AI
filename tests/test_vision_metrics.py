import numpy as np
from src.vision.metrics import defect_area_ratio, severity_score

def test_area_ratio():
    m=np.array([[1,0],[1,0]])
    assert defect_area_ratio(m)==0.5

def test_severity_range():
    assert 0 <= severity_score(0.9,0.1,2.0) <= 5
