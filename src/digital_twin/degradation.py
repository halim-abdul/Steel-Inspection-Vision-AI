import numpy as np

def simulate_degradation(n_steps=500, drift=0.002, noise=0.01, seed=42):
    rng=np.random.default_rng(seed)
    increments=np.maximum(drift+rng.normal(0,noise,size=n_steps),-0.02)
    state=np.clip(np.cumsum(increments),0,1)
    return state
