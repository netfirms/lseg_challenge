import unittest
from function import get_nested_json_value

class TestGetNestedJsonValue(unittest.TestCase):
    def setUp(self):
        # Test data
        self.test_data_1 = {"a": {"b": {"c": "d"}}}
        self.test_data_2 = {"x": {"y": {"z": "a"}}}

    def test_valid_nested_paths(self):
        # Test with first dataset
        self.assertEqual(get_nested_json_value(self.test_data_1, "a/b/c"), "d")
        self.assertEqual(get_nested_json_value(self.test_data_1, "a/b"), {"c": "d"})
        self.assertEqual(get_nested_json_value(self.test_data_1, "a"), {"b": {"c": "d"}})

        # Test with second dataset
        self.assertEqual(get_nested_json_value(self.test_data_2, "x/y/z"), "a")
        self.assertEqual(get_nested_json_value(self.test_data_2, "x/y"), {"z": "a"})
        self.assertEqual(get_nested_json_value(self.test_data_2, "x"), {"y": {"z": "a"}})

    def test_partial_paths(self):
        # Test partial paths that should work
        self.assertEqual(get_nested_json_value(self.test_data_1, "a/b"), {"c": "d"})
        self.assertEqual(get_nested_json_value(self.test_data_2, "x/y"), {"z": "a"})

    def test_invalid_paths(self):
        # Test non-existent paths
        self.assertIsNone(get_nested_json_value(self.test_data_1, "a/b/d"))
        self.assertIsNone(get_nested_json_value(self.test_data_1, "a/c"))
        self.assertIsNone(get_nested_json_value(self.test_data_1, "b"))

        self.assertIsNone(get_nested_json_value(self.test_data_2, "x/y/w"))
        self.assertIsNone(get_nested_json_value(self.test_data_2, "x/z"))
        self.assertIsNone(get_nested_json_value(self.test_data_2, "y"))

    def test_empty_path(self):
        # Test empty path should return None
        self.assertIsNone(get_nested_json_value(self.test_data_1, ""))
        self.assertIsNone(get_nested_json_value(self.test_data_2, ""))

    def test_path_with_whitespace(self):
        # Test paths with whitespace
        self.assertEqual(get_nested_json_value(self.test_data_1, " a / b / c "), "d")
        self.assertEqual(get_nested_json_value(self.test_data_2, " x / y / z "), "a")

    def test_non_dict_input(self):
        # Test with non-dictionary inputs
        self.assertIsNone(get_nested_json_value([1, 2, 3], "0"))
        self.assertIsNone(get_nested_json_value("string", "length"))
        self.assertIsNone(get_nested_json_value(123, "digits"))

    def test_malformed_paths(self):
        # Test malformed paths
        self.assertIsNone(get_nested_json_value(self.test_data_1, "/"))
        self.assertIsNone(get_nested_json_value(self.test_data_1, "a//c"))
        self.assertIsNone(get_nested_json_value(self.test_data_2, "x/y/"))

    def test_edge_cases(self):
        # Test with actual slashes in keys (should fail as we're using slash as separator)
        data_with_slashes = {"a/b": {"c/d": "value"}}
        self.assertIsNone(get_nested_json_value(data_with_slashes, "a/b/c/d"))

if __name__ == "__main__":
    unittest.main()