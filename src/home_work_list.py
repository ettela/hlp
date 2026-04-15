def input_list(prompt: str, num: int) -> list[int]:
    while True:
        _list = input(f"{prompt} （输入 {num} 个整数，空格分隔）：").split()
        
        try:
            res = list(map(int, _list))
        except ValueError:
            print(f"错误：请输入 {num} 个整数。")
            continue

        if len(res) == num:
            return res
        print(f"错误：请输入 {num} 个整数。")


def main():
    list1 = input_list("输入 list1", 4)
    list2 = input_list("输入 list2", 3)
    # list1.extend(list2)
    # list1.append(90)
    # list1.append(100)
    # list1.sort(reverse=True)
    list1 = sorted(list1 + list2 + [90, 100], reverse=True)
    print(f"{list1 = }")


if __name__ == "__main__":
    main()
