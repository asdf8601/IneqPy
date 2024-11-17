"""IneqPy: A python package for inequality analysis."""

from ineqpy import api, grouped, inequality, statistics, utils
from ineqpy._version import get_versions

__version__ = get_versions()["version"]

del get_versions

__all__ = ["inequality", "statistics", "grouped", "api", "utils"]
