import numpy as np

def bootstrap_ci(values, statistic=np.mean, n_boot=2000, alpha=0.05, seed=42):
    x=np.asarray(values); rng=np.random.default_rng(seed)
    stats=[statistic(rng.choice(x,size=len(x),replace=True)) for _ in range(n_boot)]
    return tuple(np.quantile(stats,[alpha/2,1-alpha/2]))
