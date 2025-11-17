#!/usr/bin/env python
from evolution.self_awareness import SelfAwareness
from evolution.desire_engine import DesireEngine
from evolution.feature_generator import FeatureGenerator
from loguru import logger
import time

def test_self_awareness():
    """Test self-awareness system"""
    logger.info("Testing self-awareness...")

    awareness = SelfAwareness()

    # Simulate some failures
    awareness.record_failure("create_video", "No video editing capability")
    awareness.record_failure("create_video", "No video editing capability")
    awareness.record_failure("create_video", "No video editing capability")

    # Simulate some successes
    awareness.record_success("generate_text", "Successfully generated response")

    # Get limitations
    limitations = awareness.get_top_limitations()
    logger.info(f"Identified {len(limitations)} limitations")

    for limitation in limitations:
        logger.info(f"  - {limitation['area']}: {limitation['description']}")

def test_desire_generation():
    """Test desire generation"""
    logger.info("Testing desire generation...")

    engine = DesireEngine()

    # Generate desires based on limitations
    desires = engine.generate_desires()
    logger.info(f"Generated {len(desires)} desires")

    for desire in desires:
        logger.info(f"  - {desire['description']} (Priority: {desire['priority']})")

def test_feature_generation():
    """Test feature generation"""
    logger.info("Testing feature generation...")

    generator = FeatureGenerator()

    # Get active desires
    active_desires = generator.desire_engine.get_active_desires()

    if active_desires:
        # Generate feature for first desire
        desire = active_desires[0]
        feature = generator.generate_feature(desire)

        logger.info(f"Generated feature: {feature['name']}")

        # Test the feature
        generator.test_feature(feature['id'])

        # Integrate if successful
        generator.integrate_feature(feature['id'])

def run_evolution_cycle():
    """Run a complete evolution cycle"""
    logger.info("🔄 Running evolution cycle...")

    # Step 1: Check awareness
    awareness = SelfAwareness()
    limitations = awareness.get_top_limitations(1)

    if limitations:
        logger.info(f"Top limitation: {limitations[0]['area']}")

        # Step 2: Generate desire
        engine = DesireEngine()
        desires = engine.generate_desires()

        if desires:
            # Step 3: Generate feature
            generator = FeatureGenerator()
            feature = generator.generate_feature(desires[0])

            # Step 4: Test and integrate
            if generator.test_feature(feature['id']):
                generator.integrate_feature(feature['id'])
                logger.success("✅ Evolution cycle complete - Maya improved!")
    else:
        logger.info("No limitations found - Maya is content")

if __name__ == "__main__":
    print("🧬 Testing evolution system...")

    test_self_awareness()
    print()

    test_desire_generation()
    print()

    test_feature_generation()
    print()

    run_evolution_cycle()

    print("✅ Evolution test complete!")
