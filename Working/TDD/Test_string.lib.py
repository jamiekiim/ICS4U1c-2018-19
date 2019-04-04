import unittest
import stringlib

class Test_strLength_general1(unittest.Testcase):

    def test_strLength_general1(self):
        self.assertEquals(4, stringlib.strLength("yeye"))

    def test_strLength_general2(self):
        self.assertEquals(3, stringlib.strLength("cat"))

    def test_strLength_general3(self):
        self.assertEquals(0, stringlib.strLength("hello"))

    def test_strLength_corner_emptystring(self):
        self.assertEquals(0, stringlib.strLength(""))

    def test_strLength_unusal_integer(self):
        self.assertEquals(0, stringlib.strLength(5))
