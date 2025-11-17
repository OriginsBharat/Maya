from loguru import logger
import json
import os
from datetime import datetime

class SelfAwareness:
    def __init__(self):
        self.failures = []
        self.successes = []
        self.limitations = []
        self.load_awareness_data()
        logger.info("🧠 Self-awareness system initialized")

    def load_awareness_data(self):
        """Load previous awareness data"""
        data_path = "maya_data/evolution/awareness.json"
        if os.path.exists(data_path):
            with open(data_path, 'r') as f:
                data = json.load(f)
                self.failures = data.get("failures", [])
                self.successes = data.get("successes", [])
                self.limitations = data.get("limitations", [])

    def record_failure(self, task, reason):
        """Record when Maya fails at something"""
        failure = {
            "timestamp": datetime.now().isoformat(),
            "task": task,
            "reason": reason
        }
        self.failures.append(failure)

        # Identify pattern
        if self.count_similar_failures(task) >= 3:
            self.identify_limitation(task, reason)

        self.save_awareness_data()
        logger.info(f"📝 Recorded failure: {task} - {reason}")

    def record_success(self, task, details):
        """Record successful actions"""
        success = {
            "timestamp": datetime.now().isoformat(),
            "task": task,
            "details": details
        }
        self.successes.append(success)
        self.save_awareness_data()
        logger.info(f"✅ Recorded success: {task}")

    def identify_limitation(self, task, reason):
        """Identify a consistent limitation"""
        limitation = {
            "identified": datetime.now().isoformat(),
            "area": task,
            "description": f"Consistently failing at {task} due to {reason}",
            "priority": self.calculate_priority(task)
        }

        # Check if already identified
        for existing in self.limitations:
            if existing["area"] == task:
                return

        self.limitations.append(limitation)
        logger.warning(f"⚠️ New limitation identified: {task}")

        return limitation

    def count_similar_failures(self, task):
        """Count failures for similar tasks"""
        count = 0
        for failure in self.failures[-20:]:  # Check last 20 failures
            if task.lower() in failure["task"].lower():
                count += 1
        return count

    def calculate_priority(self, task):
        """Calculate priority for fixing this limitation"""
        failure_count = self.count_similar_failures(task)
        if failure_count >= 5:
            return "high"
        elif failure_count >= 3:
            return "medium"
        else:
            return "low"

    def get_top_limitations(self, count=3):
        """Get the most important limitations to address"""
        sorted_limitations = sorted(
            self.limitations,
            key=lambda x: {"high": 3, "medium": 2, "low": 1}[x["priority"]],
            reverse=True
        )
        return sorted_limitations[:count]

    def save_awareness_data(self):
        """Save awareness data"""
        data_path = "maya_data/evolution/awareness.json"
        os.makedirs(os.path.dirname(data_path), exist_ok=True)

        data = {
            "failures": self.failures[-100:],  # Keep last 100
            "successes": self.successes[-100:],
            "limitations": self.limitations
        }

        with open(data_path, 'w') as f:
            json.dump(data, f, indent=2)
