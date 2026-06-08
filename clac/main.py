import tkinter as tk
import re

# from tkinter import ttk
from math import sin, cos, tan, log, exp, sqrt, factorial, pi, e
from dataclasses import dataclass, field

HISTORY_LIMIT = 20


@dataclass
class CalcState:
    expr: str = ""
    result: str = ""
    history: list[str] = field(default_factory=list)
    mode: str = "普通"
    just_eval: bool = False


def safe_eval(expr: str) -> str:
    expr = re.sub(r"(\d+(?:\.\d+)?)!", lambda m: f"factorial({m.group(1)})", expr)
    clean = (
        expr.replace("×", "*")
        .replace("÷", "/")
        .replace("^", "**")
        .replace("π", str(pi))
        .replace("e", str(e))
    )
    ns = {
        "sin" : sin,
        "cos" : cos,
        "tan" : tan,
        "ln"  : log,
        "exp" : exp,
        "sqrt": sqrt,
        "pi"  : pi,
        "factorial"   : factorial,
        "__builtins__": {},
    }
    try:
        val = eval(clean, ns)
        return (
            str(int(val))
            if isinstance(val, float) and val.is_integer()
            else str(round(val, 10)).rstrip("0").rstrip(".")
        )
    except ZeroDivisionError:
        return "零不能做除数"
    except Exception:
        return "错误"


def push_history(state, entry):
    if entry and "错误" not in entry:
        if entry not in state.history:
            state.history.append(entry)
        if len(state.history) > HISTORY_LIMIT:
            state.history.pop(0)


def show_main(root, container):
    root.unbind("<Key>")
    clear_frame(container)
    tk.Label(container, text="计算器应用", font=("黑体", 18, "bold")).pack(pady=30)
    tk.Button(
        container,
        text="计算器",
        width=20,
        height=2,
        command=lambda: show_calc(root, container),
    ).pack(pady=8)
    tk.Button(
        container,
        text="面积计算",
        width=20,
        height=2,
        command=lambda: show_area(root, container),
    ).pack(pady=8)
    tk.Button(container, text="退出", width=20, height=2, command=root.destroy).pack(
        pady=8
    )


def show_calc(root, container):
    clear_frame(container)
    state = CalcState()

    # 显示区
    expr_var = tk.StringVar()
    result_var = tk.StringVar()

    top_bar = tk.Frame(container)
    top_bar.pack(fill="x", pady=(4, 0))
    tk.Button(top_bar, text="← 返回", command=lambda: show_main(root, container)).pack(
        side="left", padx=4
    )
    mode_lbl = tk.Label(top_bar, text="普通模式")
    mode_lbl.pack(side="right", padx=8)

    entry = tk.Entry(
        container, textvariable=expr_var, font=("Consolas", 16), justify="right"
    )
    entry.pack(fill="x", padx=6, pady=(6, 0))
    tk.Label(
        container, textvariable=result_var, font=("Consolas", 12), anchor="e"
    ).pack(fill="x", padx=8)

    # 按键逻辑
    def append_ch(ch):
        if state.just_eval:
            if ch in "0123456789.(π":
                entry.delete(0, "end")
                result_var.set("")
            else:
                entry.delete(0, "end")
                entry.insert(0, state.result)
            state.just_eval = False
        idx = entry.index("insert")
        entry.insert(idx, ch)
        state.expr = entry.get()

    def clear():
        state.expr = ""
        state.result = ""
        state.just_eval = False
        entry.delete(0, "end")
        result_var.set("")

    def backspace():
        if state.just_eval:
            state.just_eval = False
        idx = entry.index("insert")
        if idx > 0:
            entry.delete(idx - 1, idx)
        state.expr = entry.get()

    def evaluate():
        state.expr = expr_var.get()
        if not state.expr:
            return
        res = safe_eval(state.expr)
        state.result = res
        result_var.set(f"= {res}")
        push_history(state, f"{state.expr} = {res}")
        state.just_eval = True

    def show_history():
        win = tk.Toplevel(root)
        win.title("历史记录")
        win.geometry("300x340")
        lb = tk.Listbox(win, font=("Consolas", 11))
        lb.pack(fill="both", expand=True, padx=8, pady=8)
        for h in reversed(state.history):
            lb.insert("end", h)

        def use(_=None):
            sel = lb.curselection()
            if sel:
                expr = lb.get(sel[0]).split(" = ")[0]
                state.expr = expr
                state.just_eval = False
                expr_var.set(expr)
                win.destroy()

        lb.bind("<Double-Button-1>", use)
        tk.Button(win, text="使用选中", command=use).pack(pady=4)

    def toggle_mode():
        state.mode = "科学" if state.mode == "普通" else "普通"
        mode_lbl.config(text=f"{state.mode}模式")
        rebuild_buttons()

    # # 按键表: (text_A, text_B, action_A, action_B)
    LAYOUT = [
        [
            ("M" , "M"  , toggle_mode            , toggle_mode            , "#FFC6A0"),
            ("C" , "C"  , clear                  , clear                  , "#FDB3B3"),
            ("H" , "H"  , show_history           , show_history           , "#DCFFA0"),
            ("+" , "+"  , lambda: append_ch("+") , lambda: append_ch("+") , "#A4C5FF"),
        ],
        [
            ("7" , "sin", lambda: append_ch("7"), lambda: append_ch("sin(") , "#FFC6A0"),
            ("8" , "cos", lambda: append_ch("8"), lambda: append_ch("cos(") , "#FFC6A0"),
            ("9" , "tan", lambda: append_ch("9"), lambda: append_ch("tan(") , "#FFC6A0"),
            ("-" , "-"  , lambda: append_ch("-"), lambda: append_ch("-")    , "#A4C5FF"),
        ],
        [
            # ("4" , "n!" , lambda: append_ch("4"), lambda: append_ch("factorial(")),
            ("4" , "n!" , lambda: append_ch("4"), lambda: append_ch("!")    , "#FFC6A0"),
            ("5" , "√x" , lambda: append_ch("5"), lambda: append_ch("sqrt("), "#FFC6A0"),
            ("6" , "yˣ" , lambda: append_ch("6"), lambda: append_ch("^")    , "#FFC6A0"),
            ("×" , "×"  , lambda: append_ch("×"), lambda: append_ch("×")    , "#A4C5FF"),
        ],
        [
            ("1" , "π"  , lambda: append_ch("1"), lambda: append_ch("π")    , "#FFC6A0"),
            ("2" , "ln" , lambda: append_ch("2"), lambda: append_ch("ln(")  , "#FFC6A0"),
            ("3" , "eˣ" , lambda: append_ch("3"), lambda: append_ch("exp(") , "#FFC6A0"),
            ("÷" , "÷"  , lambda: append_ch("÷"), lambda: append_ch("÷")    , "#A4C5FF"),
        ],
        [
            ("0" , "("  , lambda: append_ch("0"), lambda: append_ch("(")    , "#FFC6A0"),
            ("." , ")"  , lambda: append_ch("."), lambda: append_ch(")")    , "#FFC6A0"),
            ("⌫", "⌫" , backspace             , backspace                 , "#FDB3B3"),
            ("=" , "="  , evaluate              , evaluate                  , "#A4C5FF"),
        ],
    ]

    btn_frame = tk.Frame(container)
    btn_frame.pack(pady=4)
    btn_refs = []  # list of (tk.Button, tA, tB, aA, aB, bgc)

    def rebuild_buttons():
        for b, tA, tB, aA, aB in btn_refs:
            if state.mode == "普通":
                b.config(text=tA, command=aA)
            else:
                b.config(text=tB, command=aB)

    for r, row in enumerate(LAYOUT):
        row_refs = []
        for c, (tA, tB, aA, aB, bgc) in enumerate(row):
            b = tk.Button(
                btn_frame, text=tA, command=aA, width=5, height=2, bg=bgc, font=("Consolas", 11)
            )
            b.grid(row=r, column=c, padx=2, pady=2)
            row_refs.append((b, tA, tB, aA, aB))
        btn_refs.extend(row_refs)

    def on_key(event):
        k = event.keysym
        if k == "Return":
            evaluate()
        elif k == "BackSpace":
            backspace()
        elif k == "Escape":
            clear()
        elif event.char in "0123456789.+-*/()^":
            ch = event.char.replace("*", "×").replace("/", "÷")
            append_ch(ch)
        else:
            return  # 其他键（方向键、Ctrl等）不拦截
        return "break"  # 阻止 Entry 再处理一次

    # 绑定到 entry，"break" 才能在默认输入前生效
    entry.bind("<Key>", on_key)


