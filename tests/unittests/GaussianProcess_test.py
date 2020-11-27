import pickle
import os
import unittest
import hashlib

import numpy
from sklearn.metrics import mean_squared_error

import Surrogates.RegressionModels.GaussianProcess
import Surrogates.DataExtraction.pcs_parser as pcs_parser
from Surrogates.DataExtraction.data_util import read_csv

numpy.random.seed(1)


class GaussianProcessTest(unittest.TestCase):
    _checkpoint = None
    _data = None
    _para_header = None
    _sp = None

    def setUp(self):
        self._sp = pcs_parser.read(
            open(
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "Testdata/nips2011.pcs")))
        # Read data from csv
        header, self._data = read_csv(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "Testdata/hpnnet_nocv_convex_all_fastrf_results.csv"),
                                      has_header=True,
                                      num_header_rows=3)
        self._para_header = header[0][:-2]
        data_view = self._data.view(numpy.float)
        self._checkpoint = hashlib.sha256(data_view).hexdigest()
        self.assertEqual(
            '4a103bec122ec26deef38d1ee2279bd5797c495c3a89c7a62b0b82b39a7e042c',
            self._checkpoint)

    def tearDown(self):
        data_view = self._data.view(numpy.float)
        self.assertEqual(
            hashlib.sha256(data_view).hexdigest(), self._checkpoint)

    def test_train(self):
        x_train_data = self._data[:100, :-2]
        y_train_data = self._data[:100, -1]
        x_test_data = self._data[100:, :-2]
        y_test_data = self._data[100:, -1]

        model = Surrogates.RegressionModels.GaussianProcess.GaussianProcess(
            sp=self._sp, rng=1, encode=False, debug=True)

        model.train(x=x_train_data,
                    y=y_train_data,
                    param_names=self._para_header)

        y = model.predict(x=x_train_data[1, :])
        # print("Is: %100.70f, Should: %f" % (y, y_train_data[1]))
        print(f"Is: {y[0]:.6f}, Should: {y_train_data[1]}")
        self.assertAlmostEqual(y[0], 0.47074515351490015)

        print("Predict whole data")
        y_whole = model.predict(x=x_test_data)
        mse = mean_squared_error(y_true=y_test_data, y_pred=y_whole)
        # print("MSE: %100.70f" % mse)
        print(f'MSE: {mse:100.70f}')
        self.assertAlmostEqual(mse, 0.0062575986090041905)

        print("Soweit so gut")

        # Try the same with encoded features
        model = Surrogates.RegressionModels.GaussianProcess.GaussianProcess(
            sp=self._sp, rng=1, encode=True, debug=True)
        #print data[:10, :-2]
        model.train(x=x_train_data,
                    y=y_train_data,
                    param_names=self._para_header,
                    rng=1)

        y = model.predict(x=x_train_data[1, :])
        # print("Is: %100.70f, Should: %f" % (y, y_train_data[1]))
        print(f'Is {y:100.70f}, Should: {y_train_data[1]}')
        self.assertAlmostEqual(y[0], 0.46467166529432441)

        print("Predict whole data")
        y_whole = model.predict(x=x_test_data)
        mse = mean_squared_error(y_true=y_test_data, y_pred=y_whole)
        # print("MSE: %100.70f" % mse)
        print(f'MSE: {mse:100.70f}')
        self.assertAlmostEqual(mse, 0.0091926512804233057)

        fn = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                          "Testdata/testGP.pkl")
        fh = open(fn, "wb")
        pickle.dump(model, fh)
        fh.close()
        a = pickle.load(fn)

        print("Predict whole data")
        y_whole = a.predict(x=x_test_data)
        mse = mean_squared_error(y_true=y_test_data, y_pred=y_whole)
        # print("MSE: %100.70f" % mse)
        print(f'MSE: {mse:100.70f}')
        self.assertAlmostEqual(mse, 0.0091926512804233057)
        self.assertEqual(a._name, "GP True")
        self.assertEqual(a._mcmc_iters, 10)

        os.remove(fn)
