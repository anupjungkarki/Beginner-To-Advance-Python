'''
Numpy is a python library used for working with arrays. In python we have a list which work as 
array but they are slower in process so, numPy array are used beside those python list because
it 50x faster than those list.

'''

# So before used numPy we have to install it in our system
# --> $ pip install numpy

# After that let's import numPy
import numpy
arr = numpy.array(['foo','bar','jar'])
print(arr)


# NumPy is usually imported under np alias
import numpy as np
array = np.array([1,4,5,6,7,8,9,10])
print(array)


# checking numPy Version
print(np.__version__)