def show_area(root, container):
    root.unbind("<Key>")
    clear_frame(container)
    tk.Button(
        container, text="← 返回", command=lambda: show_main(root, container)
    ).pack(anchor="w", padx=6, pady=4)
    tk.Label(container, text="面积计算", font=("", 14, "bold")).pack(pady=(20, 10))
    tk.Button(
        container,
        text="矩形",
        width=20,
        height=2,
        command=lambda: show_rect(root, container),
    ).pack(pady=8)
    tk.Button(
        container,
        text="圆形",
        width=20,
        height=2,
        command=lambda: show_circ(root, container),
    ).pack(pady=8)


def show_rect(root, container):
    clear_frame(container)
    tk.Button(
        container, text="← 返回", command=lambda: show_area(root, container)
    ).pack(anchor="w", padx=6, pady=4)
    tk.Label(container, text="矩形面积", font=("", 13, "bold")).pack(pady=(10, 6))
    f = tk.Frame(container)
    f.pack()
    tk.Label(f, text="长:").grid(row=0, column=0, sticky="e", pady=4)
    rect_l = tk.Entry(f, width=12)
    rect_l.grid(row=0, column=1, padx=6)
    tk.Label(f, text="宽:").grid(row=1, column=0, sticky="e", pady=4)
    rect_w = tk.Entry(f, width=12)
    rect_w.grid(row=1, column=1, padx=6)
    res = tk.Label(container, text="面积: ——", font=("", 12))
    res.pack(pady=8)

    def calc():
        try:
            res.config(
                text=f"面积: {round(float(rect_l.get()) * float(rect_w.get()), 6)}"
            )
        except ValueError:
            res.config(text="面积: 请输入有效数值")

    tk.Button(container, text="计算", width=10, command=calc).pack()


def show_circ(root, container):
    clear_frame(container)
    tk.Button(
        container, text="← 返回", command=lambda: show_area(root, container)
    ).pack(anchor="w", padx=6, pady=4)
    tk.Label(container, text="圆形面积", font=("", 13, "bold")).pack(pady=(10, 6))
    f = tk.Frame(container)
    f.pack()
    tk.Label(f, text="半径:").grid(row=0, column=0, sticky="e", pady=4)
    circ_r = tk.Entry(f, width=12)
    circ_r.grid(row=0, column=1, padx=6)
    res = tk.Label(container, text="面积: ——", font=("", 12))
    res.pack(pady=8)

    def calc():
        try:
            res.config(text=f"面积: {round(pi * float(circ_r.get()) ** 2, 6)}")
        except ValueError:
            res.config(text="面积: 请输入有效数值")

    tk.Button(container, text="计算", width=10, command=calc).pack()


def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()


def main():
    root = tk.Tk()
    root.title("计算器")
    root.geometry("320x460")
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    show_main(root, container)
    root.mainloop()


if __name__ == "__main__":
    main()
