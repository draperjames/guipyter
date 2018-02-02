# -*- coding: utf-8 -*-
import os
import xlrd
import pandas as pd
from .cli_tools import CLITools
from ..jtkinter import filedialog

class DataLoader(object):
    """
    """

    def __init__(self, **kwargs):
        self.source_file_name = None
        self.raw = None
        self.buffer = filedialog.askopenfile()

        try:
            self.source_file_name = self.buffer.name

        except AttributeError as e:
            print(e.args[0])

        self.source_file_ext = os.path.splitext(self.source_file_name)[-1]

        if self.source_file_ext == ".xls" or self.source_file_ext == ".xlsx":

            try:
                # Excel files are so special that need to be read by a different function.
                # NOTE: Only the first sheet in the file will be read.
                # self.raw = pd.read_excel(self.buffer.name)
                self.raw = read_excel_cli(self.buffer.name, **kwargs)

            except ValueError as e:
                print(e.args[0])

        else:
            try:
                # This should work with everything else.
                self.raw = pd.read_table(self.buffer,**kwargs)

            except ValueError as e:
                print(e.args[0])
        self.buffer.close()

if __name__ == "__main__":
    dl = DataLoader()
