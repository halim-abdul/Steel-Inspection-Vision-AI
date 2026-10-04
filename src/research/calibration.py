import numpy as np

def expected_calibration_error(prob, y, bins=15):
    prob=np.asarray(prob,dtype=float); y=np.asarray(y,dtype=float)
    edges=np.linspace(0,1,bins+1); ece=0.0
    for lo,hi in zip(edges[:-1],edges[1:]):
        m=(prob>lo)&(prob<=hi)
        if m.any(): ece += m.mean()*abs(prob[m].mean()-y[m].mean())
    return float(ece)
