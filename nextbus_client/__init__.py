"""
Inititalization details for the nextbus_client package

Author: Adam Duston
License: BSD-3-Clause
"""
from nextbus_client import route_config
from nextbus_client import predictions
from nextbus_client import errors
from .version import __version__
from .client import Client
from .agency import Agency
from .route import Route

__title__ = 'nextbus_client'
__author__ = 'Adam Duston'
__license__ = 'BSD-3-Clause'
