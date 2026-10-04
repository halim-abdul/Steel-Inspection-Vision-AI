import pandas as pd

def align_asof(events, sensors, tolerance='2s'):
    e=events.sort_values('timestamp').copy(); s=sensors.sort_values('timestamp').copy()
    return pd.merge_asof(e,s,on='timestamp',by='asset_id',tolerance=pd.Timedelta(tolerance),direction='nearest')
