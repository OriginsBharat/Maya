from loguru import logger
import subprocess
import os

class OBSController:
    def __init__(self):
        self.obs_running = False
        logger.info("🎬 OBS Controller initialized")

    def check_obs(self):
        """Check if OBS is available"""
        try:
            # Try to find OBS
            result = subprocess.run(["which", "obs"], capture_output=True, text=True)
            if result.returncode == 0:
                logger.success("✅ OBS found")
                return True
        except:
            pass

        logger.warning("⚠️ OBS not found - recording disabled")
        return False

    def start_recording(self, filename="recording"):
        """Start recording (mock for now)"""
        output_path = f"maya_data/content/recordings/{filename}.mp4"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # In reality, this would control OBS
        # For now, create a mock file
        with open(output_path, 'wb') as f:
            f.write(b"MOCK_VIDEO_START")

        logger.info(f"🔴 Recording started: {output_path}")
        return output_path

    def stop_recording(self):
        """Stop recording"""
        logger.info("⏹️ Recording stopped")
        return True
