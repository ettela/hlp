import argparse
import textwrap
import zipfile
from pathlib import Path

C_DIR = Path(__file__).resolve().parent
OUT_DIR = C_DIR / "outs"
ZIP_PATH = OUT_DIR / "歪比巴卜.zip"

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
