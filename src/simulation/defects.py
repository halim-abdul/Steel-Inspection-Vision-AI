import numpy as np

def synthetic_scratch(image, seed=42, width=2):
    out=np.asarray(image).copy(); rng=np.random.default_rng(seed)
    h,w=out.shape[:2]; y=int(rng.integers(0,h)); x0=int(rng.integers(0,max(1,w//3))); x1=int(rng.integers(max(x0+1,2*w//3),w))
    for dy in range(-width,width+1):
        yy=np.clip(y+dy,0,h-1); out[yy,x0:x1]=np.asarray(out[yy,x0:x1])*0.35
    return out

def synthetic_pit(image, center=None, radius=8):
    out=np.asarray(image).copy(); h,w=out.shape[:2]; cy,cx=center or (h//2,w//2)
    yy,xx=np.ogrid[:h,:w]; mask=(yy-cy)**2+(xx-cx)**2<=radius**2
    out[mask]=np.asarray(out[mask])*0.45
    return out
