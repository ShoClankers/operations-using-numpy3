import numpy as np


original_array = np.arange(10)

modified_array = original_array.copy()
modified_array[modified_array % 2 != 0] = -1

two_row_array = original_array.reshape(2, 5)

total = 0
for value in original_array:
    total += value

print("Original array:", original_array)
print("Array with odd numbers replaced:", modified_array)
print("Original array reshaped into two rows:\n", two_row_array)
print("Sum of original array elements:", total)