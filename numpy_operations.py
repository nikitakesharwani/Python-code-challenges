import numpy as np

numpy_list1 = np.array([[4,5,6,3,2,5],[4,5,6,4,3,3]])
numpy_list2 = np.array([[7,7,7,8,5,4],[4,5,3,33,5,6]])

addition = numpy_list1 + numpy_list2
print(addition)

subtraction = numpy_list1 - numpy_list2
print(subtraction)

multiplication = numpy_list1 * numpy_list2
print(multiplication)

numpy1_squared = numpy_list1 ** 2
print(numpy1_squared) 

numpy2_squared = numpy_list2 ** 2
print(numpy2_squared)

array_arange = np.arange(5)
sliced_array = array_arange[0:2]
print(sliced_array)

