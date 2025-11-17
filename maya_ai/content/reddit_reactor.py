from loguru import logger
from senses.vision import Vision
from senses.control import Control
from voice.voice_manager import VoiceManager
from streaming.obs_controller import OBSController
from content.video_creator import VideoCreator
import time

class RedditReactor:
    def __init__(self):
        self.vision = Vision()
        self.control = Control()
        self.voice = VoiceManager()
        self.obs = OBSController()
        self.video_creator = VideoCreator()
        logger.info("🎭 Reddit Reactor initialized")

    def create_reaction_video(self, subreddit="memes", num_posts=5):
        """Create a Reddit reaction video"""
        logger.info(f"Creating reaction video for r/{subreddit}")

        # Start recording
        recording_path = self.obs.start_recording(f"reddit_{subreddit}")

        reactions = []
        reaction_data = {
            "subreddit": subreddit,
            "posts": []
        }

        for i in range(num_posts):
            logger.info(f"Reacting to post {i+1}/{num_posts}")

            # Capture screen
            screen = self.vision.see_screen()

            # Generate reaction
            reaction = self.generate_reaction(screen)
            reactions.append(reaction)

            # Speak reaction
            audio_path = self.voice.speak(reaction["text"], reaction["persona"])

            # Save reaction data
            reaction_data["posts"].append({
                "post_number": i+1,
                "reaction": reaction,
                "audio": audio_path
            })

            # Scroll to next post
            self.control.scroll(-5)
            time.sleep(2)

        # Stop recording
        self.obs.stop_recording()

        # Create final video
        video_path = self.video_creator.create_video("reddit_reaction", reaction_data)

        logger.success(f"✅ Created reaction video: {video_path}")
        return video_path

    def generate_reaction(self, screen_data):
        """Generate reaction based on what Maya sees"""
        import random

        # Decide which persona reacts
        persona = random.choice(["sarjana", "durjana"])

        if persona == "sarjana":
            reactions = [
                "This is quite interesting from an educational perspective",
                "Let me explain why this is funny",
                "The wisdom in this meme is profound"
            ]
        else:  # durjana
            reactions = [
                "BRUH this is too funny lmaooo",
                "No cap this slaps fr fr",
                "I'm dead 💀 this is chaos"
            ]

        return {
            "persona": persona,
            "text": random.choice(reactions),
            "timestamp": time.time()
        }
