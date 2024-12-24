"""
File operations utility
"""
import json
import os

def read_json_file(file_path: str) -> dict:
    """Read and parse a JSON file"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def write_json_file(file_path: str, data: dict) -> None:
    """Write data to a JSON file"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)