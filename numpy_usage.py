import numpy as np

numbers = [4,2,3,5,5,6,44,9]
np_array_list = np.array(numbers)
print(np_array_list)
print(type(np_array_list))
print(np_array_list.ndim)
print(np_array_list.shape)
print(np_array_list.dtype)

zeros_tensor = np.zeros((4,6))
print(zeros_tensor)

ones_tensor = np.ones((4,6))
print(ones_tensor)

eye_tensor = np.eye(5,5)
print(eye_tensor)

arange_tensor = np.arange(4)
print(arange_tensor)

new_array = np.array(([2,34,5,4,6,5],[7,9,5,6,7,7]))
print(new_array)
print(new_array.shape)
new_array.shape = ((6,2))
print(new_array)