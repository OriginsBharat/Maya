from loguru import logger
import requests

class Brain:
    def __init__(self):
        logger.info("Brain initializing...")
        self.model = "llama2:7b"
        self.api_url = "http://localhost:11434/api/generate"

    def think(self, prompt):
        try:
            response = requests.post(self.api_url, json={
                "model": self.model,
                "prompt": prompt
            })
            return response.json()["response"]
        except Exception as e:
            logger.error(f"Brain error: {e}")
            return "I'm having trouble thinking right now..."
