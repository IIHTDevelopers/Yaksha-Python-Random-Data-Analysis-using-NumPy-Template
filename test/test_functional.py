import unittest
import numpy as np
from mainclass import RandomDataAnalysis
from test.TestUtils import TestUtils


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test data"""
        cls.random_data_analysis = RandomDataAnalysis()

    def test_mean_calculation(self):
        """Test if the mean is correctly calculated"""
        test_obj = TestUtils()
        try:
            obj = self.random_data_analysis.calculate_mean()
            mean_value = np.mean(self.random_data_analysis.data)
            
            if np.isclose(obj, mean_value):
                test_obj.yakshaAssert("TestMeanCalculation", True, "functional")
                print("TestMeanCalculation = Passed")
            else:
                test_obj.yakshaAssert("TestMeanCalculation", False, "functional")
                print("TestMeanCalculation = Failed")
        except:
            test_obj.yakshaAssert("TestMeanCalculation", False, "functional")
            print("TestMeanCalculation = Failed")
                
    def test_median_calculation(self):
        """Test if the median is correctly calculated"""
        test_obj = TestUtils()
        
        try:
            obj = self.random_data_analysis.calculate_median()
            median_value = np.median(self.random_data_analysis.data)
            
            if obj == median_value:
                test_obj.yakshaAssert("TestMedianCalculation", True, "functional")
                print("TestMedianCalculation = Passed")
            else:
                test_obj.yakshaAssert("TestMedianCalculation", False, "functional")
                print("TestMedianCalculation = Failed")
        except:
            test_obj.yakshaAssert("TestMedianCalculation", False, "functional")
            print("TestMedianCalculation = Failed")