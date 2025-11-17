#!/usr/bin/env python
from integrations.grok_access import GrokAccess
from integrations.captcha_solver import CaptchaSolver
from automation.browser_automation import BrowserAutomation
from loguru import logger

def test_grok_access():
    """Test Grok access methods"""
    logger.info("Testing Grok access...")

    grok = GrokAccess()

    # Test different types of queries
    queries = [
        "What makes this meme funny?",
        "Write a Python function to sort a list",
        "Explain quantum computing simply"
    ]

    for query in queries:
        response = grok.query(query)
        logger.info(f"Query: {query[:50]}...")
        logger.info(f"Response: {response[:100]}...")
        print()

    # Test cache
    logger.info("Testing cache...")
    response1 = grok.query("Test query")
    response2 = grok.query("Test query")  # Should use cache
    assert response1 == response2
    logger.success("✅ Cache working")

def test_captcha_solver():
    """Test CAPTCHA solver"""
    logger.info("Testing CAPTCHA solver...")

    solver = CaptchaSolver()

    # Test different CAPTCHA types
    captcha_types = ["text", "image", "recaptcha", "generic"]

    for captcha_type in captcha_types:
        result = solver.solve(captcha_type)
        if result["success"]:
            logger.success(f"✅ Solved {captcha_type} CAPTCHA")
        else:
            logger.warning(f"❌ Failed {captcha_type} CAPTCHA")

def test_browser_automation():
    """Test browser automation"""
    logger.info("Testing browser automation...")

    browser = BrowserAutomation()

    # Test human-like behaviors
    browser.human_delay()
    text = browser.human_typing("Hello World")
    movements = browser.random_mouse_movement()
    browser.scroll_naturally()

    logger.info(f"Typed: {text}")
    logger.info(f"Generated {len(movements)} mouse movements")

    # Test account creation (mock)
    try:
        browser.create_account("test@example.com", "password123")
        logger.success("✅ Account creation simulation complete")
    except Exception as e:
        logger.error(f"Account creation failed: {e}")

if __name__ == "__main__":
    print("🧪 Testing integrations...")

    test_grok_access()
    print("\n" + "="*50 + "\n")

    test_captcha_solver()
    print("\n" + "="*50 + "\n")

    test_browser_automation()

    print("\n✅ Integration tests complete!")
