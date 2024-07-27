# tests/test_metrics.py
import unittest
from metrics import Metrics


class TestMetrics(unittest.TestCase):

    def test_get_cpu_usage_by_core(self):
        result = Metrics.get_cpu_usage_by_core(interval=0.1)
        self.assertIsInstance(result, dict)
        for core, usage in result.items():
            self.assertIsInstance(core, str)
            self.assertIsInstance(usage, float)

    def test_get_cpu_usage(self):
        result = Metrics.get_cpu_usage(interval=0.1)
        self.assertIsInstance(result, float)

    def test_get_memory_info(self):
        result = Metrics.get_memory_info()
        self.assertIsInstance(result, dict)
        self.assertIn("total", result)
        self.assertIn("available", result)
        self.assertIn("percent", result)
        self.assertIn("used", result)
        self.assertIn("free", result)


if __name__ == "__main__":
    unittest.main()
