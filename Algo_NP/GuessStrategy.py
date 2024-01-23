def get_num_guesses(length):
    cnt = 0
    for power in range(1, length + 1):
        cnt += 26**power
    return cnt