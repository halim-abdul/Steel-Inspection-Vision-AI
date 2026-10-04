import numpy as np
from sklearn.ensemble import IsolationForest

class SensorAnomalyDetector:
    def __init__(self, contamination=0.01, random_state=42):
        self.model=IsolationForest(contamination=contamination,random_state=random_state,n_estimators=300,n_jobs=-1)
    def fit(self,X): self.model.fit(X); return self
    def score(self,X):
        raw=-self.model.score_samples(X)
        lo,hi=np.percentile(raw,[1,99])
        return np.clip((raw-lo)/(hi-lo+1e-12),0,1)
