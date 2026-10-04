from enum import Enum

class DefectClass(str, Enum):
    SCRATCH = "scratch"
    CRACK = "crack"
    PITTING = "pitting"
    INCLUSION = "inclusion"
    SCALE = "scale"
    ROLLED_IN_SCALE = "rolled_in_scale"
    PATCH = "patch"
    CRAZING = "crazing"

SEVERITY_WEIGHTS = {c.value: w for c, w in zip(DefectClass, [1.0,2.0,1.6,1.4,1.1,1.5,1.2,1.3])}
