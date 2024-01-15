
def get_avg_brand_followers(all_handles, brand_name):
    hits = 0
    for followers in all_handles:
        for handle in followers:
            if brand_name in handle:
                hits += 1
    return hits / len(all_handles)