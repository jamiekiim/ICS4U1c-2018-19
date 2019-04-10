import unittest
import foo_lib

class Test_foo_lib(uniittest.TestCase):

    def test_fool_general1(self):
        self.assertEqual(3, foo_lib.fool(9))

    def test_fool_general2(self):
        self.assertEqual(4, foo_lib.fool(16))

    def test_fool_unusual_negative(self):
        self.assertRaises(ValueError, foo_lib.fool, -16)

    def test_fool_unusual_nagative_specific_msg(self):
        with self.assertRaises(ValueError) as err:
            foo_lib.fool(-16)

        self.assertEqual("Cannot square root a negative number", str(err.exception))





