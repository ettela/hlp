def f(n):
    if n == 7:
        s = 1
    else:
        s = (f(n + 1) + 1) * 2
    return s


print(f"peaches: {f(1)}")
