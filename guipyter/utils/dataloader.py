# -*- coding: utf-8 -*-
import os
import xlrd
import inspect

# Try to import pandas from pandomics
try:
    from panomics import pandas as pd
except ImportError as err:
    import pandas as pd

from .cli_tools import CLITools
from ..jtkinter import filedialog

class DataLoader(object):
    """Multi-purpose dataloading tools.
    """

    def __init__(self, *args, **kwargs):
        self.file_name = None
        self.raw = None
        self.buffer = None
        self.file_name = ''
        self.file_path = ''
        self.file_ext = ''

        # Sort out the parameters.
        read_table_params = inspect.signature(pd.read_table)
        read_excel_params = inspect.signature(pd.read_excel)
        read_excel_params = set(read_excel_params.parameters.keys())
        read_table_params = set(read_table_params.parameters.keys())
        filedialog_params = set(["defaultextension", "filetypes", "initialdir", "initialfile", "multiple", "parent", "title", "typevariable"])

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

        # filedialog params collected here.
        filedialog_params_final = dict()
        for k,v in kwargs.items():
            if k in filedialog_params:
                filedialog_params_final[k]=v

        # Set the file buffer.
        self.buffer = filedialog.askopenfile(filedialog_params_final)

        # Try to collect the file path.
        try:
            self.file_path = self.buffer.name
        except AttributeError as err:
            print(err.args[0])

        # Try to collect the file name.
        try:
            self.file_name = os.path.split(self.file_path)[-1]
        except Exception as err:
            print(err.args[0])

        # try to collect the file extension.
        try:
            self.file_ext = os.path.splitext(self.file_name)[-1]
        except Exception as err:
            print(err.args[0])

        if self.file_ext == ".xls" or self.file_ext == ".xlsx":
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
