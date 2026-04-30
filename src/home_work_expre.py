def main():
    sales = [
        123, 226, 136, 178, 124, 167, 183,
        194, 119, 135, 189, 125, 173, 193,
        143, 226, 201, 200, 211, 226, 132,
        163, 225, 129, 150, 151, 226, 177,
        189, 134, 222,
    ]

    max_sales = max(sales)
    max_days = [day for day, sale in enumerate(sales, 1) if sale == max_sales]
    print(f"最大销量：{max_sales}")
    print("销售日分别为：", " ".join(f"第 {day} 日" for day in max_days))


if __name__ == "__main__":
    main()
