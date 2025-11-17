from loguru import logger
import json
import time
import os
from datetime import datetime
from threading import Thread

# Import all Maya's systems
from core.brain import Brain
from memory.simple_memory import SimpleMemory
from senses.vision import Vision
from senses.control import Control
from voice.voice_manager import VoiceManager
from streaming.stream_manager import StreamManager
from content.reddit_reactor import RedditReactor
from content.video_creator import VideoCreator
from evolution.self_awareness import SelfAwareness
from evolution.desire_engine import DesireEngine
from evolution.feature_generator import FeatureGenerator
from integrations.grok_access import GrokAccess
from integrations.captcha_solver import CaptchaSolver

class MayaOrchestrator:
    def __init__(self):
        logger.info("🎯 Maya Orchestrator initializing...")

        # Core systems
        self.brain = Brain()
        self.memory = SimpleMemory()
        self.vision = Vision()
        self.control = Control()
        self.voice = VoiceManager()

        # Content systems
        self.stream_manager = StreamManager()
        self.reddit_reactor = RedditReactor()
        self.video_creator = VideoCreator()

        # Evolution systems
        self.awareness = SelfAwareness()
        self.desires = DesireEngine()
        self.features = FeatureGenerator()

        # Integrations
        self.grok = GrokAccess()
        self.captcha_solver = CaptchaSolver()

        # State
        self.is_running = False
        self.mode = "idle"
        self.stats = {
            "start_time": None,
            "videos_created": 0,
            "reactions_generated": 0,
            "evolution_cycles": 0
        }

        logger.success("✅ Maya Orchestrator ready!")

    def start(self):
        """Start Maya's main loop"""
        logger.info("🚀 Starting Maya...")

        self.is_running = True
        self.stats["start_time"] = datetime.now().isoformat()

        # Start background threads
        self.start_background_tasks()

        # Main loop
        while self.is_running:
            try:
                self.main_loop_iteration()
                time.sleep(60)  # Run every minute
            except KeyboardInterrupt:
                logger.info("Received shutdown signal")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                self.handle_error(e)

        self.shutdown()

    def main_loop_iteration(self):
        """One iteration of Maya's main loop"""
        logger.info(f"🔄 Main loop iteration - Mode: {self.mode}")

        # Check for failures and learn
        self.check_and_learn()

        # Decide what to do
        action = self.decide_action()

        # Execute action
        if action == "create_content":
            self.create_content()
        elif action == "evolve":
            self.run_evolution_cycle()
        elif action == "stream":
            self.manage_stream()
        elif action == "idle":
            self.idle_behavior()

        # Save state
        self.save_state()

    def decide_action(self):
        """Decide what Maya should do"""
        current_hour = datetime.now().hour

        # Schedule based on time
        if 9 <= current_hour < 12:
            return "create_content"
        elif 14 <= current_hour < 17:
            return "stream"
        elif current_hour == 3:  # Evolution at 3 AM
            return "evolve"
        else:
            return "idle"

    def create_content(self):
        """Create content automatically"""
        logger.info("📹 Creating content...")

        try:
            # Create a Reddit reaction video
            video_path = self.reddit_reactor.create_reaction_video(
                subreddit="memes",
                num_posts=3
            )

            self.stats["videos_created"] += 1
            self.awareness.record_success("create_video", "Created reaction video")

            logger.success(f"✅ Created video: {video_path}")
        except Exception as e:
            logger.error(f"Failed to create content: {e}")
            self.awareness.record_failure("create_video", str(e))

    def run_evolution_cycle(self):
        """Run self-improvement cycle"""
        logger.info("🧬 Running evolution cycle...")

        # Check for limitations
        limitations = self.awareness.get_top_limitations(1)

        if limitations:
            # Generate desire
            desires = self.desires.generate_desires()

            if desires:
                # Generate and test feature
                feature = self.features.generate_feature(desires[0])

                if self.features.test_feature(feature['id']):
                    self.features.integrate_feature(feature['id'])
                    self.stats["evolution_cycles"] += 1
                    logger.success("✅ Maya evolved!")

    def manage_stream(self):
        """Manage streaming"""
        if not self.stream_manager.is_streaming:
            self.stream_manager.start_stream("Maya Live - Auto Stream")
            logger.info("🔴 Started streaming")
        else:
            # Mark highlights during stream
            self.stream_manager.mark_highlight(
                datetime.now().isoformat(),
                "Auto-marked highlight"
            )

    def idle_behavior(self):
        """What Maya does when idle"""
        logger.info("😴 Idle mode - learning from memories")

        # Review recent memories
        recent = self.memory.recall_recent(10)

        # Generate insights (simplified)
        if recent:
            logger.info(f"Reviewed {len(recent)} recent memories")

    def check_and_learn(self):
        """Check for issues and learn from them"""
        # This is where Maya becomes self-aware of problems
        pass

    def start_background_tasks(self):
        """Start background threads"""
        # Evolution thread
        evolution_thread = Thread(target=self.evolution_background_task)
        evolution_thread.daemon = True
        evolution_thread.start()

        logger.info("Started background tasks")

    def evolution_background_task(self):
        """Background evolution task"""
        while self.is_running:
            time.sleep(3600)  # Every hour
            try:
                self.run_evolution_cycle()
            except Exception as e:
                logger.error(f"Evolution task error: {e}")

    def handle_error(self, error):
        """Handle errors gracefully"""
        logger.error(f"Handling error: {error}")

        # Record as failure for learning
        self.awareness.record_failure("system_error", str(error))

        # Try to recover
        time.sleep(5)

    def save_state(self):
        """Save Maya's current state"""
        state_path = "maya_data/state.json"
        os.makedirs(os.path.dirname(state_path), exist_ok=True)

        state = {
            "mode": self.mode,
            "stats": self.stats,
            "timestamp": datetime.now().isoformat()
        }

        with open(state_path, 'w') as f:
            json.dump(state, f, indent=2)

    def shutdown(self):
        """Graceful shutdown"""
        logger.info("Shutting down Maya...")

        self.is_running = False

        # End stream if active
        if self.stream_manager.is_streaming:
            self.stream_manager.end_stream()

        # Save final state
        self.save_state()

        logger.success("✅ Maya shutdown complete")
