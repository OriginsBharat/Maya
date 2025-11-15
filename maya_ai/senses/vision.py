from loguru import logger
import base64
from io import BytesIO

try:
    from PIL import Image, ImageGrab
    import pytesseract
except ImportError:
    logger.warning("PIL or pytesseract not installed - vision limited")
    Image = None
    ImageGrab = None

class Vision:
    def __init__(self):
        self.last_screenshot = None
        logger.info("👁️ Vision system initialized")

    def see_screen(self):
        """Capture what's on screen"""
        if not ImageGrab:
            return "Vision not available - install pillow"

        try:
            screenshot = ImageGrab.grab()
            self.last_screenshot = screenshot

            # Save for reference
            screenshot.save("maya_data/content/last_seen.png")
            logger.info("Captured screen")

            return self.analyze_screenshot(screenshot)
        except Exception as e:
            logger.error(f"Vision error: {e}")
            return None

    def analyze_screenshot(self, image):
        """Basic analysis of what Maya sees"""
        # For now, just get basic info
        width, height = image.size

        # Try to read text if possible
        text = ""
        if pytesseract:
            try:
                text = pytesseract.image_to_string(image)[:500]  # Limit text
            except:
                pass

        return {
            "size": f"{width}x{height}",
            "text_found": text[:200] if text else "No text detected",
            "description": "Screenshot captured successfully"
        }

    def find_meme(self):
        """Check if current screen has a meme"""
        # Simple detection for now
        if self.last_screenshot:
            # Check for common meme indicators
            # This is simplified - we'll improve later
            return "Possible meme detected"
        return "No meme found"
