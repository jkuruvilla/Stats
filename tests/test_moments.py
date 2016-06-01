__license__   = "GNU GPLv3 <https://www.gnu.org/licenses/gpl.txt>"
__copyright__ = "2016, Joseph Kuruvilla"
__author__    = "Joseph Kuruvilla <joseph.k@uni-bonn.de>"
__version__   = "1.0"

'''
Tests for moments.py

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

import unittest
import numpy as np
import Stats.moments as mo

# ---------------
# Defining Class
# ---------------

class MyTest(unittest.TestCase):
    '''Tests for moments.py
    '''
    
    def test_unweighted_mean(self):
        a = np.array([2,4,6,8,10])
        self.assertEqual(mo.stat(a).mean(),6)


    def test_weighted_mean(self):
        a = np.array([2,4,6,8,10])
        w = np.array([5,4,3,2,2])
        self.assertEqual(mo.stat(a,w).mean(),5)

    def test_population_variance(self):
        a = np.array([2,4,6,8,10])
        self.assertEqual(mo.stat(a,method='population').variance(), np.sqrt(8))

    def test_sample_variance(self):
        a = np.array([2,4,6,8,10])
        self.assertEqual(mo.stat(a).variance(), np.sqrt(10))

    def test_weighted_variance(self):
        a = np.array([2,5,10])
        w = np.array([5,2,1])
        self.assertEqual(mo.stat(a,w).variance(), np.sqrt(7.1875))

# --------------------
#   Program  start
# --------------------

if __name__ == '__main__':
    unittest.main()
