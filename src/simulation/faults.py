import numpy as np

def inject_sensor_fault(x, kind='bias', magnitude=1.0, seed=42):
    x=np.asarray(x,dtype=float).copy(); rng=np.random.default_rng(seed)
    if kind=='bias': x += magnitude
    elif kind=='drift': x += np.linspace(0,magnitude,len(x))
    elif kind=='spikes':
        idx=rng.choice(len(x),size=max(1,len(x)//50),replace=False); x[idx]+=magnitude
    elif kind=='dropout':
        idx=rng.choice(len(x),size=max(1,len(x)//20),replace=False); x[idx]=np.nan
    else: raise ValueError(kind)
    return x
