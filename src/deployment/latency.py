from time import perf_counter
from contextlib import contextmanager

@contextmanager
def latency_timer(store, key):
    t=perf_counter(); yield; store[key]=(perf_counter()-t)*1000.0
