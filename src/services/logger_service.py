"""
Logging service for wallet operations
"""
import os
from datetime import datetime
from typing import Dict, Any

class LoggerService:
    def __init__(self, log_path: str):
        self.log_path = log_path
        self._init_log_file()

    def _init_log_file(self):
        """Initialize log file with session header"""
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            f.write(f"=== Starting new session at {datetime.now()} ===\n")

    async def log_wallet(self, wallet_info: Dict[str, Any], balances: Dict[str, float]):
        """Log wallet information and balances"""
        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(f"\nFound at: {datetime.now()}\n")
                f.write(f"Seed Phrase: {wallet_info['phrase']}\n")
                for crypto in ['btc', 'ltc', 'eth', 'bnb']:
                    f.write(f"{crypto.upper()} Address: {wallet_info[crypto]['address']}\n")
                    f.write(f"{crypto.upper()} Private Key: {wallet_info[crypto]['private_key']}\n")
                    f.write(f"{crypto.upper()} Balance: {balances[crypto]}\n")
                f.write("-" * 29 + "\n")
                f.flush()
        except Exception as e:
            print(f"\nError writing to log: {e}")