import pandas as pd

def validate_sensor_frame(df: pd.DataFrame):
    required={'timestamp','asset_id','vibration_rms','temperature_c','motor_current_a'}
    missing=required-set(df.columns)
    if missing: raise ValueError(f'missing columns: {sorted(missing)}')
    if df['timestamp'].isna().any(): raise ValueError('timestamp contains nulls')
    return True
