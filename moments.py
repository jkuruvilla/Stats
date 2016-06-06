__license__   = "GNU GPLv3 <https://www.gnu.org/licenses/gpl.txt>"
__copyright__ = "2016, Joseph Kuruvilla"
__author__    = "Joseph Kuruvilla <joseph.k@uni-bonn.de>"
__version__   = "1.0"

'''
Program to compute mean, dispersion, skewness and kurtosis both weigthed
and unweighted.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# ------------------
# Importing Modules
# ------------------

import numpy as np

# -------------------
# Defining Class
# -------------------

class stat:
    '''Class to determine the moments
    '''
    def __init__(self, x_quantity, weights=None, method='sample'):
        '''Function initialising the quantities.
        We want to find the mean of x_quantity.
        method denotes if it is sample or population statistic measure
        '''
        self.x_quantity = x_quantity
        if weights is None:
            self.weights = 1
        else:
            self.weights = weights
        self.size = len(self.x_quantity)
        self.method = method

    def mean(self):
        if self.weights is 1:
            _mean =  np.sum(self.x_quantity)/float(self.size)
        else:
            _mean =  np.sum(self.x_quantity*self.weights)/float(np.sum(self.weights))
        return _mean

    def variance(self):
        _mean = self.mean()
        if self.weights is 1:
            if self.method == 'population':
                _variance = np.sqrt(np.sum((self.x_quantity - _mean)**2)/float(self.size))
            elif self.method == 'sample':
                _variance = np.sqrt(np.sum((self.x_quantity - _mean)**2)*(1/float(self.size-1)))
            else:
                raise Exception("Booo. Seems like you didn't give the right method.")
        else:
            _variance = np.sqrt(np.sum(self.weights*(self.x_quantity - _mean)**2)/float(np.sum(self.weights)))
        return _variance

    def skewness(self):
        _mean = self.mean()
        _variance = self.variance()
        if self.weights is 1:
            if self.method == 'population':
                _skewness = np.sum((((self.x_quantity - _mean)/float(_variance))**3))/float(self.size)
            elif self.method == 'sample':
                _skewness = np.sum((((self.x_quantity - _mean)/float(_variance))**3))*float(self.size/float((self.size-1)*(self.size-2)))
            else:
                raise Exception("Booo. Seems like you didn't give the right method.")
        else:
            _skewness = np.sum((((self.weights*(self.x_quantity - _mean))/float(_variance))**3))/float(np.sum(self.weights))
        return _skewness

    def kurtosis(self):
        _mean = self.mean()
        _variance = self.variance()
        if self.weights is 1:
            if self.method == 'population':
                _kurtosis = np.sum(((self.x_quantity - _mean)/float(_variance))**4)/float(self.size)
            elif self.method == 'sample':
                _kurtosis = np.sum(((self.x_quantity - _mean)/float(_variance))**4)*float((self.size*(self.size+1))/float((self.size-1)*(self.size-2)*(self.size-3)))
            else:
                raise Exception("Booo. Seems like you didn't give the right method.")
        else:
            _kurtosis = np.sum((((self.weights*(self.x_quantity - _mean))/float(_variance))**4))/float(np.sum(self.weights))
        return _kurtosis

def statistic_measure_weigthed(a,w):
    _mean = np.sum(a*w)/float(np.sum(w))
    _variance = np.sqrt(np.sum(w*(a-_mean)**2)/float(np.sum(w)))
    _skewness = np.sum(w*((a-_mean)/float(_variance))**3)/float(np.sum(w))
    _kurtosis = np.sum(w*((a-_mean)/float(_variance))**4)/float(np.sum(w))
    return _mean, _variance, _skewness, _kurtosis

# --------------------
#   Program  start
# --------------------

if __name__ == "__main__":

    main()
