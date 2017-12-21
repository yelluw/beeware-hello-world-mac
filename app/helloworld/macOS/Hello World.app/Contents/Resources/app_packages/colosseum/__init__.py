# Core capabilities
from .constants import (
    AUTO, FLEX_START, CENTER, FLEX_END,
    STRETCH, SPACE_BETWEEN, SPACE_AROUND,

    RELATIVE, ABSOLUTE,

    NOWRAP, WRAP,

    ROW, COLUMN,
)
from .engine import Layout
from .declaration import CSS
# from .utils import *

__all__ = [
    '__version__',
    'CSS',
    'Layout',

    'AUTO',
    'FLEX_START',
    'CENTER',
    'FLEX_END',
    'STRETCH',
    'SPACE_BETWEEN',
    'SPACE_AROUND',

    'RELATIVE',
    'ABSOLUTE',

    'NOWRAP',
    'WRAP',

    'ROW',
    'COLUMN',
]

# Examples of valid version strings
# __version__ = '1.2.3.dev1'  # Development release 1
# __version__ = '1.2.3a1'     # Alpha Release 1
# __version__ = '1.2.3b1'     # Beta Release 1
# __version__ = '1.2.3rc1'    # RC Release 1
# __version__ = '1.2.3'       # Final Release
# __version__ = '1.2.3.post1' # Post Release 1

__version__ = '0.1.6'
