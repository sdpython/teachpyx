# coding: windows-1251
__rev_id__ = """setup.py,v 1.0 16/03/2008"""

import sys
from distutils.core import setup

DESCRIPTION = 'Python Sample'

LONG_DESCRIPTION = \
"This project is a skeleton for a Python library written in C++ under Windows."

CLASSIFIERS = \
[
 'Operating System :: Win32',
 'Programming Language :: C++',
 'License :: none',
 'Development Status :: 0.1',
 'Intended Audience :: Developers',
 'Topic :: Software Development :: Libraries :: Python Modules',
 'Topic :: Python :: Sample'
]

KEYWORDS = 'Python Sample'

setup(name = 'PythonSample',
      version = '0.1',
      author = 'Xavier Duprй',
      author_email = 'webmaster@site.com',
      url = 'http://www.xavierdupre.fr/',
      download_url='http://www.xavierdupre.fr/',    
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      license = 'GNU 2.0',
      platforms = 'Win 32',
      packages = ['PythonSample'],
      keywords = KEYWORDS,
      classifiers = CLASSIFIERS
      )

import distutils.sysconfig as SH
to = SH.get_python_lib () + "/PythonSample"
fr = "PythonSample"

# pour copier des fichiers supplйmentaires lors de l'installation
# python setup.py install
import shutil
import os
li = os.listdir (fr)
for f in li :
    if ".dll" in f or ".exe" in f or ".chm" in f :
        print "copy of file ", f
        shutil.copy (fr + "/" + f, to + "/" + f)