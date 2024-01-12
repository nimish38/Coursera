
def find_min(list):
    min_val = float("inf")
    for item in list:
        if item < min_val:
            min_val = item
    return min_val