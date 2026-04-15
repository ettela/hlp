def main1():
    # an_int = 1
    # sum_int = 0

    # while an_int <= 200:
    #     if an_int % 2 == 0:
    #         sum_int += an_int
    #     an_int += 1

    sum_int_ = sum([i for i in range(1, 201) if i % 2 == 0])
    # assert sum_int == sum_int_
    print(f"1-200 的偶数和：{sum_int_}")


def main2():
    sum_sales = 0
    f_sale = float(input("输入订单的销售额:"))
    while f_sale > 0:
        sum_sales += f_sale
        f_sale = float(input("输入下一个订单的销售额:"))
    print(f"销售总额为：{sum_sales}")


def main():
    name_list = ["Beijing", "Shanghai", "Hangzhou", "Nanjing", "Taizhou", "Wuhan"]
    print("城市列表：", " ".join(name_list))


if __name__ == "__main__":
    main()
