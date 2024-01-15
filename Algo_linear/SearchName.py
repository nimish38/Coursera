def does_name_exist(first_names, last_names, full_name):
    # for first in first_names:
    #     for last in last_names:
    #         if full_name == first + ' ' + last:
    #             return True
    # return False

    full_name = list(full_name.split())
    if full_name[0] in first_names and full_name[1] in last_names:
        return True
    return False
