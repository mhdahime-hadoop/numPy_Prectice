# NumPy Exercises, Practice, Solution (https://www.w3resource.com/python-exercises/numpy/basic/index.php)

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

# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

z = np.array([1,2,np.inf,np.nan]) # here we can also use np.array([1,2,np.NINF,np.nan])
print(z)
print(np.isfinite(z))

# 6. Write a NumPy program to test elements-wise for positive or negative infinity. 

z = np.array([1,2,3,np.nan,np.inf,np.NINF,-1,0]) # this will return [false false false false true true false false]
print(z)
print(np.isinf(z))


# 7. Write a NumPy program to test element-wise for NaN of a given array.

z = np.array([1,2,3,np.nan,np.inf,np.NINF,-1,0]) # this will return [false false false true false false false false]
print(z)
print(np.isnan(z))

# 8. Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not. 

f = np.array([1+1j,1+0j,1.5,2,3j])
print(f)
print(np.iscomplex(f)) # [ True False False False  True]
print(f)
print(np.isreal(f)) # [False  True  True  True False]
print(f)
print(np.isscalar(3.1)) # True
print(np.isscalar([3.5])) # False
print(np.isscalar([1+2j])) # False
print(f)
print(np.isscalar(f)) # False










