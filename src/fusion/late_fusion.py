import numpy as np

def fuse_risk(vision_risk, sensor_risk, maintenance_risk, weights=(0.5,0.3,0.2)):
    w=np.asarray(weights,dtype=float); w=w/w.sum()
    x=np.stack([vision_risk,sensor_risk,maintenance_risk],axis=-1)
    return np.clip(np.sum(x*w,axis=-1),0,1)
