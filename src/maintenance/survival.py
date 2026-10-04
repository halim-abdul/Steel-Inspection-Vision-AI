import numpy as np

def weibull_survival(t, shape, scale):
    t=np.maximum(np.asarray(t,dtype=float),0)
    return np.exp(-((t/scale)**shape))

def hazard(t, shape, scale):
    t=np.maximum(np.asarray(t,dtype=float),1e-12)
    return (shape/scale)*(t/scale)**(shape-1)
