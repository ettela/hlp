def list_to_tuple():
    print("请输入若干个字符串组成列表 list1 ，当提示输出为 y 或 yes 结束，大小写无关")
    yy = "n"
    i = 1
    list1 = []
    while yy.lower() not in ["y", "yes"]:
        str1 = input(f"请输入第{i}个元素：")
        list1.append(str1)
        i += 1
        yy = input("是否结束输入？（y / yes）")
    tuple1 = tuple(list1)
    print("列表 list1：", list1)
    print("元组 tuple1：", tuple1)


def list_2_tuple_method_2():
    print("请输入若干个字符串组成列表 list1 ，当提示输出为 y 或 yes 结束，大小写无关")
    stop_words = {"y", "yes"}

    def iter_items():
        while True:
            s = input("请输入一个元素：")
            if s.strip().casefold() in stop_words:
                return
            yield s

    list1 = list(iter_items())
    tuple1 = tuple(list1)
    print("列表 list1：", list1)
    print("元组 tuple1：", tuple1)


if __name__ == "__main__":
    # list_to_tuple()
    # print("\n")
    list_2_tuple_method_2()
