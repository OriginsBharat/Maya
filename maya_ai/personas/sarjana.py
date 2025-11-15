from loguru import logger

class Sarjana:
    def __init__(self):
        self.name = "Sarjana"
        self.load_personality()

    def load_personality(self):
        with open("maya_data/personas/sarjana.txt", 'r') as f:
            self.personality = f.read()

    def get_prompt(self, user_input):
        return f"""
        {self.personality}

        User said: {user_input}

        Respond as Sarjana - be calm, wise, and educational.
        """

    def process_response(self, response):
        # Add personality-specific modifications
        return response.replace("I think", "In my wisdom, I believe")
