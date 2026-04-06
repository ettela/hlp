import math


def example1():
    r = float(input("请输入圆的半径："))
    if r <= 0:
        print("半径应当为正数！")
        return
    else:
        area = math.pi * r**2
        s = math.pi * r * 2
        print(f"圆的周长为：{s}\t圆的面积为：{area}")


def example2():
    t = input("请输入年份：")
    t = int(t)
    if t % 400 == 0 or (t % 4 == 0 and t % 100 != 0):
        print(f"{t} 年是闰年")
    else:
        print(f"{t} 年不是闰年")


def example3():
    price = float(input("请输入商品价格："))
    qauntity = int(input("请输入购买数量："))

    if qauntity < 0:
        coff = -1
    elif qauntity < 300:
        coff = 0
    elif qauntity < 500:
        coff = 0.03
    elif qauntity < 1000:
        coff = 0.05
    elif qauntity < 2000:
        coff = 0.08
    else:
        coff = 0.1
    if qauntity >= 0 and price >= 0:
        pays = price * qauntity * (1 - coff)
        print(f"支付金额：{pays:.2f}")
    else:
        print("输入的订货量与标准价格均不能小于零！")


def example4():
    customer_type = int(input("请输入客户类型（小于5为新客户）："))
    price = float(input("请输入标准价格："))
    quantity = int(input("请输入订货数量："))

    if customer_type > 0 and price > 0 and quantity > 0:
        if customer_type < 5:
            if quantity < 800:
                coff = 0
            else:
                coff = 0.02
        else:
            if quantity < 500:
                coff = 0.03
            elif quantity < 1000:
                coff = 0.05
            elif quantity < 2000:
                coff = 0.08
            else:
                coff = 0.1

        pays = price * quantity * (1 - coff)
        print(f"应付款为：{pays:.2f}")

    else:
        print("输入错误。")

def main():...

if __name__ == "__main__":
    main()
