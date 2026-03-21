def factorial_sum(n):
    k, sums = 1, 0

    for i in range(1, n + 1):
        k *= i
        sums += k

    return sums


if __name__ == "__main__":
    factorial_sum(12)
