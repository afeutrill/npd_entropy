#Implementation of a quantised version of the Grassberger estimator, based on the Lempel-Ziv algorithm, for the continuous valued processes AF 9/6/20 

import numpy as np
from numba import jit, prange
from scipy.special import erfinv

def quantise_series(series, res):
	"""
	Returns a quantised version of a continuous-valued, discrete-time process. This takes the floor to the nearest increment of 1/res
	Parameters:
		series - numpy array: A time series of continuous valued variables
		res - float: the resolution of the quantisation
	Returns:
		Numpy array of a discrete quantised version of the series
	"""  
	series = np.array(series)
	return np.floor(series*res)/res

def quantise_series_around_zero(series, res):
	"""
        Returns a quantised version of a continuous-valued, discrete-time process. Quantises centred around zero.                  
        Parameters:
                series - numpy array: A time series of continuous valued variables
                res - float: the resolution of the quantisation
        Returns:
                Numpy array of a discrete quantised version of the series
        """
	series = np.array(series)
	return np.rint(series*res)/res 

def quantise_series_normal_quantiles(series, num_quantiles):
	"""
        Returns a quantised version of a continuous-valued, discrete-time process. This returns discrete quantiles of the same probability mass, according to a normal distribution                  
        Parameters:
                series - numpy array: A time series of continuous valued variables
                num_quantiles - int: The number of possible quantiles to use as bins for the quantisation
        Returns:
                Numpy array of a discrete quantised version of the series
        """
	series = np.array(series)
	bins = np.array([np.sqrt(2) * erfinv(2 * (i/num_quantiles) - 1) for i in range(num_quantiles+1)])
	return np.digitize(series, bins)	
		

# n is the size of the window, starts at the nth point and the window extends back as far as n, leave some buffer after 2n for potential matching substrings as your appraoch 2n
@jit(nopython = True)
def grassberger_estimate(series, n):
	"""
        Implementation of the estimator described in P. Grassberger "Estimating the information content of symbol sequences and efficient codes", IEEE Transactions on Information Theory 1989.                  
        Parameters:
                series - numpy array: A discrete-valued time series.
                n - int: Number of past values to start for string matching.
        Returns:
                Shannon entropy estimate of the discrete-valued time series
        """
	L_num_array = np.zeros((n,))
	for i in prange(n):
		L_num = 0
		for num in np.arange(n):
			for j in np.arange(1, n-num+1):
				# Comparing the series to back in time only
				if np.all(series[n+i:n+i+num] == series[n+i-j-num:n+i-j]):
					break
				# Just testing changing this to num -1, as it think it's the same as the NN estimator in this case
				# CHanged to L_num = num 3/8/20
				# If the end of the loop with no matches, then set L_num to the previous length
				if j == n - num:
					L_num = num - 1
			# Tests whether non-match has occurred, then exits
			if L_num > 0:
				break
		L_num_array[i] = L_num
	reciprocal = 1/(n * np.log(n)) * L_num_array.sum()
	H_est = 1/reciprocal
	return H_est

