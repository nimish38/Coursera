def power_set(input_set):
    final_res = subsets(input_set)
    final_res.append([])
    return final_res

def subsets(input_set):
    resultSet = []
    if len(input_set) == 0:
        return resultSet
    combos = subsets(input_set[1:])
    for subset in combos:
        firstCombo = subset.copy()
        firstCombo.insert(0, input_set[0])
        resultSet.append(firstCombo)
        resultSet.append(subset)
    resultSet.append([input_set[0]])
    return sorted(resultSet, key=lambda x: len(x), reverse=True)
