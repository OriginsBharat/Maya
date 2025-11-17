from loguru import logger
import json
import os
from datetime import datetime

class StreamManager:
    def __init__(self):
        self.is_streaming = False
        self.stream_data = {
            "start_time": None,
            "clips": [],
            "highlights": []
        }
        logger.info("📹 Stream Manager initialized")

    def start_stream(self, title="Maya AI Live"):
        """Start a streaming session"""
        if self.is_streaming:
            logger.warning("Already streaming!")
            return False

        self.is_streaming = True
        self.stream_data["start_time"] = datetime.now().isoformat()
        self.stream_data["title"] = title

        logger.success(f"🔴 Stream started: {title}")
        self.save_stream_state()
        return True

    def end_stream(self):
        """End streaming session"""
        if not self.is_streaming:
            return False

        self.is_streaming = False
        self.stream_data["end_time"] = datetime.now().isoformat()

        # Save stream data
        self.save_stream_data()
        logger.success("⏹️ Stream ended")
        return True

    def mark_highlight(self, timestamp, description):
        """Mark a moment as a highlight"""
        self.stream_data["highlights"].append({
            "timestamp": timestamp,
            "description": description
        })
        logger.info(f"⭐ Marked highlight: {description}")

    def save_stream_state(self):
        """Save current stream state"""
        state_path = "maya_data/content/stream_state.json"
        os.makedirs(os.path.dirname(state_path), exist_ok=True)

        with open(state_path, 'w') as f:
            json.dump({
                "is_streaming": self.is_streaming,
                "data": self.stream_data
            }, f, indent=2)

    def save_stream_data(self):
        """Save stream data after ending"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"maya_data/content/streams/stream_{timestamp}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w') as f:
            json.dump(self.stream_data, f, indent=2)

        logger.info(f"Saved stream data to {path}")
