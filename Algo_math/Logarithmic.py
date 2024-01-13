import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log2(num_followers)
