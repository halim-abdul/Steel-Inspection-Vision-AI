from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class SensorRecord:
    timestamp: datetime
    asset_id: str
    vibration_rms: float
    temperature_c: float
    motor_current_a: float
    line_speed_mps: float
    acoustic_rms: float = 0.0
