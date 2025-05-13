# -*- coding: utf-8 -*-
import os

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import  __author__, __author_email__, __license__
from .__version__ import __copyright__

print("=========BT_API_KEY: ", os.getenv("BT_API_KEY"))
print("=========PANEL_ADDRESS: ", os.getenv("PANEL_ADDRESS"))

__all__ = [
    '__title__',
    '__description__',
    '__url__',
    '__version__',
    '__author__',
    '__author_email__',
    '__license__',
    '__copyright__',
]
