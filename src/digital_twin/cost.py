def lifecycle_cost(scrap, downtime_h, inspections, failures, costs=None):
    c=costs or {'scrap':100,'downtime_h':500,'inspection':40,'failure':5000}
    return scrap*c['scrap']+downtime_h*c['downtime_h']+inspections*c['inspection']+failures*c['failure']
