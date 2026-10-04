def maintenance_policy(health_index, defect_risk, age_hours):
    if defect_risk>=0.85: return 'inspect-now'
    if health_index<=0.2: return 'planned-stop'
    if health_index<=0.4 or age_hours>5000: return 'schedule-maintenance'
    return 'continue'
