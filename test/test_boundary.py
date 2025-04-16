import unittest
import numpy as np
from mainclass import RandomDataAnalysis
from test.TestUtils import TestUtils


class BoundaryTests(unittest.TestCase):
    def test_single_value_data(self):
        """Test system with only one data point"""
        single_value_analysis = RandomDataAnalysis()
        single_value_analysis.data = np.array([500])  # Boundary case with one value
        obj_mean = single_value_analysis.calculate_mean()
        obj_median = single_value_analysis.calculate_median()
        test_obj = TestUtils()
        if obj_mean == 500 and obj_median == 500:
            test_obj.yakshaAssert("TestSingleValueData", True, "boundary")
            print("TestSingleValueData = Passed")
        else:
            test_obj.yakshaAssert("TestSingleValueData", False, "boundary")
            print("TestSingleValueData = Failed")
            
    def test_large_value_data(self):
        """Test system with large data points"""
        test_obj = TestUtils()
        try:
            large_value_analysis = RandomDataAnalysis()
            large_value_analysis.data = np.random.randint(1, 1000001, size=100)
            obj_mean = large_value_analysis.calculate_mean()
            obj_median = large_value_analysis.calculate_median()
            
            if obj_mean > 0 and obj_median > 0:
                test_obj.yakshaAssert("TestLargeValueData", True, "boundary")
                print("TestLargeValueData = Passed")
            else:
                test_obj.yakshaAssert("TestLargeValueData", False, "boundary")
                print("TestLargeValueData = Failed")
        except:
            test_obj.yakshaAssert("TestLargeValueData", False, "boundary")
            print("TestLargeValueData = Failed")