# -*- coding: utf-8 -*-
import os

try:
    import tkinter
except ImportError as err:
    print(err)


def conditional_kwargs(**nkwargs):
    """Returns function with conditionally supplied kwargs.

    This decorator is intended for use with higher level functions that
    act more like wrappers for other functions or classes.
    """
    def decorator(some_function):
        def wrapper(nkwargs=nkwargs, *args, **kwargs):
            for k, v in nkwargs.items():
                if k not in kwargs:
                    kwargs[k] = v
                else:
                    pass
            return some_function(*args, **kwargs)
        return wrapper
    return decorator


def root_topmost():
    """Return root as a withdrawn topmost window.
    """
    root = tkinter.Tk()
    # Hide the main window.
    root.withdraw()
    root.call('wm', 'attributes', ".", '-topmost', True)
    return root

def relative_position(root, w=500, h=200):
    w = int(w)
    h = int(h)
    # Width of the screen.
    ws = root.winfo_screenwidth()
    # Height of the screen.
    hs = root.winfo_screenheight()
    x = int((ws / 2) - (w / 2))
    y = int((hs / 2) - (h / 2))
    root.geometry("{:d}x{:d}+{:d}+{:d}".format(w, h, x, y))
