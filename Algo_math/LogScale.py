import math
def log_scale(data, base):
    for i in range(len(data)):
        data[i] = math.log(data[i], base)
    return data