import numpy as np

def health_index(anomaly_score, vibration_rms, temperature_z):
    risk=0.5*np.asarray(anomaly_score)+0.3*np.tanh(np.asarray(vibration_rms))+0.2*np.clip(np.asarray(temperature_z)/4,0,1)
    return np.clip(1-risk,0,1)
