# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Ensure the source tree is on the path so autodoc can import the package.
sys.path.insert(0, os.path.abspath("../src"))

# ---------------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------------
project = "PSGE-II"
copyright = "2024, Jules Demangeot"
author = "Jules Demangeot"
release = "1.2.0-dev"
version = "1.2"

# ---------------------------------------------------------------------------
# General configuration
# ---------------------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# autodoc: document members in source order; include undocumented members
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "member-order": "bysource",
}

# Napoleon settings (NumPy-style docstrings)
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
}

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Base URL for the GitHub Pages project site.
# Required so that CSS/JS assets are resolved correctly from the sub-path
# /PSGE-II/ rather than the root of the GitHub Pages domain.
html_baseurl = "https://julesdemangeot-ship-it.github.io/PSGE-II/"

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

html_context = {
    "display_github": True,
    "github_user": "julesdemangeot-ship-it",
    "github_repo": "PSGE-II",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
