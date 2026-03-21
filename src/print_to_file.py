from pathlib import Path
import os

def main():
    dir_path = Path("outs")
    if not dir_path.exists():
        os.mkdir(dir_path)
    file_path = dir_path / "ok.txt"
    # try file_path.
    with open(file=file_path, mode= "w") as f:
        print("I write Hello World!", file=f)

if __name__=="__main__":
    main()