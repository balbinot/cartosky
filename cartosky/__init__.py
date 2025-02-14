"""
CartoSky
======

Provides utilities for plotting sky maps.
"""
__author__ = 'Alex Drlica-Wagner'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from cartosky.core import *
from cartosky.survey import SurveySkymap,SurveyMcBryde,SurveyOrtho
from cartosky.zoom import DESSkymap, BlissSkymap


import warnings


from packaging import version
from matplotlib import __version__ as mplversion

if version.parse(mplversion) > version.parse("3.6"):
    from matplotlib import MatplotlibDeprecationWarning
else:
    from matplotlib.cbook import MatplotlibDeprecationWarning

warnings.filterwarnings("ignore",category=MatplotlibDeprecationWarning)

