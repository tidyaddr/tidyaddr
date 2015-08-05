__author__ = 'Evan Mahone'
from distutils.core import setup
import py2exe, sys, os

setup(windows=["tidycsv/tidyaddr.py"],
      options = {'py2exe':{'packages': ['tidycsv']}}
)