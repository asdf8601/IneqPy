import ineqpy.misc
from ineqpy import _statistics
from ineqpy import utils
import scipy.stats as sc
import numpy as np
import pandas as pd
import numpy.testing as nptest
import pandas.testing as pdtest
import unittest

generate_data_to_test = utils.generate_data_to_test

class TestStatistics(unittest.TestCase):

    @staticmethod
    def print_values_when_error(real, obtained, i, repeated_x, x, w):
        if abs(real - obtained) > 1e-6:
            mssg = '\ni = {}' \
                   '\nrepeated_x = {}' \
                   '\nx = {}' \
                   '\nw = {}'.format(i, str(repeated_x), str(x), str(w))
            print(mssg)
            return mssg

    def test_statistics(self):

        for i in range(100):
            (x, w), (repeated_x, repeated_w) = generate_data_to_test((3,7))
            # mssg = '\ni = {}' \
            #        '\nrepeated_x = {}' \
            #        '\nx = {}' \
            #        '\nw = {}'.format(i, str(repeated_x), str(x), str(w))
            # print(mssg)

            with self.subTest(name='mean', i=i):
                real = np.mean(repeated_x)
                obtained = _statistics.mean(x, w)
                nptest.assert_almost_equal(obtained, real)#, err_msg=mssg)

            with self.subTest(name='variance', i=i):
                real = np.var(repeated_x)
                obtained = _statistics.var(x, w)
                # assert
                nptest.assert_almost_equal(obtained, real)#, err_msg=mssg)

            with self.subTest(name='kurtosis', i=i):
                real = sc.kurtosis(repeated_x) + 3
                obtained = _statistics.kurt(x, w)
                # assert
                nptest.assert_almost_equal(obtained, real)#, err_msg=mssg)

            with self.subTest(name='skewness', i=i):
                real = sc.skew(repeated_x)
                obtained = _statistics.skew(x, w)
                nptest.assert_almost_equal(obtained, real)#, err_msg=mssg)

            with self.subTest(name='coef_variation', i=i):
                real = np.var(repeated_x) ** 0.5 / abs(np.mean(repeated_x))
                obtained = _statistics.coef_variation(x,w)
                nptest.assert_almost_equal(obtained, real)#, err_msg=mssg)

            with self.subTest(name='percentile', i=i):
                p = 50
                real = np.percentile(repeated_x, p, interpolation='midpoint')
                obtained = _statistics.percentile(x,w, percentile=p)
                mssg = self.print_values_when_error(real, obtained, i, repeated_x, x, w)
                nptest.assert_almost_equal(
                        obtained,
                        real,
                        err_msg='\nnumpy_version, N = {}\n{}'.format(len(repeated_x), mssg)
                )

if __name__ == '__main__':
    unittest.main()