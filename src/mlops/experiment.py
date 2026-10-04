from dataclasses import dataclass, asdict
import json

@dataclass
class ExperimentRecord:
    name: str
    seed: int
    dataset_version: str
    model: str
    notes: str=''
    def to_json(self): return json.dumps(asdict(self),indent=2)
