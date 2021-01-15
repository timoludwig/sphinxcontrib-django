# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "sphinxcontrib-django2"
copyright = "2021"
author = "Timo Ludwig"

# The full version, including alpha/beta/rc tags
release = "0.7"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "sphinx_last_updated_by_git",
    "sphinxcontrib_django2.roles",
]

# Enable cross-references to other documentations
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "django": (
        "https://docs.djangoproject.com/en/stable/",
        "https://docs.djangoproject.com/en/stable/_objects/",
    ),
}

# Warn about all references where the target cannot be found
nitpicky = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "sphinx_rtd_theme"
# The logos shown in the menu bar
html_logo = "images/django-sphinx-logo.png"
# The facivon of the html doc files
html_favicon = "images/favicon.svg"
# Do not include links to the documentation source (.rst files) in build
html_show_sourcelink = False