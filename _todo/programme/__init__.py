__rev_id__ = """__init__.py, version 1.0, 30/07/2007"""

import sys
if sys.version_info[:2] != (2, 5):
    print >> sys.stderr, "Sorry, PythonSample requires Python 2.5"
    sys.exit (1)

from PythonSample import *