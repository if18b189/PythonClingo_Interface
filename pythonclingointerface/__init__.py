from pip._internal.exceptions import DistributionNotFound

from .clingo_interface import ClingoInterface
from .__version__ import __version__
from pkg_resources import get_distribution(__name__).version

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    #package is not installed
    pass

__all__ = ['ClingoInterface', '__version__']