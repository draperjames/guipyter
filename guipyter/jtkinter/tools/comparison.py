# -*- coding: utf-8 -*-

try:
    import tkinter
    from tkinter import ttk
except ImportError as err:
    print(err)

from ..base import root_topmost, relative_position, conditional_kwargs


class ComparisonSelector(object):

    def __init__(self, root=None, numerator=None, denominator=None, title=None):
        self.root = root or tkinter.Tk()
        relative_position(self.root)

        self.root.grid_columnconfigure(0, weight=1)

        self.root.grid_rowconfigure(0, weight=1)

        self._title = title or "Comparison"

        self._numerator = numerator or list()

        self._denominator = denominator or list()

        self.main_frame = ttk.Frame(self.root)

        self.main_frame.grid(column=0, row=0)

        self.title_frame = ttk.Frame(self.main_frame)

        self.title_frame.grid(column=0, row=0)

        self.title = ttk.Label(self.title_frame, text=self._title)

        self.title.grid(column=0, row=0, pady=10)

        self.numerator_frame()

        self.denominator_frame()

        self.select_button()

    def numerator_frame(self):
        num_frame = ttk.Frame(self.main_frame)
        num_frame.grid(column=0, row=1, pady=5)

        num_label = ttk.Label(num_frame, text="Numerator:")
        # num_label.pack(side="left")
        num_label.grid(column=0, row=1, pady=5)
        self.num_combobox = ttk.Combobox(num_frame, values=self._numerator)
        # self.num_combobox.pack(side="left")
        self.num_combobox.grid(column=1, row=1, pady=5)

    def denominator_frame(self):
        den_frame = ttk.Frame(self.main_frame)
        den_frame.grid(column=0, row=2, pady=5)

        den_label = ttk.Label(den_frame, text="Denominator:")
        # den_label.pack(side="left")
        den_label.grid(column=0, row=2, pady=5)
        self.den_combobox = ttk.Combobox(den_frame, values=self._denominator)
        # self.den_combobox.pack(side="left")
        self.den_combobox.grid(column=1, row=2, pady=5)

    def select_button(self):
        self._button = ttk.Button(self.main_frame)
        self._button['text'] = "Select"
        self._button["command"] = self.select_cmd
        self._button.grid(column=3, row=3, pady=5)

    def select_cmd(self, event=None):
        """set the Style to the content of the Combobox"""
        numerator = self.num_combobox.get()
        denominator = self.den_combobox.get()
        self.root.quit()
        print(numerator, denominator)
        return numerator, denominator


# if __name__ == "__main__":
#     import string
#
#     def rand_characters(n, chars):
#         return ''.join([random.choice(chars) for i in range(n)])
#
#     def rand_char_list(members, char_len, chars):
#         return [rand_characters(char_len, chars) for i in range(members)]
#
#     rand_list = rand_char_list(10, 10, string.ascii_uppercase)
#
#     root = root_topmost()
#     content = ComparisonSelector(root, rand_list, randlist)
