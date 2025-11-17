from loguru import logger
from evolution.self_awareness import SelfAwareness
import json
import os
from datetime import datetime

class DesireEngine:
    def __init__(self):
        self.awareness = SelfAwareness()
        self.desires = []
        self.load_desires()
        logger.info("💭 Desire engine initialized")

    def load_desires(self):
        """Load existing desires"""
        desires_path = "maya_data/evolution/desires.json"
        if os.path.exists(desires_path):
            with open(desires_path, 'r') as f:
                self.desires = json.load(f)

    def generate_desires(self):
        """Generate desires based on limitations"""
        new_desires = []

        # Get top limitations
        limitations = self.awareness.get_top_limitations()

        for limitation in limitations:
            desire = self.create_desire_from_limitation(limitation)
            if desire:
                new_desires.append(desire)

        # Add to desires list
        for desire in new_desires:
            if not self.desire_exists(desire):
                self.desires.append(desire)
                logger.info(f"💫 New desire: {desire['description']}")

        self.save_desires()
        return new_desires

    def create_desire_from_limitation(self, limitation):
        """Create a desire to overcome a limitation"""
        desire = {
            "id": f"desire_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created": datetime.now().isoformat(),
            "limitation": limitation["area"],
            "description": f"I want to be able to {limitation['area']} better",
            "priority": limitation["priority"],
            "status": "pending",
            "proposed_solution": self.propose_solution(limitation)
        }
        return desire

    def propose_solution(self, limitation):
        """Propose a solution for a limitation"""
        solutions = {
            "video": "Add video editing capabilities",
            "memory": "Improve memory system",
            "voice": "Enhance voice synthesis",
            "reaction": "Better reaction generation",
            "understanding": "Improve content understanding"
        }

        # Find matching solution
        for key, solution in solutions.items():
            if key in limitation["area"].lower():
                return solution

        return "Develop new capability"

    def desire_exists(self, new_desire):
        """Check if similar desire already exists"""
        for existing in self.desires:
            if existing["limitation"] == new_desire["limitation"]:
                return True
        return False

    def get_active_desires(self):
        """Get desires that haven't been fulfilled"""
        return [d for d in self.desires if d["status"] == "pending"]

    def mark_desire_fulfilled(self, desire_id):
        """Mark a desire as fulfilled"""
        for desire in self.desires:
            if desire["id"] == desire_id:
                desire["status"] = "fulfilled"
                desire["fulfilled_at"] = datetime.now().isoformat()
                logger.success(f"✅ Desire fulfilled: {desire['description']}")
                break

        self.save_desires()

    def save_desires(self):
        """Save desires to file"""
        desires_path = "maya_data/evolution/desires.json"
        os.makedirs(os.path.dirname(desires_path), exist_ok=True)

        with open(desires_path, 'w') as f:
            json.dump(self.desires, f, indent=2)
