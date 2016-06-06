__license__   = "GNU GPLv3 <https://www.gnu.org/licenses/gpl.txt>"
__copyright__ = "2016, Joseph Kuruvilla"
__author__    = "Joseph Kuruvilla <joseph.k@uni-bonn.de>"
__version__   = "1.0"

'''
Program to compute the errors based on Gerhels (1986)

http://adsabs.harvard.edu/abs/1986ApJ...303..336G

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
# Defining Functions
# -------------------

def upper_limit(count_array, S=1.000):
    '''Function to compute the upper limit errors. Equation 10 in Gerhels paper.

    Args:
    --------

    count_array: The array for which the upper limit error is to be computed.
    S: Value of S depends on the confidence level considered. Check Table 3 of
       Gerhels paper. Default of 1 corresponds to 1 sigma.

    Returns:
    ---------
    up_lim: Array containing the upper limit errors.
    '''
    count_array = np.asarray(count_array)
    up_lim = count_array + (S*np.sqrt(count_array+1)) + ((S**2+2)/float(3))
    return np.array(up_lim)

def lower_limit(count_array, S=1.000):
    '''Function to compute the lower limit errors. Equation 11 in Gerhels paper.

    Args:
    --------

    count_array: The array for which the lower limit error is to be computed.
    S: Value of S depends on the confidence level considered. Check Table 3 of
       Gerhels paper. Default of 1 corresponds to 1 sigma.

    Returns:
    ---------
    lo_lim: Array containing the lower limit errors.
    '''
    count_array = np.asarray(count_array)
    lo_lim = []
    for i in range(len(count_array)):
        if count_array[i] == 0:
            lo_lim.append(0)
        else:
            lo_lim.append(count_array[i] - np.sqrt(count_array[i]-0.25) + ((S**2-1)/float(3)))
    return np.array(lo_lim)
