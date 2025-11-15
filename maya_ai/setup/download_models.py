#!/usr/bin/env python
import os
import requests
from loguru import logger

def download_file(url, path):
    """Download a file with progress"""
    logger.info(f"Downloading {path}...")
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'wb') as file:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"\rProgress: {percent:.1f}%", end='')

        print()  # New line after progress
        logger.success(f"✅ Downloaded {path}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to download {path}: {e}")
        return False

def setup_index_tts():
    """Download Index TTS models if not present"""
    model_dir = "vendor/index-tts/checkpoints"

    files_needed = {
        "config.yaml": "https://huggingface.co/X-LANCE/Index-1.9B-v2/resolve/main/config.yaml",
        # For now, we'll use a placeholder for the model
        # In production, you'd download the actual model
    }

    for filename, url in files_needed.items():
        path = f"{model_dir}/{filename}"
        if not os.path.exists(path):
            download_file(url, path)
        else:
            logger.info(f"✅ {filename} already exists")

    # Create mock model file for testing
    model_path = f"{model_dir}/pytorch_model.bin"
    if not os.path.exists(model_path):
        logger.warning("⚠️ Creating mock model file for testing")
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, 'wb') as f:
            f.write(b"MOCK_MODEL")  # Placeholder

    logger.success("✅ Index TTS setup complete")

if __name__ == "__main__":
    setup_index_tts()
