import unittest

from inventory import validate_inventory


class TestInventory(unittest.TestCase):
    def test_valid_server_is_accepted(self):
        result = validate_inventory([{"name": "server1", "ip": "192.168.1.1"}])
        self.assertEqual(result, [])

    def test_empty_name_is_rejected(self):
        result = validate_inventory([{"name": "", "ip": "192.168.1.1"}])
        self.assertTrue(result)

    def test_missing_name_is_rejected(self):
        result = validate_inventory([{"ip": "192.168.1.1"}])
        self.assertTrue(result)

    def test_whitespace_name_is_rejected(self):
        result = validate_inventory([{"name": "   ", "ip": "192.168.1.1"}])
        self.assertTrue(result)

    def test_numeric_name_is_rejected(self):
        result = validate_inventory([{"name": 123, "ip": "192.168.1.1"}])
        self.assertTrue(result)

    def test_object_instead_of_list_is_rejected(self):
        result = validate_inventory({"name": "server1", "ip": "192.168.1.1"})
        self.assertTrue(result)

    def test_non_object_in_list_is_rejected(self):
        result = validate_inventory(["server1"])
        self.assertTrue(result)
