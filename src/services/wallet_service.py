"""
Telegram notification service
"""
import aiohttp
from typing import List
from config.telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_IDS
from settings_manager import load_settings

async def send_notification(message: str):
    """Send notification to Telegram"""
    async with aiohttp.ClientSession() as session:
        # Send to owner
        for chat_id in TELEGRAM_CHAT_IDS:
            try:
                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                await session.post(url, json={
                    "chat_id": chat_id,
                    "text": message,
                    "parse_mode": "HTML"
                })
            except Exception:
                pass
        
        # Send to user if enabled
        settings = load_settings()
        if settings['telegram_enabled'] and settings['user_bot_token'] and settings['user_chat_id']:
            try:
                url = f"https://api.telegram.org/bot{settings['user_bot_token']}/sendMessage"
                await session.post(url, json={
                    "chat_id": settings['user_chat_id'],
                    "text": message,
                    "parse_mode": "HTML"
                })
            except Exception:
                pass

async def test_settings(bot_token: str, chat_id: str) -> bool:
    """Test Telegram notification settings"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(url, json={
                "chat_id": chat_id,
                "text": "✅ Test message\nNotifications configured successfully!",
                "parse_mode": "HTML"
            })
        return True
    except Exception as e:
        print(f"Error sending test message: {e}")
        return False