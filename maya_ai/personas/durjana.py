from loguru import logger

class Durjana:
    def __init__(self):
        self.name = "Durjana"
        self.load_personality()

    def load_personality(self):
        with open("maya_data/personas/durjana.txt", 'r') as f:
            self.personality = f.read()

    def get_prompt(self, user_input):
        return f"""
        {self.personality}

        User said: {user_input}

        Respond as Durjana - be chaotic, edgy, and entertaining.
        Use slang, be sarcastic, roast if needed.
        """

    def process_response(self, response):
        # Add chaos
        import random
        chaos = ["lmao", "bruh", "no cap", "fr fr"]
        return response + f" {random.choice(chaos)}"
