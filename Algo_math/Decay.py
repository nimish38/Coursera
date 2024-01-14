def decayed_followers(intl_followers, fraction_lost_daily, days):
    for i in range(days):
        intl_followers -= intl_followers * fraction_lost_daily
    return intl_followers
