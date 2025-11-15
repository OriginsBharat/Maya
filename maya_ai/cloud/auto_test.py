from loguru import logger
import sys

class MayaAutoTest:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    def run_all_tests(self):
        logger.info("Maya is testing herself...")

        # Test 1: Storage
        try:
            from cloud.storage import CloudStorage
            storage = CloudStorage()
            storage.save("test", "test.txt")
            self.tests_passed += 1
            logger.success("✅ Storage: OK")
        except:
            self.tests_failed += 1
            logger.error("❌ Storage: Failed")

        # Test 2: Config
        try:
            import yaml
            with open('config/config.yaml') as f:
                config = yaml.safe_load(f)
            self.tests_passed += 1
            logger.success("✅ Config: OK")
        except:
            self.tests_failed += 1
            logger.error("❌ Config: Failed")

        # Report
        logger.info(f"Tests Passed: {self.tests_passed}")
        logger.info(f"Tests Failed: {self.tests_failed}")

        if self.tests_failed > 0:
            logger.warning("Some tests failed, but Maya will keep running")

        return self.tests_failed == 0

if __name__ == "__main__":
    tester = MayaAutoTest()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
