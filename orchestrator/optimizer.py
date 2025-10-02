def pick_instances(predicted_cores, candidates):
    plan = []
    remaining = predicted_cores
    sorted_c = sorted(candidates, key=lambda c: c['price_per_hour']/c['vcpu'])
    for c in sorted_c:
        can_take = remaining // c['vcpu']
        if can_take > 0:
            plan.append({'instance_type': c['instance_type'], 'count': int(can_take), 'provider': c['provider']})
            remaining -= can_take*c['vcpu']
    if remaining > 0:
        plan.append({'instance_type': sorted_c[0]['instance_type'], 'count': 1, 'provider': sorted_c[0]['provider']})
    return plan
