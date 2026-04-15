import code
import inspect


def start_repl():
    """
    启动当前脚本下 REPL 环境
    """
    local = inspect.currentframe().f_back.f_locals
    code.interact(local=local)
