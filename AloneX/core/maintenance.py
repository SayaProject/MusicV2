# ALONE-CODER
import asyncio
import os
import sys
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from AloneX import logger, config

def get_next_5am():
    """Calculate time delta to next 5:00 AM"""
    now = datetime.now()
    next_5am = now.replace(hour=5, minute=0, second=0, microsecond=0)
    if next_5am <= now:
        next_5am += timedelta(days=1)
    return (next_5am - now).total_seconds()

async def auto_update():
    """Auto update from git repo at 5:00 AM daily"""
    while True:
        sleep_duration = get_next_5am()
        logger.info(f"Next auto-update in {sleep_duration / 3600:.1f} hours")
        await asyncio.sleep(sleep_duration)
        
        logger.info("Starting daily auto-update at 5:00 AM...")
        
        try:
            # Check if .git exists
            if Path(".git").exists():
                # Fetch latest changes
                subprocess.run(["git", "fetch"], check=True, capture_output=True, text=True)
                # Reset to latest
                result = subprocess.run(["git", "reset", "--hard", "origin/main"], check=True, capture_output=True, text=True)
                logger.info(f"Git reset result: {result.stdout}")
                
                # Pull changes
                pull_result = subprocess.run(["git", "pull", "origin", "main"], check=True, capture_output=True, text=True)
                logger.info(f"Git pull result: {pull_result.stdout}")
                
                logger.info("Auto-update completed! Restarting...")
                os.execl(sys.executable, sys.executable, "-m", "AloneX")
            else:
                logger.info("Not a git repository, skipping auto-update")
        except Exception as e:
            logger.error(f"Error during auto-update: {e}")

async def auto_maintenance():
    """Clear cache and restart every 7 days at 5:00 AM"""
    days_count = 0
    
    while True:
        sleep_duration = get_next_5am()
        logger.info(f"Next maintenance check in {sleep_duration / 3600:.1f} hours")
        await asyncio.sleep(sleep_duration)
        
        days_count += 1
        logger.info(f"Day {days_count} since last maintenance")
        
        if days_count >= 7:
            logger.info("Starting scheduled 7-day maintenance at 5:00 AM...")
            
            # 1. Clear Local Cache & Downloads
            for directory in ["cache", "downloads"]:
                dir_path = Path(directory)
                if dir_path.exists():
                    for item in dir_path.iterdir():
                        try:
                            if item.is_file():
                                item.unlink()
                            elif item.is_dir():
                                shutil.rmtree(item)
                        except Exception as e:
                            logger.error(f"Error clearing {item}: {e}")
            
            logger.info("Local cache and downloads cleared.")
            
            # 2. Restart the bot
            days_count = 0
            logger.info("Scheduled restart initiated...")
            os.execl(sys.executable, sys.executable, "-m", "AloneX")
