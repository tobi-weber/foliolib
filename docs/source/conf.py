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

current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../.."))
sys.path.insert(0, target_dir)

# -- Project information -----------------------------------------------------

project = 'pyokapi'
copyright = '2020, Tobias Weber'
author = 'Tobias Weber'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_copybutton'
]
# Napoleon settings
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
#napoleon_use_ivar = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None
napoleon_custom_sections = ["Headers", "Schema"]

# if True, set typing.TYPE_CHECKING to True to enable "expensive" typing imports
set_type_checking_flag = False
# if True, class names are always fully qualified (e.g. module.for.Class). If False, just the class name displays (e.g. Class)
typehints_fully_qualified = False
# If False, do not add type info for undocumented parameters. If True, add stub documentation for undocumented parameters to be able to add type info.
always_document_param_types = False
# If False, never add an :rtype: directive. If True, add the :rtype: directive if no existing :rtype: is found
typehints_document_rtype = True

# “class”: Only the class’ docstring is inserted. This is the default. You “can still document init as a separate method using automethod or “the members option to autoclass.
# “both”: Both the class’ and the init method’s docstring are concatenated and inserted.
# “init”: Only the init method’s docstring is inserted.
autoclass_content = 'both'

# autodoc_typehints = "description"
autodoc_mock_imports = []

# This value selects if automatically documented members are sorted alphabetical (value 'alphabetical'),
# by member type (value 'groupwise') or by source order (value 'bysource'). The default is alphabetical.
autodoc_member_order = 'bysource',
autodoc_default_options = {'autosummary': True
                           }
autodoc_default_flags = [
    # Make sure that any autodoc declarations show the right members
    "members",
    "inherited-members",
    "private-members",
    "show-inheritance",
]

autosummary_generate = True

#add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# RTD html options
html_show_sourcelink = False
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'style_nav_header_background': 'white',
    # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
}
