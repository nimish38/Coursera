def find_last_name(names_dict, first_name):
    if first_name in names_dict.keys():
        return names_dict[first_name]
    return None
