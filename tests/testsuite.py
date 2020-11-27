import unittest

#import unittests.ArcGPTest
import unittests.GaussianProcess_test
import unittests.LinearRegression_test
import unittests.RandomForest_test
import unittests.ModelUtil_test
import unittests.RidgeRegression_test
import unittests.Scaler_test
import unittests.SupportVector_test
import unittests.RemoveInactive
import unittests.DependenciesVersions_test
import unittests.KNN_test


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(unittests.DependenciesVersions_test.
                                      TestDependenciesVersion))
    for i in range(2):
        #_suite.addTest(unittest.makeSuite(unittests.ArcGPTest.ArcGPTest))
        _suite.addTest(unittest.makeSuite(unittests.KNN_test.KNN_test))
        _suite.addTest(unittest.makeSuite(unittests.RandomForest_test.
                                          RandomForest_test))
        _suite.addTest(unittest.makeSuite(unittests.RidgeRegression_test.
                                          RidgeRegression_test))
        _suite.addTest(unittest.makeSuite(unittests.GaussianProcess_test.
                                          GaussianProcess_test))
        _suite.addTest(unittest.makeSuite(unittests.LinearRegression_test.
                                          LinearRegression_test))
        _suite.addTest(unittest.makeSuite(unittests.ModelUtil_test.
                                          ModelUtil_test))
        _suite.addTest(unittest.makeSuite(unittests.Scaler_test.Scaler_test))
        _suite.addTest(unittest.makeSuite(unittests.SupportVector_test.
                                          SupportVectorRegressionTest))
        _suite.addTest(unittest.makeSuite(unittests.RemoveInactive.
                                          RemoveInactive))

    return _suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    test_suite = suite()
    runner.run(suite())
