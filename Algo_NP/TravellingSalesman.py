def tsp(cities, paths, dist):
    for path in permutations(cities):
        min_dist = 0
        for i in range(len(path) - 1):
            min_dist += paths[path[i]][path[i+1]]
            if min_dist >= dist:
                continue
        if min_dist < dist:
            return True
    return False

# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

print(tsp([0, 1, 2, 3],
        [
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],
        1060))