#!/usr/bin/env python
from streaming.stream_manager import StreamManager
from content.video_creator import VideoCreator
from content.reddit_reactor import RedditReactor
from loguru import logger

def test_streaming():
    """Test streaming functions"""
    logger.info("Testing streaming...")

    stream = StreamManager()
    stream.start_stream("Test Stream")

    # Simulate some highlights
    stream.mark_highlight("00:01:00", "Funny moment")
    stream.mark_highlight("00:05:00", "Epic reaction")

    stream.end_stream()
    logger.success("✅ Streaming test complete")

def test_video_creation():
    """Test video creation"""
    logger.info("Testing video creation...")

    creator = VideoCreator()

    # Create a test video
    video_path = creator.create_video("test", {
        "content": "Test video",
        "reactions": ["LOL", "Amazing"]
    })

    # Apply some edits
    creator.edit_video(video_path, ["trim", "add_music", "add_text"])

    logger.success("✅ Video creation test complete")

def test_reddit_reactor():
    """Test Reddit reactor"""
    logger.info("Testing Reddit reactor...")

    reactor = RedditReactor()

    # Create a reaction video (simplified test)
    video_path = reactor.create_reaction_video("memes", num_posts=2)

    logger.success(f"✅ Created reaction video: {video_path}")

if __name__ == "__main__":
    print("🧪 Testing content creation systems...")

    test_streaming()
    test_video_creation()
    test_reddit_reactor()

    print("✅ All content tests complete!")
