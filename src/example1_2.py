# example1_2.py
# coding=UTF-8

def with_indent():
    n = input("输入一个整数：")
    n = int(n)
    k = 1
    sum = 0

    for i in range(1, n + 1):
        k = k * i
        sum = sum + k

    print("sums=%i" % sum)


def no_indent():
    n = input("输入一个整数：")
    n = int(n)
    k = 1
    sum = 0

    for i in range(1, n + 1):
        k = k * i
    sum = sum + k

    print("sums=%i" % sum)



if __name__ == "__main__":
    # right()
    with_indent()
    no_indent()
