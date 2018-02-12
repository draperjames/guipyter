from guipyter.jtkinter.tools import ComparisonSelector
from guipyter.jtkinter.base import root_topmost
from guipyter import filedialog

# root = root_topmost()
# cs = ComparisonSelector(numerator=['one','two'], denominator=['three', 'four'])
# cs.root.mainloop()

def comparison(numerator=None, denominator=None):
    cs = ComparisonSelector(numerator=numerator, denominator=denominator)
    cs.root.mainloop()
    return

comparison(numerator=['one','two'], denominator=['three', 'four'])
# filedialog.askdirectory()
