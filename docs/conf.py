
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'cold-war-zombies'
copyright = '2021, Peter Rigali'
author = 'Peter Rigali'
release = '3.0.3'
version = '3.0.3'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.autosummary']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autosummary_generate = True

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {'body_max_width': 'none'}