import numpy as np

def population_stability_index(reference, current, bins=10):
    r=np.asarray(reference); c=np.asarray(current)
    q=np.unique(np.quantile(r,np.linspace(0,1,bins+1)))
    if len(q)<3: return 0.0
    rh,_=np.histogram(r,bins=q); ch,_=np.histogram(c,bins=q)
    rp=np.clip(rh/rh.sum(),1e-6,None); cp=np.clip(ch/ch.sum(),1e-6,None)
    return float(np.sum((cp-rp)*np.log(cp/rp)))
