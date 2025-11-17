from loguru import logger
import json
import os
import time
import hashlib

class GrokAccess:
    def __init__(self):
        self.cache = {}
        self.cache_file = "maya_data/cache/grok_cache.json"
        self.load_cache()
        self.access_methods = [
            self.method_cache,      # Check cache first
            self.method_local,      # Use local LLM
            self.method_mock       # Mock response for testing
        ]
        logger.info("🤖 Grok access system initialized")

    def load_cache(self):
        """Load cached responses"""
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                self.cache = json.load(f)

    def save_cache(self):
        """Save cache to file"""
        os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)

    def query(self, prompt):
        """Query Grok using multiple methods"""
        for method in self.access_methods:
            try:
                response = method(prompt)
                if response:
                    return response
            except Exception as e:
                logger.warning(f"Method failed: {e}")
                continue

        return "Unable to get response at this time"

    def method_cache(self, prompt):
        """Check if we have a cached response"""
        # Create hash of prompt for cache key
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()

        if prompt_hash in self.cache:
            logger.info("💾 Using cached response")
            return self.cache[prompt_hash]["response"]

        # Check for similar prompts
        for key, value in self.cache.items():
            if self.is_similar(prompt, value.get("prompt", "")):
                logger.info("💾 Using similar cached response")
                return value["response"]

        return None

    def method_local(self, prompt):
        """Use local LLM as fallback"""
        logger.info("🏠 Using local LLM fallback")

        # In production, this would call Ollama
        # For now, return a mock response
        response = f"[Local Response] Processed: {prompt[:50]}..."

        # Cache the response
        self.add_to_cache(prompt, response)

        return response

    def method_mock(self, prompt):
        """Mock response for testing"""
        logger.info("🎭 Using mock response")

        responses = {
            "meme": "This meme is absolutely hilarious! It perfectly captures the absurdity of modern life.",
            "code": "Here's an elegant solution using advanced algorithms.",
            "default": "That's an interesting perspective. Let me think about it."
        }

        # Determine response type
        response_type = "default"
        if "meme" in prompt.lower():
            response_type = "meme"
        elif "code" in prompt.lower():
            response_type = "code"

        response = responses[response_type]
        self.add_to_cache(prompt, response)

        return response

    def is_similar(self, prompt1, prompt2):
        """Check if two prompts are similar"""
        # Simple similarity check
        words1 = set(prompt1.lower().split())
        words2 = set(prompt2.lower().split())

        if not words2:
            return False

        similarity = len(words1.intersection(words2)) / len(words2)
        return similarity > 0.7

    def add_to_cache(self, prompt, response):
        """Add response to cache"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()

        self.cache[prompt_hash] = {
            "prompt": prompt,
            "response": response,
            "timestamp": time.time()
        }

        # Keep cache size limited
        if len(self.cache) > 1000:
            # Remove oldest entries
            sorted_items = sorted(self.cache.items(),
                                key=lambda x: x[1].get("timestamp", 0))
            self.cache = dict(sorted_items[-500:])

        self.save_cache()
