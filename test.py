import unittest
from package import HR_STR, is_valid_date, load_json, save_json

class TestMyModule(unittest.TestCase):
    def test_valid_date_true(self):
        self.assertTrue(is_valid_date("2024-10-10"))
    
    def test_valid_date_false(self):
        self.assertFalse(is_valid_date("2024-99-99"))

    def test_load_json(self):
        file_name = "test.json"
        data = [{"name": "John Doe"}]

        save_json(file_name, data)
        result = load_json(file_name)

        self.assertEqual(result, data)

    def test_constant_var(self):
        val = HR_STR
        self.assertLogs(val)

if __name__ == "__main__":
    unittest.main()
