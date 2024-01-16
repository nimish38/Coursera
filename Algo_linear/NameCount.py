def count_names(list_of_lists, target_name):
    hits = 0
    for names in list_of_lists:
        hits += names.count(target_name)
    return hits
