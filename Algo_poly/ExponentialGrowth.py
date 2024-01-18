def exponential_growth(n, factor, days):
    growth = [n]
    while days > 0:
        n *= factor
        growth.append(n)
        days -= 1
    return growth