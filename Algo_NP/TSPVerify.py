def verify_tsp(paths, dist, actual_path):
    actual_dist = 0
    for city in range(len(actual_path) - 1):
        actual_dist += paths[city][city + 1]
    if actual_dist < dist:
        return True
    return False
