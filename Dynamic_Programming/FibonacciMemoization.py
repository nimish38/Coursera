import time
def fibonacci(n, precomputed={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # return fibonacci(n - 1) + fibonacci(n - 2)

    if n - 1 not in precomputed:
        precomputed[n - 1] = fibonacci(n - 1, precomputed)

    if n - 2 not in precomputed:
        precomputed[n - 2] = fibonacci(n - 2, precomputed)

    precomputed[n] = precomputed[n - 1] + precomputed[n - 2]
    return precomputed[n]
    # don't touch below this line


def main():
    for i in range(50):
        print(fibonacci(i))


start_time = time.time()
main()
end_time = time.time()
print("Time taken: ", end_time - start_time, "seconds")