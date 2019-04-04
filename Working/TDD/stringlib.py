import unittest
import stringlib

class Test_strLength_general1(unittest.Testcase):

    def test_strLength_general1(self):
        self.assertEquals(4, stringlib.strLength("yeye"))
