def edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])

    insert_distance = edit_distance(str1, str2[:-1])
    remove_distance = edit_distance(str1[:-1], str2)
    substitute_distance = edit_distance(str1[:-1], str2[:-1])

    return 1 + min(insert_distance, remove_distance, substitute_distance)

    # don't touch below this line


def main():
    print_edit_distance("burger king", "burger king")
    print_edit_distance("mcdonalds", "mc donalds")
    print_edit_distance("docter office", "doctors office")
    print_edit_distance("park", "parc")
    print_edit_distance("moms house", "moms hows")
    print_edit_distance("abracadabra", "abracad")


def print_edit_distance(w1, w2):
    print(f"edit distance of {w1} and {w2}: {edit_distance(w1, w2)}")


main()