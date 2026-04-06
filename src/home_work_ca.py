from math import sqrt


def main(test_speed: list[float]):
    # v   = sqrt(G*M/r)
    G_M   = 3.986e14
    R_0   = 4.2164e7
    DELTA = 50e3

    orb_speed = lambda r: sqrt(G_M / r)

    v_0   = orb_speed(R_0)
    v_min = orb_speed(R_0 + DELTA)
    v_max = orb_speed(R_0 - DELTA)

    print(f"标准速度: {v_0:.2f} m/s \t 速度范围: {v_min:.2f} ~ {v_max:.2f} m/s")

    warn_speed = lambda v: (
        "速度偏低，轨道偏高"
        if v <  v_min
        else
        "速度正常，轨道正常"
        if v <= v_max
        else
        "速度偏高，轨道偏低"
    )

    speed_info = lambda v: f"测试速度: {v:.2f} m/s \t 状态: {warn_speed(v)}"

    print(f"{" 速度测试 ":=^42}")
    input_bool = input("是否手动输入测试速度?（y/n）: ").lower() == "y"

    while input_bool:
        try:
            v = float(input("请输入测试速度 (m/s): "))
            print(speed_info(v))
        except ValueError:
            print("输入无效，请输入一个数字。")
        except KeyboardInterrupt:
            print("\n已退出测试。")
            break
    else:
        print(f"{" 使用预设测试速度 ":=^38}")
        for v in test_speed:
            print(speed_info(v))


if __name__ == "__main__":
    test_data = [3070.33, 3073.11, 4000.00]
    main(test_data)
