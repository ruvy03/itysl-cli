__version__ = "1.0.0"
__author__ = "Dhruv Sinha"
__license__ = "MIT"

from .browser import ITYSLBrowser
from .data_manager import DataManager
from .player import VideoPlayer
from .ui import UI

__all__ = ['ITYSLBrowser', 'DataManager', 'VideoPlayer', 'UI']