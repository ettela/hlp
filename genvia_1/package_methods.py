import argparse
import textwrap
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUT_DIR = SCRIPT_DIR / "dist"
DEFAULT_ZIP = DEFAULT_OUT_DIR / "methods.zip"

SOURCES = {
    "method_1.py": textwrap.dedent(
        """\
        x = 1
        for i in range(6, 0, -1):
            x = (x + 1) * 2

        print(f"peaches: {x}")
        """
    ),
    "method_2.py": textwrap.dedent(
        """\
        def f(n):
            if n == 7:
                s = 1
            else:
                s = (f(n + 1) + 1) * 2
            return s


        print(f"peaches: {f(1)}")
        """
    ),
}


def build_dir(dest: Path) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    for name, content in SOURCES.items():
        (dest / name).write_text(content, encoding="utf-8")
    return dest


def build_zip(dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, content in SOURCES.items():
            zf.writestr(name, content)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Package embedded method_1.py and method_2.py into a folder and/or zip."
    )
    parser.add_argument("--dir", type=Path, help="Output directory to create.")
    parser.add_argument("--zip", type=Path, help="Output zip file path.")
    args = parser.parse_args()

    out_dir = args.dir
    out_zip = args.zip

    if out_dir is None and out_zip is None:
        out_dir = DEFAULT_OUT_DIR
        out_zip = DEFAULT_ZIP

    if out_dir is not None:
        created_dir = build_dir(out_dir)
        print(f"Folder created: {created_dir}")

    if out_zip is not None:
        created_zip = build_zip(out_zip)
        print(f"Zip created: {created_zip}")


if __name__ == "__main__":
    main()
