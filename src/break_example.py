def break_example():
    num = int(input("请输入一个整数："))
    count = num // 2

    while count > 0:
        if num % count == 0:
            break
        count -= 1

    print(f"{count} is the max factor of {num}.")


def while_with_else():
    n = int(input("请输入一个整数："))
    i = n
    while i > 0:
        if i % 23 == 0:
            print(f"小于等于 {n} 的且能被 23 整除的最大正整数数是 {i}")
            break
        i -= 1
    else:
        print("未找到。")


def for_with_else():
    sales = [5000, 3000, 8000, 10600, 6000, 5000]

    for i in sales:
        if i > 6000:
            print(f"第一个大于 6000 的销售额是 {i}")
            break
    else:
        print("未找到。")


def calc_euler_number():
    e = 1
    n = 1
    while True:
        s = 1
        for i in range(1, n + 1):
            s *= i
        e += 1 / s
        if 1 / s < 1e-8:
            break
        n += 1

    print(f"n = {n}")
    print(f"e = {e}")


def calc_euler_number_without_inner_loop():
    e = 1
    n = 1
    s = 1
    while True:
        s *= n
        e += 1 / s
        if 1 / s < 1e-8:
            break
        n += 1

    print(f"n = {n}")
    print(f"e = {e}")


def find_factor():
    num = int(input("请输入一个自然数："))
    while num != -1:
        count = num // 2
        while count > 0:
            if num % count == 0:
                break
            count -= 1
        print(f"{count} is the factor of {num}")
        num = int(input("请再输入一个自然数："))
    else:
        print("程序结束")


def print_three_digit_primes():
    print("所有的三位素数如下：", end=" ")
    for i in range(100, 1000):
        j = 2
        flag = 1
        while j < i:
            if i % j == 0:
                flag = 0
                break
            j += 1
        if flag == 1:
            print(i, end=" ")


def print_three_digit_primes_method_2():
    print("所有的三位素数如下：", end=" ")
    for i in range(100, 1000):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")


if __name__ == "__main__":
    print_three_digit_primes_method_2()
