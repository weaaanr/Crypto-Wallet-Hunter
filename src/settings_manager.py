"""
Settings manager module
"""
from config.default_settings import DEFAULT_SETTINGS
from utils.file_handler import read_json_file, write_json_file

SETTINGS_FILE = 'user_settings.json'

def load_settings() -> dict:
    """Load user settings, falling back to defaults if necessary"""
    user_settings = read_json_file(SETTINGS_FILE)
    return user_settings if user_settings else DEFAULT_SETTINGS

def save_settings(settings: dict) -> None:
    """Save user settings to file"""
    write_json_file(SETTINGS_FILE, settings)