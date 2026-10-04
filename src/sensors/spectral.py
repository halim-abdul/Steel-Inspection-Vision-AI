import numpy as np

def fft_band_energy(x, fs, bands):
    x=np.asarray(x,dtype=float)
    f=np.fft.rfftfreq(len(x),1/fs)
    p=np.abs(np.fft.rfft(x-x.mean()))**2
    return {name:float(p[(f>=lo)&(f<hi)].sum()) for name,(lo,hi) in bands.items()}
