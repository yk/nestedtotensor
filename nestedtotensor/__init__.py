import math


def nested_to_tensor(data, limits):
    if isinstance(limits, int):
        limits = [limits]
    limit = limits[0]
    if len(limits) > 1:
        d_new = []
        for d in data:
            d_new.append(nested_to_tensor(d, limits[1:]))
    else:
        d_new = [di for di in data]
    if limit > 0:
        times_too_short = math.ceil((limit - len(data)) / len(data))
        if times_too_short > 0:
            multiple = len(data) / limit
            d_new_tmp = [d_new[math.floor(ii * multiple)] for ii in range(limit)]
            d_new = d_new_tmp
        for _ in range(len(d_new) - limit):
            d_new.pop()
    return d_new
