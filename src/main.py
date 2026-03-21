from my_function import *
from pathlib import Path
import os


def main():
    for i in range(12):
        x = factorial_sum(i + i)

        dir_path = Path("outs")
        if not dir_path.exists():
            os.mkdir(dir_path)
        file_path = dir_path / "data.txt"

        with open(file=file_path, mode="a", encoding="utf-8") as f:
            print(f"当 n = {i} 时，阶乘和为 sum = {x}", file=f)


if __name__ == "__main__":
    main()
