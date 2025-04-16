import unittest
from mainclass import RandomDataAnalysis
from test.TestUtils import TestUtils
import numpy as np

class ExceptionalTests(unittest.TestCase):
    def test_empty_data(self):
        """Test if empty data raises an error"""
        test_obj = TestUtils()
        try:
            empty_analysis = RandomDataAnalysis()
            empty_analysis.data = np.array([])
            empty_analysis.calculate_mean()
            test_obj.yakshaAssert("TestEmptyData", False, "exceptional")
            print("TestEmptyData = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyData", True, "exceptional")
            print("TestEmptyData = Passed")

    def test_invalid_data_type(self):
        """Test if invalid data type raises an error"""
        test_obj = TestUtils()
        try:
            invalid_analysis = RandomDataAnalysis()
            invalid_analysis.data = np.array(["string", "data", "values"])
            invalid_analysis.calculate_mean()
            test_obj.yakshaAssert("TestInvalidDataType", False, "exceptional")
            print("TestInvalidDataType = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestInvalidDataType", True, "exceptional")
            print("TestInvalidDataType = Passed")
