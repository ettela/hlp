import math
import tkinter as tk


def safe_eval(expr: str) -> str:
    expr = expr.strip()
    if not expr:
        return "0"
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed.update({"pi": math.pi, "e": math.e})
    value = eval(expr, {"__builtins__": {}}, allowed)
    return str(value)


def main():
    win = tk.Tk()
    win.title("计算器")
    menubar = tk.Menu(win)

    def open_rectangle():
        rect_win = tk.Toplevel(win)
        rect_win.title("矩形面积计算")
        tk.Label(rect_win, text="宽:").grid(row=0, column=0)
        w_ent = tk.Entry(rect_win)
        w_ent.grid(row=0, column=1)
        tk.Label(rect_win, text="高:").grid(row=1, column=0)
        h_ent = tk.Entry(rect_win)
        h_ent.grid(row=1, column=1)
        tk.Label(rect_win, text="面积:").grid(row=2, column=0)
        res = tk.Entry(rect_win)
        res.grid(row=2, column=1)

        def calc_rect():
            a = float(w_ent.get()) * float(h_ent.get())
            res.delete(0, tk.END)
            res.insert(0, str(f"{a:.4f}"))

        tk.Button(rect_win, text="计算", command=calc_rect).grid(
            row=3, column=0, columnspan=2, pady=4
        )

    def open_circle():
        circle_win = tk.Toplevel(win)
        circle_win.title("圆的面积计算")
        tk.Label(circle_win, text="半径:").grid(row=0, column=0)
        r_ent = tk.Entry(circle_win)
        r_ent.grid(row=0, column=1)
        tk.Label(circle_win, text="面积:").grid(row=1, column=0)
        res = tk.Entry(circle_win)
        res.grid(row=1, column=1)

        def calc_circle():
            r = float(r_ent.get())
            a = math.pi * r * r
            res.delete(0, tk.END)
            res.insert(0, str(f"{a:.4f}"))

        tk.Button(circle_win, text="计算", command=calc_circle).grid(
            row=2, column=0, columnspan=2, pady=4
        )

    func_menu = tk.Menu(menubar, tearoff=0)
    func_menu.add_command(label="矩形面积计算", command=open_rectangle)
    func_menu.add_command(label="圆的面积计算", command=open_circle)
    menubar.add_cascade(label="面积", menu=func_menu)
    menubar.add_command(label="退出", command=win.destroy)
    win.config(menu=menubar)

    ans = tk.Entry(win, width=24, justify="right")
    ans.insert(0, "0")
    ans.grid(row=0, column=0, columnspan=4, padx=6, pady=6)

    ready = False

    def start_new_input() -> None:
        nonlocal ready
        if ready:
            ans.delete(0, tk.END)
            ready = False

    def append(token: str) -> None:
        start_new_input()
        text = ans.get()
        if text == "0" and token not in (".", ")"):
            ans.delete(0, tk.END)
        ans.insert(tk.INSERT, token)

    def clear() -> None:
        ans.delete(0, tk.END)
        ans.insert(0, "0")

    def equals() -> None:
        result = safe_eval(ans.get())
        ans.delete(0, tk.END)
        ans.insert(0, result)
        nonlocal ready
        ready = True

    def on_key(event: tk.Event) -> str | None:
        if event.keysym == "Return":
            equals()
            return "break"
        if event.char and event.char in "0123456789.+-*/()":
            append(event.char)
            return "break"
        if event.keysym == "Escape":
            clear()
            return "break"
        return None

    ans.bind("<KeyPress>", on_key)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("(", 4, 2), ("/", 4, 3),
        ("sin(", 5, 0), ("cos(", 5, 1),  ("tan(", 5, 2),   ("sqrt(", 5, 3),   
        ("^", 6, 0),    ("log(", 6, 1),  ("exp(", 6, 2),   (")", 6, 3),  
        ("C", 7, 0),    ("=", 7, 2),
    ]

    for text, r, c in buttons:
        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = equals
        elif text == "^":
            cmd = lambda t="**": append(t)
        else:
            cmd = lambda t=text: append(t)
        width = 6 if text not in ("C", "=") else 12
        span = 1 if text not in ("C", "=") else 2
        tk.Button(win, text=text, width=width, command=cmd).grid(
            row=r, column=c, columnspan=span, padx=3, pady=3
        )

    win.mainloop()


if __name__ == "__main__":
    main()
