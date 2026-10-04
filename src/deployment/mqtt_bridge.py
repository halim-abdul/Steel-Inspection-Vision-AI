import json

def encode_event(asset_id, risk, action, timestamp):
    return json.dumps({'asset_id':asset_id,'risk':float(risk),'action':action,'timestamp':str(timestamp)})
