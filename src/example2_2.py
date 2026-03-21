# example2_2.py

def main():
    total = 1500
    price = float(input("请输入书包的价格:")) * 0.85
    left = total - price
    print(f"折扣后书包的价格: {price}")
    print(f"小明买了书包后剩余的钱: {left}")

if __name__ == "__main__":
    main()