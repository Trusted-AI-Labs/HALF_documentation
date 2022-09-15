# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'HALF'
copyright = '2022, TRAIL @ Berlin - P4 Active Learning Framework Team'
author = 'Augustin Delecluse, Axel Abels, Charlotte Nachtegael, Clément Nicolas, Elias Fernandez, Gian Marco Paldino, Lucile Dierckx, Natarajan Chidambaram'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.githubpages' 
]

autosummary_generate = True

autodoc_default_options = {
    'members': True,
    # The ones below should be optional but work nicely together with
    # example_package/autodoctest/doc/source/_templates/autosummary/class.rst
    # and other defaults in sphinx-autodoc.
    'show-inheritance': True,
    'inherited-members': False,
    'no-special-members': True,
}

autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['distil/', 'main', 'benchmark']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
    "sidebar_hide_name": True,
}