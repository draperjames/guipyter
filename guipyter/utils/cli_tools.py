# -*- coding: utf-8 -*-
import xlrd
import pandas as pd

class CLITools(object):
    """Command Line Interface Tools.
    """
    @staticmethod
    def list_choice_cli(inp, message="Choose from the following:\n"):
        """Return the users selection from a list.

        Parameters
        ----------
        inp : list

        message : string

        Returns
        -------
        result : string
        """
        show = ["{}) {}\n".format(n, i) for n,i in enumerate(inp)]
        show = ''.join(show)
        show = message+show
        print(show)
        selection = int(input())
        result = inp[selection]
        return result

    @classmethod
    def read_excel_cli(cls, file_name, **kwargs):
        """Return a DataFrame from the selected sheet of an Excel file.

        Parameters
        ----------
        file_name : string

        Returns
        -------
        result : DataFrame

        """
        book = xlrd.open_workbook(file_name)
        if book.nsheets > 1:
            selected_sheet = cls.list_choice_cli(book.sheet_names())
            result = pd.read_excel(file_name,
                                   sheet_name=selected_sheet,
                                   **kwargs)
        else:
            result = pd.read_excel(file_name, **kwargs)
        return result
