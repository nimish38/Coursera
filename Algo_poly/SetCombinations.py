def power_set(input_set):
    resultSet = []
    if len(input()) == 0:
        return resultSet
    combos = power_set(input_set[1:])
    for subset in combos:
        firstCombo = subset.insert(input_set[0], 0)
        resultSet.append(firstCombo, subset)
    return resultSet
