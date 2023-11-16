
import numpy as np

# Sorting Operations
arr = np.array([3, 1, 2, 4])
sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

keys = np.array(['apple', 'banana', 'cherry', 'date'])
sorted_indices = np.lexsort(keys)
print("Lexsorted Indices:", sorted_indices)

indices = np.argsort(arr)
print("Indices that Sort the Array:", indices)

arr.sort()
print("In-place Sorted Array:", arr)

complex_arr = np.array([3 + 2j, 1 + 1j, 2 - 3j, 4 + 0j])
sorted_complex_arr = np.sort_complex(complex_arr)
print("Sorted Complex Array:", sorted_complex_arr)

partitioned_arr = np.partition(arr, 2)
print("Partitioned Array:", partitioned_arr)

indices_partition = np.argpartition(arr, 2)
print("Indices for Partitioning:", indices_partition)

# Searching Operations
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

max_index = np.argmax(arr_2d)
print("Index of Maximum Value:", max_index)

arr_nan = np.array([1, 2, np.nan, 4, 5])
nan_max_index = np.nanargmax(arr_nan)
print("Index of Maximum Value (ignoring NaNs):", nan_max_index)

min_index = np.argmin(arr_2d)
print("Index of Minimum Value:", min_index)

nan_min_index = np.nanargmin(arr_nan)
print("Index of Minimum Value (ignoring NaNs):", nan_min_index)

arr_condition = np.array([[0, 1, 0], [2, 0, 3]])
indices_condition = np.argwhere(arr_condition != 0)
print("Indices of Non-Zero Elements:", indices_condition)

nonzero_indices = np.nonzero(arr)
print("Indices of Non-Zero Elements (Flattened):", nonzero_indices)

flat_nonzero_indices = np.flatnonzero(arr)
print("Indices of Non-Zero Elements (Flattened):", flat_nonzero_indices)

condition = arr > 3
result = np.where(condition, arr, 0)
print("Conditional Result:", result)

sorted_arr_search = np.array([1, 2, 4, 5, 7])
indices_search = np.searchsorted(sorted_arr_search, 3)
print("Index to Insert 3:", indices_search)

condition_extract = arr % 2 == 0
extracted_values = np.extract(condition_extract, arr)
print("Extracted Values (even elements):", extracted_values)

# Counting Operations
count_nonzero = np.count_nonzero(arr_condition)
print("Count of Non-Zero Elements:", count_nonzero)



