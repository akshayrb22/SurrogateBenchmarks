import unittest


class TestDependenciesVersion(unittest.TestCase):

    def test_sklearn(self):
        import sklearn
        version = sklearn.__version__
        self.assertEqual(version, '0.23.2')

    def test_scipy(self):
        import scipy
        version = scipy.__version__
        self.assertEqual(version, "1.5.4")

    def test_numpy(self):
        import numpy
        version = numpy.__version__
        self.assertEqual(version, "1.19.4")
