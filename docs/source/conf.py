import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))
project = "my-arithmetic-julien"
author = "julien"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
napoleon_google_docstring = False
napoleon_numpy_docstring = True
html_theme = "sphinx_rtd_theme"
