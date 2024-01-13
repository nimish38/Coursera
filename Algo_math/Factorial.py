def num_possible_orders(num_posts):
    res = 1
    while num_posts > 1:
        res *= num_posts
        num_posts -= 1
    return res
