import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_metrics_endpoint(self):
        response = self.app.get("/metrics")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("cpu_usage", data)
        self.assertIn("cpu_usage_by_core", data)
        self.assertIn("memory_info", data)


if __name__ == "__main__":
    unittest.main()
