"""
molecool
A python package for analysizing and visualizing xyz files
"""

# Add imports here
from .functions import canvas
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_molecular_mass
from .visualize import draw_molecule, bond_histogram
from . import io
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
