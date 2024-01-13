def get_follower_prediction(follower_count, influencer_type, num_months):
    Type = {"fitness": 4, "cosmetic": 3, "others": 2}
    if influencer_type not in Type.keys():
        influencer_type = 'others'
    return follower_count * (Type[influencer_type] ** num_months)
