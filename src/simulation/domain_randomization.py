import numpy as np

def randomize_intensity(image, seed=42, gain=(0.8,1.2), offset=(-15,15)):
    rng=np.random.default_rng(seed); g=rng.uniform(*gain); b=rng.uniform(*offset)
    return np.clip(np.asarray(image,dtype=float)*g+b,0,255).astype(np.uint8)
