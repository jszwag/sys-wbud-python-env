import re
import time
import ctypes
import struct
import logging
from typing import Any, Tuple, Callable, Optional

from ..common import ipv4, check_error, load_library
from ..types import SrvEvent, LocalPort, cpu_statuses, server_statuses
from ..types import longword, wordlen_to_ctypes, WordLen, S7Object
from ..types import srvAreaDB, srvAreaPA, srvAreaTM, srvAreaCT

logger = logging.getLogger(__name__)


def error_wrap(func):
    """Parses a s7 error code returned the decorated function."""
    def f(*args, **kw):
        code = func(*args, **kw)
        check_error(code, context="server")

    return f