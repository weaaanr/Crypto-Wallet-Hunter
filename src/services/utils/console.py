"""
Console utilities for handling UI elements
"""
import os
import ctypes
from datetime import datetime

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def init_console():
    """Initialize console settings"""
    if os.name == 'nt':
        kernel32 = ctypes.WinDLL('kernel32')
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def update_window_title(count: int, balance: float = None):
    """Update console window title"""
    try:
        if os.name == 'nt':
            console_handle = ctypes.windll.kernel32.GetConsoleWindow()
            if console_handle:
                title = f"Wallet Hunter | Checked: {count}"
                if balance is not None:
                    title += f" | Found Balance: {balance} BTC"
                ctypes.windll.user32.SetWindowTextW(console_handle, title)
    except:
        pass