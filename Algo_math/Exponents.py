def get_estimated_spread(audiences_followers):
    avg_followers = sum(audiences_followers) / len(audiences_followers)
    return avg_followers * (len(audiences_followers) ** 1.2)
