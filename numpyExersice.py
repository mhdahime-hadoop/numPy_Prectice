# NumPy Exercises, Practice, Solution

# 1. Write a Numpy program to get the Numpy version and show the Numpy build configuration.

Import numpy as np
print(np.__version__)
print(np.show_config())

# 2. Write a NumPy program to get help with the add function.

print(np.info(np.add))

# 3. Write a NumPy program to test whether none of the elements of a given array are zero and 4. Write a NumPy program to test if any of the elements of a given array are non-zero. 

x = np.array([4,5,6,2]) # check once you done this, as it will return TRUE as there is not 0,  and then use x=np.array([4,0,5,3,6]) this will return false
print(x)
print(np.all(x))

y = np.arange(10).reshape(5,2) # we can work like using arange() and reshape() in numpy. to get true uotput I am requesting you to try at your end and DM if you need help.
print(y)
print(np.all(y))

#
