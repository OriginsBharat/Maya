from loguru import logger
from senses.vision import Vision
from senses.control import Control
import time

class RedditWatcher:
    def __init__(self):
        self.vision = Vision()
        self.control = Control()
        logger.info("🔍 Reddit Watcher initialized")

    def watch_reddit(self, duration=60):
        """Watch Reddit and react to content"""
        logger.info(f"Starting Reddit watch for {duration} seconds")

        reactions = []
        start_time = time.time()

        while time.time() - start_time < duration:
            # See what's on screen
            screen_data = self.vision.see_screen()

            if screen_data:
                # Check for memes
                if "meme" in str(screen_data).lower() or self.vision.find_meme():
                    reaction = self.generate_reaction("meme")
                    reactions.append(reaction)
                    logger.info(f"Reaction: {reaction}")

                # Scroll to next post
                self.control.scroll(-3)  # Scroll down
                time.sleep(2)  # Wait for content to load

        return reactions

    def generate_reaction(self, content_type):
        """Generate a reaction based on content"""
        reactions = {
            "meme": ["LOL", "This is hilarious!", "Bruh moment", "Dead 💀"],
            "news": ["Interesting...", "Big if true", "Need more context"],
            "default": ["Hmm", "I see", "Cool"]
        }

        import random
        return random.choice(reactions.get(content_type, reactions["default"]))
