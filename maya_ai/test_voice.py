#!/usr/bin/env python
from voice.voice_manager import VoiceManager
from core.brain import Brain
from loguru import logger

def test_voice_basic():
    """Test basic voice synthesis"""
    logger.info("Testing basic voice...")
    voice = VoiceManager()

    # Test both personas
    sarjana_audio = voice.speak("Hello, I am Sarjana", persona="sarjana")
    durjana_audio = voice.speak("Yo what's up, I'm Durjana", persona="durjana")

    logger.info(f"Sarjana audio: {sarjana_audio}")
    logger.info(f"Durjana audio: {durjana_audio}")

def test_brain_with_voice():
    """Test brain with voice output"""
    logger.info("Testing brain with voice...")
    brain = Brain()

    # Test with Sarjana
    brain.switch_persona("sarjana")
    result = brain.think_and_speak("What is wisdom?")
    logger.info(f"Sarjana said: {result['text'][:100]}...")

    # Test with Durjana
    brain.switch_persona("durjana")
    result = brain.think_and_speak("What do you think about memes?")
    logger.info(f"Durjana said: {result['text'][:100]}...")

if __name__ == "__main__":
    # First setup Index TTS
    from setup.download_models import setup_index_tts
    setup_index_tts()

    # Then test voice
    test_voice_basic()
    test_brain_with_voice()

    print("✅ Voice test complete!")
