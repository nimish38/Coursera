def fibonacci(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # return fibonacci(n - 1) + fibonacci(n - 2)

    val = [None] * (n + 1)
    val[0] = 0

    if n > 0:
        val[1] = 1

    for i in range(2, n + 1):
        val[i] = val[i - 1] + val[i - 2]
    return val[n]

    # don't touch below this line


def main():
    for i in range(75):
        print(fibonacci(i))


main()
