#!/usr/bin/env python
"""
Final system test for Maya
"""

from loguru import logger
import time

def test_maya_startup():
    """Test Maya can start up"""
    logger.info("Testing Maya startup...")

    from orchestrator import MayaOrchestrator

    maya = MayaOrchestrator()
    assert maya is not None
    assert maya.brain is not None
    assert maya.voice is not None

    logger.success("✅ Maya initialized successfully")

    # Test one iteration
    maya.main_loop_iteration()

    logger.success("✅ Maya can run iterations")

def test_all_systems():
    """Test all systems are connected"""
    from orchestrator import MayaOrchestrator

    maya = MayaOrchestrator()

    # Test each system
    systems = [
        ("Brain", maya.brain),
        ("Memory", maya.memory),
        ("Vision", maya.vision),
        ("Voice", maya.voice),
        ("Evolution", maya.awareness),
        ("Grok", maya.grok)
    ]

    for name, system in systems:
        assert system is not None, f"{name} not initialized"
        logger.success(f"✅ {name} system OK")

if __name__ == "__main__":
    print("🧪 Running full system test...")

    test_maya_startup()
    test_all_systems()

    print("\n✅ Maya is ready to run!")
    print("\nTo start Maya:")
    print("  ./run_maya.sh")
    print("or")
    print("  python main.py")
