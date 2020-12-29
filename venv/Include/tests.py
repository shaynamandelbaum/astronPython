import unittest
import constants


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(5, 5)
        self.assertEqual(5 in constants.HAZARD_NUMBERS, True)


if __name__ == '__main__':
    unittest.main()
