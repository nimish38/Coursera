def edit_distance(str1, str2):
    i, j = len(str1), len(str2)
    grid = []
    for k in range(i + 1):
        grid.append([0] * (j + 1))
    for row in range(i + 1):
        for col in range(j + 1):

            if row == 0:
                grid[row][col] = j
            if j == 0:
                grid[row][col] = i
            if str1[row - 1] == str2[col - 1]:
                grid[row][col] = grid[row - 1][col - 1]
            else:
                grid[row][col] = 1 + min(grid[row][col-1], grid[row-1][col], grid[row-1][col-1])
    return grid[-1][-1]




    # don't touch below this line


def main():
    print_edit_distance("burger king", "burger king")
    print_edit_distance("mcdonalds", "mc donalds")
    print_edit_distance("docter office", "doctors office")
    print_edit_distance("park", "parc")
    print_edit_distance("moms house", "moms hows")
    print_edit_distance("abracadabra", "abracad")
    print_edit_distance("abracadabra", "konkadonk")
    print_edit_distance(
        "Mount Kilimanjaro in Tanzania", "Everest the mountain in the himalayas"
    )


def print_edit_distance(w1, w2):
    print(f"edit distance of {w1} and {w2}: {edit_distance(w1, w2)}")


main()
