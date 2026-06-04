import math
import tkinter as tk


def main(win):
    menubar = tk.Menu(win)
    a_menu = tk.Menu(menubar, tearoff=0)

    def open_rw():
        rect_win = tk.Toplevel(win)
        rect_win.title("矩形面积计算")
        rect_win.resizable(False, False)
        for i, text in enumerate(["宽:", "高:"]):
            tk.Label(rect_win, text=text).grid(row=i, column=0, padx=6, pady=4, sticky="e")
        w_e = tk.Entry(rect_win, width=12)
        w_e.grid(row=0, column=1, padx=6)
        h_e = tk.Entry(rect_win, width=12)
        h_e.grid(row=1, column=1, padx=6)
        tk.Label(rect_win, text="面积:").grid(row=2, column=0, padx=6, pady=4, sticky="e")
        res = tk.Entry(rect_win, width=12, state="readonly")
        res.grid(row=2, column=1, padx=6)

        def calc():
            res.config(state="normal")
            res.delete(0, tk.END)
            res.insert(0, f"{float(w_e.get()) * float(h_e.get()):.2f}")
            res.config(state="readonly")

        tk.Button(rect_win, text="计算", width=10, command=calc).grid(
            row=3, column=0, columnspan=2, pady=6
        )

    def open_cw():
        c_win = tk.Toplevel(win)
        c_win.title("圆的面积计算")
        c_win.resizable(False, False)
        tk.Label(c_win, text="半径:").grid(row=0, column=0, padx=6, pady=4, sticky="e")
        r_e = tk.Entry(c_win, width=12)
        r_e.grid(row=0, column=1, padx=6)
        tk.Label(c_win, text="面积:").grid(row=1, column=0, padx=6, pady=4, sticky="e")
        res = tk.Entry(c_win, width=12, state="readonly")
        res.grid(row=1, column=1, padx=6)

        def calc():
            res.config(state="normal")
            res.delete(0, tk.END)
            res.insert(0, f"{math.pi * float(r_e.get()) ** 2:.2f}")
            res.config(state="readonly")

        tk.Button(c_win, text="计算", width=10, command=calc).grid(
            row=2, column=0, columnspan=2, pady=6
        )

    a_menu.add_command(label="矩形面积计算", command=open_rw)
    a_menu.add_command(label="圆的面积计算", command=open_cw)
    menubar.add_cascade(label="面积", menu=a_menu)
    menubar.add_command(label="退出", command=win.destroy)
    win.config(menu=menubar)

    ans = tk.Entry(win, width=26, justify="right", font=("Courier", 14))
    ans.insert(0, "")
    ans.grid(row=0, column=0, columnspan=4, padx=6, pady=8)

    ns = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    expr, ready = "", False

    def dispatch(t):
        nonlocal expr, ready
        match t:
            case "=":
                value = eval(expr.replace("^", "**"), ns)
                expr = (
                    str(int(value))
                    if isinstance(value, float) and value.is_integer()
                    else str(value)
                )
                ready = True
            case "C":
                expr, ready = "", False
            case "<-":
                expr, ready = ("0", False) if ready else (expr[:-1] or "0", False)
            case _ if t in "+-*/^":
                expr = expr + t
            case _:
                base = "" if ready else expr
                expr = (
                    t
                    if base in ("0", "") and t not in (".", ")")
                    else base + t
                )
                ready = False
        ans.delete(0, tk.END)
        ans.insert(0, expr)

    def on_key(event):
        match event.keysym:
            case "Return":
                dispatch("=")
                return "break"
            case "BackSpace":
                dispatch("<-")
                return "break"
            case "Escape":
                dispatch("C")
                return "break"
        if event.char in "0123456789.+-*/()^":
            dispatch(event.char)
            return "break"

    ans.bind("<KeyPress>", on_key)

    buttons = [
        ("7", "7", 1, 0), ("8", "8", 1, 1), ("9", "9", 1, 2), ("+", "+", 1, 3),
        ("4", "4", 2, 0), ("5", "5", 2, 1), ("6", "6", 2, 2), ("-", "-", 2, 3),
        ("1", "1", 3, 0), ("2", "2", 3, 1), ("3", "3", 3, 2), ("*", "*", 3, 3),
        ("0", "0", 4, 0), (".", ".", 4, 1), ("exp(", "exp(",4, 2), ("/", "/", 4, 3),
        ("sin(", "sin(", 5, 0), ("cos(", "cos(", 5, 1), ("tan(", "tan(", 5, 2), ("√(", "sqrt(", 5, 3),
        ("xʸ", "^", 6, 0),      ("log(", "log(", 6, 1), ("(", "(", 6, 2), (")", ")", 6, 3),
        ("<-", "<-", 7, 0),     ("C", "C", 7, 1),       ("=", "=", 7, 2),
    ]

    for label, t, row, col in buttons:
        span = 2 if label == "=" else 1
        tk.Button(
            win, text=label, width=6 * span, command=lambda t=t: dispatch(t), padx=2
        ).grid(row=row, column=col, columnspan=span, padx=3, pady=3)


if __name__ == "__main__":
    win = tk.Tk()
    win.title("计算器")
    win.resizable(False, False)
    main(win)
    win.mainloop()
