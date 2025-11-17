#!/usr/bin/env python
"""
Maya AI - Autonomous VTuber
Main entry point
"""

import sys
import os
from loguru import logger
from orchestrator import MayaOrchestrator

# Setup logging
logger.remove()  # Remove default handler
logger.add(sys.stderr, level="INFO")
logger.add("maya_data/logs/maya.log", rotation="10 MB", level="DEBUG")

def setup_environment():
    """Setup Maya's environment"""
    logger.info("Setting up environment...")

    # Add vendor to path for Index TTS
    vendor_path = os.path.join(os.path.dirname(__file__), "..", "vendor")
    if os.path.exists(vendor_path):
        sys.path.insert(0, vendor_path)

    # Create necessary directories
    directories = [
        "maya_data/logs",
        "maya_data/memories",
        "maya_data/content",
        "maya_data/evolution",
        "maya_data/cache",
        "voices",
        "vendor/index-tts/checkpoints"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    logger.success("✅ Environment ready")

def check_dependencies():
    """Check if all dependencies are installed"""
    logger.info("Checking dependencies...")

    required = ["requests", "loguru", "pyyaml"]
    missing = []

    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)

    if missing:
        logger.error(f"Missing packages: {missing}")
        logger.info("Run: pip install -r requirements.txt")
        return False

    logger.success("✅ All dependencies installed")
    return True

def main():
    """Main function"""
    print("""
    ╔══════════════════════════════════════╗
    ║           MAYA AI VTUBER             ║
    ║     Autonomous Content Creator       ║
    ╚══════════════════════════════════════╝
    """)

    # Setup
    setup_environment()

    if not check_dependencies():
        sys.exit(1)

    # Download models if needed
    from setup.download_models import setup_index_tts
    logger.info("Checking Index TTS models...")
    setup_index_tts()

    # Start Maya
    maya = MayaOrchestrator()

    try:
        maya.start()
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
    finally:
        maya.shutdown()

if __name__ == "__main__":
    main()
