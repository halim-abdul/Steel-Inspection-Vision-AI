import numpy as np
from sklearn.ensemble import RandomForestRegressor

class RULRegressor:
    def __init__(self, n_estimators=300, random_state=42):
        self.model=RandomForestRegressor(n_estimators=n_estimators,random_state=random_state,n_jobs=-1)
    def fit(self,X,y): self.model.fit(X,y); return self
    def predict(self,X): return np.maximum(self.model.predict(X),0.0)
