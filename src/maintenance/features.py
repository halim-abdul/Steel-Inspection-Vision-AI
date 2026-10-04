import numpy as np

def rolling_features(x, window=32):
    x=np.asarray(x,dtype=float)
    if len(x)<window: return {}
    z=x[-window:]
    return {'mean':float(z.mean()),'std':float(z.std()),'rms':float(np.sqrt(np.mean(z*z))),'peak':float(np.max(np.abs(z))),'crest_factor':float(np.max(np.abs(z))/(np.sqrt(np.mean(z*z))+1e-12))}
