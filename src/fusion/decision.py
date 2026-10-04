def inspection_action(risk: float) -> str:
    if risk >= 0.85: return 'stop-and-inspect'
    if risk >= 0.65: return 'manual-review'
    if risk >= 0.40: return 'increase-monitoring'
    return 'continue'
