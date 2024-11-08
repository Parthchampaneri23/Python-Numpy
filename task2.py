#Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result. Input: my_list = [1, 2, 3, 4, 5]



import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the array
print("Array:", my_array)

# Display the first and last index
print("First index:", 0)
print("Last index:", len(my_array) - 1)

# Multiply each element by 2
result = my_array * 2

# Display the result
print("Result after multiplying by 2:", result)
