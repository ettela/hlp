def method_1():
    """
    方法一
    """
    number = input("请输入股票代码：")
    name = input("请输入股票名称：")
    highest = float(input("请输入当天最高价："))
    lowest = float(input("请输入当天最低价："))
    diff = highest - lowest
    print(f"股票代码: {number}\t股票名称：{name}")
    print(f"最高价: {highest}\t最低价: {lowest}\t差值: {diff}")


def method_2():
    """
    方法二
    """
    number = input("请输入股票代码：")
    name = input("请输入股票名称：")
    highest = input("请输入当天最高价：")
    lowest = input("请输入当天最低价：")
    diff = float(highest) - float(lowest)
    print(f"股票代码: {number}\t股票名称：{name}")
    print(f"最高价: {highest}\t最低价: {lowest}\t差值: {diff}")


def method_3():
    """
    方法三
    """
    print('输入以"," 或 "，"号分隔')
    number_and_name = input("请输入股票代码和名称：").replace("，", ",")
    number, name = map(str, number_and_name.split(","))
    highest_and_lowest = input("请输入当天最高价和最低价：").replace("，", ",")
    highest, lowest = map(float, highest_and_lowest.split(","))
    diff = highest - lowest
    print(f"股票代码: {number}\t股票名称：{name}")
    print(f"最高价: {highest:.2f}\t最低价: {lowest:.2f}\t差值: {diff:.2f}")


def main():
    func_list = [method_1, method_2, method_3]
    for i, func in enumerate(func_list, start=1):
        print(f"{"方法 %d" % i:=^40}")
        func()


if __name__ == "__main__":
    main()