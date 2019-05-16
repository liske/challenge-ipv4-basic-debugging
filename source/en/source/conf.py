
import os, sys;
sys.path.insert(0, os.path.dirname(os.path.realpath("..")))

from conf import *

project = 'IPv4 Basic Debugging Challenge'

language = 'en'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ChallengeIPv4BasicDebuggingEN.tex', project, author, 'howto'),
]

# Bibliographic Dublin Core info.
epub_title = project
