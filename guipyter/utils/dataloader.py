# -*- coding: utf-8 -*-
import os
import xlrd
import inspect
import pandas as pd
from .cli_tools import CLITools
from ..jtkinter import filedialog

class DataLoader(object):
    """
    """

    def __init__(self, *args, **kwargs):
        self.source_file_name = None
        self.raw = None
        self.buffer = filedialog.askopenfile()

        try:
            self.source_file_name = self.buffer.name

        except AttributeError as e:
            print(e.args[0])
        # Get the file extension.
        self.source_file_ext = os.path.splitext(self.source_file_name)[-1]
        # Sort out the parameters.
        read_table_params = inspect.signature(pd.read_table)
        read_excel_params = inspect.signature(pd.read_excel)
        read_excel_params = set(read_excel_params.parameters.keys())
        read_table_params = set(read_table_params.parameters.keys())
        # pd.read_table params collected here
        read_table_params_final = dict()
        for k,v in kwargs.items():
            if k in read_table_params:
                read_table_params_final[k]=v
        # pd.read_excel params collected here
        read_excel_params_final = dict()
        for k,v in kwargs.items():
            if k in read_excel_params:
                read_excel_params_final[k]=v

        if self.source_file_ext == ".xls" or self.source_file_ext == ".xlsx":

            try:
                # Excel files are so special.
                # The CLI will allow the user to select a page in an excel file.

                self.raw = CLITools.read_excel_cli(self.buffer.name,
                                                   **read_excel_params_final)

            except ValueError as e:
                print(e.args[0])

        else:
            try:
                # This should work with everything else.
                self.raw = pd.read_table(self.buffer,
                                         **read_table_params_final)

            except ValueError as e:
                print(e.args[0])
        self.buffer.close()

if __name__ == "__main__":
    dl = DataLoader()
