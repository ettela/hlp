from pathlib import Path


def main():
    path = Path().cwd() / "src" / "mozi_orbit.txt"
    import os
    path2 = os.path.dirname(__file__)
    print(path)
    mozi = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    clean_lines = [line.strip() for line in lines if line.strip()]
    for line in clean_lines:
        mozi.append(float(line))
    print(mozi)
    print(f"墨子号的最大轨道半径为 {max(mozi)}")
    print(f"墨子号的最小轨道半径为 {min(mozi)}")


if __name__ == "__main__":
    main()
