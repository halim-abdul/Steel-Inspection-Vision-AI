# MLOps and Reproducibility

Every experiment should record Git commit, data version, random seed, model/configuration, hardware, preprocessing and evaluation protocol. Do not commit production data or trained weights by default. CI runs unit tests; expensive GPU training is intentionally separate.
