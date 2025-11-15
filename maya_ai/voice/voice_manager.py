from loguru import logger
from voice.index_tts_setup import IndexTTSWrapper
import os
import json

class VoiceManager:
    def __init__(self):
        self.tts = IndexTTSWrapper()
        self.voice_refs = self.load_voice_references()
        self.speech_history = []
        logger.info("🎤 Voice Manager initialized")

    def load_voice_references(self):
        """Load voice reference files"""
        refs = {
            "sarjana": "voices/sarjana_ref.wav",
            "durjana": "voices/durjana_ref.wav"
        }

        # Create mock references if they don't exist
        for name, path in refs.items():
            if not os.path.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'wb') as f:
                    f.write(b"MOCK_VOICE_REF")
                logger.info(f"Created mock voice reference: {path}")

        return refs

    def speak(self, text, persona="sarjana", emotion="neutral"):
        """Make Maya speak with the given persona's voice"""
        logger.info(f"🗣️ {persona} speaking: {text[:50]}...")

        # Get voice reference
        voice_ref = self.voice_refs.get(persona, self.voice_refs["sarjana"])

        # Synthesize speech
        audio_path = self.tts.synthesize(text, voice_ref, emotion)

        # Save to history
        self.speech_history.append({
            "text": text,
            "persona": persona,
            "emotion": emotion,
            "audio_path": audio_path
        })

        # Keep only last 50 speeches
        self.speech_history = self.speech_history[-50:]

        return audio_path

    def save_speech_history(self):
        """Save speech history to file"""
        history_path = "maya_data/content/speech_history.json"
        os.makedirs(os.path.dirname(history_path), exist_ok=True)

        with open(history_path, 'w') as f:
            json.dump(self.speech_history, f, indent=2)

        logger.info(f"Saved {len(self.speech_history)} speech entries")
