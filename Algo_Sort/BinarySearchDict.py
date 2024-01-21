def binary_search(data, followers):
    low, high = 0, len(data)
    while low < high:
        mid = (high + low) // 2
        if data[mid]['followers'] == followers:
            return data[mid]['name']
        if data[mid]['followers'] < followers:
            low = mid + 1
        else:
            high = mid - 1

    if low < len(data) and data[low]['followers'] == followers:
        return data[low]['name']
    return None
#
# binary_search([{'name': 'John', 'followers': 5}, {'name': 'Jane', 'followers': 10}, {'name': 'James', 'followers': 15}, {'name': 'Judy', 'followers': 20}], 10)