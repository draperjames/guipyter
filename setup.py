"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://github.com/genepattern/genepattern-notebook/blob/master/setup.py
"""
import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop


here = os.getcwd()

with open(os.path.join(here, 'guipyter', '__version__')) as f:
    __version__ = f.read().strip()



def _post_install():
    """After installing the python module enable the nbextensions.

    Inspired by https://github.com/genepattern/genepattern-notebook/blob/master/setup.py.
    """
    import subprocess
    from distutils import log
    log.set_verbosity(log.DEBUG)

    try:
        # Enable the required nbextensions for ipywidgets and nbtools
        subprocess.call(["jupyter", "nbextension", "install", "--user", "--py", "guipyter.fileupload"])
        subprocess.call(["jupyter", "nbextension", "enable", "--user", "--py", "guipyter.fileupload"])
    except:
        log.warn("Unable to automatically enable GenePattern extension for Jupyter.\n" +
                 "Please manually enable the extension by running the following commands:\n" +
                 "jupyter nbextension install --user --py guipyter.fileupload\n" +
                  "jupyter nbextension enable --user --py guipyter.fileupload")

class GuipyterInstall(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, [], msg="Running post install task")


class GuipyterDevelop(_develop):
    def run(self):
        _develop.run(self)
        self.execute(_post_install, [], msg="Running post develop task")


setup(
    name='guipyter',
    version=__version__,
    description="GUI tools for jupyter notebook.",
    # The project's main homepage.
    url='https://github.com/draperjames/guipyter',
    # Author details
    author='James Draper',
    author_email='james.draper@duke.edu',
    # Choose your license
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Jupyter Notebook',
    packages=find_packages(),
    package_data = {'guipyter': ['__version__', 'fileupload/static/*.js'],},
    install_requires=['pandas', 'xlrd'],
    cmdclass={'install': GuipyterInstall, "develop":GuipyterDevelop},

    # entry_points={
    #     'console_scripts': [
    #         'guipyter=guipyter:main'
    #         #'sample=sample:main',
    #     ],
    # },
)
