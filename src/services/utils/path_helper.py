"""
Path handling utilities
"""
import os
import sys

def get_app_dir() -> str:
    """Get the application directory path"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))