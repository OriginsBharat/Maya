from loguru import logger
import requests
from memory.simple_memory import SimpleMemory
from personas.sarjana import Sarjana
from personas.durjana import Durjana

class Brain:
    def __init__(self):
        logger.info("Brain initializing...")
        self.model = "llama2:7b"
        self.api_url = "http://localhost:11434/api/generate"
        self.memory = SimpleMemory()
        self.sarjana = Sarjana()
        self.durjana = Durjana()
        self.current_persona = self.sarjana

    def switch_persona(self, persona_name):
        if persona_name.lower() == "durjana":
            self.current_persona = self.durjana
        else:
            self.current_persona = self.sarjana
        logger.info(f"Switched to {self.current_persona.name}")

    def think(self, prompt):
        try:
            # Get persona-specific prompt
            full_prompt = self.current_persona.get_prompt(prompt)

            response = requests.post(self.api_url, json={
                "model": self.model,
                "prompt": full_prompt
            })

            result = response.json()["response"]
            result = self.current_persona.process_response(result)

            # Remember the conversation
            self.memory.remember_conversation(prompt, result)

            return result
        except Exception as e:
            logger.error(f"Brain error: {e}")
            return "I'm having trouble thinking right now..."
