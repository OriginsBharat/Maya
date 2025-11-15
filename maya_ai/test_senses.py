#!/usr/bin/env python
from senses.vision import Vision
from senses.control import Control
from content.reddit_watcher import RedditWatcher
from loguru import logger

def test_vision():
    logger.info("Testing Maya's vision...")
    vision = Vision()
    result = vision.see_screen()
    logger.info(f"Maya sees: {result}")

def test_control():
    logger.info("Testing Maya's control...")
    control = Control()
    # Just move mouse slightly
    control.move_mouse(500, 500)

def test_reddit():
    logger.info("Testing Reddit watcher...")
    watcher = RedditWatcher()
    # Watch for just 10 seconds
    reactions = watcher.watch_reddit(duration=10)
    logger.info(f"Generated {len(reactions)} reactions")

if __name__ == "__main__":
    print("🧪 Testing Maya's senses...")
    test_vision()
    test_control()
    test_reddit()
    print("✅ Senses test complete!")
