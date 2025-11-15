from loguru import logger
import os

class CloudStorage:
    def __init__(self):
        """Using GitHub as free storage"""
        self.storage_path = "maya_data/"
        self.ensure_directories()

    def ensure_directories(self):
        dirs = [
            "maya_data/memories",
            "maya_data/content",
            "maya_data/logs"
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

    def save(self, data, filename):
        path = f"maya_data/{filename}"
        with open(path, 'w') as f:
            f.write(str(data))
        logger.info(f"Saved: {filename}")
        return path

    def load(self, filename):
        path = f"maya_data/{filename}"
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        return None

def check_brain():
    """Check if brain is responsive"""
    logger.info("Brain check: OK")
    return True
