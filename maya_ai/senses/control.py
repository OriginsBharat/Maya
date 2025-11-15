from loguru import logger
import time
import random

try:
    import pyautogui
    pyautogui.FAILSAFE = True  # Safety feature
except ImportError:
    logger.warning("pyautogui not installed - control limited")
    pyautogui = None

class Control:
    def __init__(self):
        logger.info("🖱️ Control system initialized")
        self.safety_on = True

    def move_mouse(self, x, y, human_like=True):
        """Move mouse with human-like motion"""
        if not pyautogui:
            return False

        try:
            if human_like:
                # Add some randomness
                duration = random.uniform(0.5, 1.5)
                pyautogui.moveTo(x, y, duration=duration)
            else:
                pyautogui.moveTo(x, y)

            logger.info(f"Moved mouse to {x}, {y}")
            return True
        except Exception as e:
            logger.error(f"Mouse control error: {e}")
            return False

    def click(self, button='left'):
        """Click mouse button"""
        if not pyautogui:
            return False

        try:
            pyautogui.click(button=button)
            logger.info(f"Clicked {button} button")
            return True
        except Exception as e:
            logger.error(f"Click error: {e}")
            return False

    def type_text(self, text, human_like=True):
        """Type text with human-like speed"""
        if not pyautogui:
            return False

        try:
            if human_like:
                # Type with random delays
                for char in text:
                    pyautogui.write(char)
                    time.sleep(random.uniform(0.05, 0.2))
            else:
                pyautogui.write(text)

            logger.info(f"Typed: {text[:20]}...")
            return True
        except Exception as e:
            logger.error(f"Typing error: {e}")
            return False

    def scroll(self, amount):
        """Scroll the screen"""
        if not pyautogui:
            return False

        try:
            pyautogui.scroll(amount)
            logger.info(f"Scrolled {amount}")
            return True
        except Exception as e:
            logger.error(f"Scroll error: {e}")
            return False
