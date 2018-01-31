import os
import re
import glob
import subprocess
from IPython.display import Javascript


here = os.getcwd()


def native_cmd(cmd, whitespace=False):
    """Returns the output of a native command on a give system.

    NOTE: Results may contain white space charaters at end of lines.
    """
    result = subprocess.check_output(cmd, shell=True).decode()
    if whitespace:
        return result
    else:
        # Remove carrige returns.
        result = re.sub('\r|\n', '', result, re.X)
        return result

# Javascript for notebook_save.
notebook_save_script = '''
require(["base/js/namespace"],function(Jupyter) {
    Jupyter.notebook.save_checkpoint();
});
'''


def notebook_save():
    Javascript(notebook_save_script)
    print('This notebook has been saved.')


def notebook_current():
    ipynb_list = list(map(lambda x: (x, os.path.getmtime(x)),
                          glob.glob("*.ipynb")))

    ipynb_list.sort(key=lambda x: x[1], reverse=True)
    last_modified = ipynb_list[0][0]
    return last_modified


def nbconvert_wrapper(file_type=None, file_name=None):
    command = "jupyter nbconvert --to {file_type} {file_name}".format(**locals())
    result = native_cmd(command)
    return result


def notebook_current_convert(file_type=None):
    notebook_save()
    result = nbconvert_wrapper(file_type=file_type, file_name=notebook_current())
    if len(result) == 0:
        print("Converted notebook.")
    else:
        print("Failed to convert notebook.")
    return
