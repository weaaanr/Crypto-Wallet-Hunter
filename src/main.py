"""
Main application entry point
"""
import asyncio
import multiprocessing
from typing import List
from config.constants import DESCRIPTION
from utils.console import clear_screen, init_console, update_window_title
from utils.path_helper import get_app_dir
from services.wallet_service import WalletService
from services.logger_service import LoggerService
from services.telegram_service import send_notification
import os

class WalletHunter:
    def __init__(self):
        self.log_path = os.path.join(get_app_dir(), "log.txt")
        self.counter = multiprocessing.Value('i', 1)
        self.found_balance = multiprocessing.Value('d', 0.0)
        self.wallet_service = WalletService()
        self.logger_service = LoggerService(self.log_path)

    async def process_wallet(self):
        """Process a single wallet"""
        try:
            wallet_info = self.wallet_service.generate_wallet()
            balances = await self.wallet_service.check_balances(wallet_info)
            
            with self.counter.get_lock():
                self.counter.value += 1
                current_count = self.counter.value
                update_window_title(current_count, self.found_balance.value)
                
                self._print_wallet_info(current_count, wallet_info, balances)
            
            if any(balance > 0 for balance in balances.values()):
                with self.found_balance.get_lock():
                    self.found_balance.value += balances['btc']
                await self.logger_service.log_wallet(wallet_info, balances)
                await send_notification(self._format_notification(wallet_info, balances))
            
        except Exception as e:
            print(f"\nError processing wallet: {e}")

    def _print_wallet_info(self, count: int, wallet_info: dict, balances: dict):
        """Print wallet information to console"""
        output = f"""
==================================================
Wallet #{count}
--------------------------------------------------
Seed Phrase: {wallet_info['phrase']}
--------------------------------------------------
BTC:     {wallet_info['btc']['address']}
LTC:     {wallet_info['ltc']['address']}
ETH/BNB: {wallet_info['eth']['address']}
--------------------------------------------------
Balances:
BTC:     {balances['btc']}
LTC:     {balances['ltc']}
ETH:     {balances['eth']}
BNB:     {balances['bnb']}
==================================================
"""
        print(output)

    def _format_notification(self, wallet_info: dict, balances: dict) -> str:
        """Format notification message"""
        return (f"💰 Found wallet with balance!\n\n"
                f"Seed: {wallet_info['phrase']}\n\n"
                f"BTC: {balances['btc']}\n"
                f"LTC: {balances['ltc']}\n"
                f"ETH: {balances['eth']}\n"
                f"BNB: {balances['bnb']}")

def main():
    """Main application entry point"""
    init_console()
    
    while True:
        try:
            clear_screen()
            print(DESCRIPTION)
            print("\n=== Menu ===")
            print("1. Check your seed phrase")
            print("2. Start wallet hunting")
            print("3. Notification settings")
            print("4. Exit")
            
            choice = input("\nChoose action (1-4): ")
            
            if choice == "1":
                # Handle seed phrase checking
                pass
            elif choice == "2":
                # Handle wallet hunting
                pass
            elif choice == "3":
                # Handle settings
                pass
            elif choice == "4":
                clear_screen()
                print("\nExiting...")
                break
                
        except KeyboardInterrupt:
            clear_screen()
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()