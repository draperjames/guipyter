REM Building python package using twine (https://github.com/pypa/twine).

REM This probably will need to be changed.

set conda_activate="%programfiles%\Miniconda3\Scripts\activate.bat"
call %conda_activate%

REM Cleaning up from last build.
python clean.py

REM Building the package like normal.
python setup.py sdist bdist_wheel

REM Uploading with twine.
twine upload dist/*

timeout 15
