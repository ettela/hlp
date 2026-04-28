def dictional_tests():
    stu_dict = {
        "张琳": 58,
        "孙治平": 70,
        "徐小伟": 89,
        "徐丽萍": 69,
        "童方丽": 90,
        "钱志敏": 84,
        "赵虚余": 64,
    }

    stu_dict["晋宇浩"] = "缺考"
    stu_dict["张琳"] = 60
    del stu_dict["徐小伟"]
    total_students = len(stu_dict)
    print(f"总共有 {total_students} 名学生。")

    def find_stu_via_input():
        name = input("请输入学生姓名：")
        if name in stu_dict:
            print(f"{name}的成绩是：{stu_dict[name]}")
        else:
            print("没有找到该学生的信息。")

    while True:
        find_stu_via_input()


def list_unique_via_set_tests():
    import random

    num_list = [random.randint(1, 9) for _ in range(15)]
    print(f"原始列表：{num_list}")
    unique_nums_list = list(set(num_list))
    print(f"去重列表：{unique_nums_list}")
    # keep the original order
    keep_order_unique_nums_list = sorted(unique_nums_list, key=num_list.index)
    print(f"保持次序去重列表：{keep_order_unique_nums_list}")


def set_operations_tests():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(f"集合A：{set_a = }")
    print(f"集合B：{set_b = }")
    print(f"并集：{(set_a | set_b) = }")
    print(f"交集：{(set_a & set_b) = }")
    print(f"差集: {(set_a - set_b) = }")
    print(f"对称差集：{(set_a ^ set_b) = }")


if __name__ == "__main__":
    set_operations_tests()
