import json
import os
from datetime import datetime
from loguru import logger

class SimpleMemory:
    def __init__(self):
        self.memory_file = "maya_data/memories/memory.json"
        self.memories = self.load_memories()

    def load_memories(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return {"conversations": [], "facts": []}

    def save_memories(self):
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.memories, f, indent=2)

    def remember_conversation(self, user_input, maya_response):
        self.memories["conversations"].append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "maya": maya_response
        })
        # Keep only last 100 conversations (free tier limit)
        self.memories["conversations"] = self.memories["conversations"][-100:]
        self.save_memories()
        logger.info(f"Remembered conversation")

    def add_fact(self, fact):
        self.memories["facts"].append({
            "timestamp": datetime.now().isoformat(),
            "fact": fact
        })
        self.save_memories()

    def recall_recent(self, count=5):
        return self.memories["conversations"][-count:]
