def method_1():
    # 方法一：lambda表达式
    prompt = "Please enter your age (or 'q' to quit): "

    movie_ticket = lambda age: (
        "free" if age < 3 else "10 USD" if age < 13 else "15 USD"
    )

    while (m := input(prompt)) != "q":
        print(f"Your ticket fare is {movie_ticket(int(m))}.")


def method_2():
    # 方法二：函数定义
    prompt = "Please enter your age (or 'q' to quit): "

    def movie_ticket(age):
        if age < 3:
            return "free"
        elif age < 13:
            return "10 USD"
        else:
            return "15 USD"

    while (m := input(prompt)) != "q":
        print(f"Your ticket fare is {movie_ticket(int(m))}.")


if __name__ == "__main__":
    method_2()
