def max_sales_days(sales):
    max_sales = max(sales)
    days = tuple(
        map(
            lambda item: item[0],
            filter(lambda item: item[1] == max_sales, enumerate(sales, 1)),
        )
    )
    return max_sales, days


def format_days(days):
    return " ".join(map(lambda day: f"第 {day} 日", days))


def main():
    sales = (
        123, 226, 136, 178, 124, 167, 183,
        194, 119, 135, 189, 125, 173, 193,
        143, 226, 201, 200, 211, 226, 132,
        163, 225, 129, 150, 151, 226, 177,
        189, 134, 222,
    )

    max_sales, max_days = max_sales_days(sales)
    print(f"最大销量：{max_sales}")
    print("销售日分别为：", format_days(max_days))


if __name__ == "__main__":
    main()
