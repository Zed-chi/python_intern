import unittest
from requests import Response
from host_checker import is_alive_host


class TestHostCheckerFunc(unittest.TestCase):
    def test_200_codes(self):
        res = Response()
        res.status_code = 200
        self.assertTrue(is_alive_host(response=res))

    def test_300_codes(self):
        res = Response()
        res.status_code = 300
        self.assertTrue(is_alive_host(response=res))

    def test_400_codes(self):
        res = Response()
        res.status_code = 400
        self.assertFalse(is_alive_host(response=res))

    def test_500_codes(self):
        res = Response()
        res.status_code = 500
        self.assertFalse(is_alive_host(response=res))

    def test_no_args(self):
        self.assertRaises(AttributeError, is_alive_host)


if __name__ == "__main__":
    unittest.main()
