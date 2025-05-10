import numpy as np
'''
Q1: Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)
create a two-dimensional array? Write it the correct way 

Ans: This is because the np.array() function only takes one iterable as an argument. The wrong version passes multiple tuples instead of a list of tuples.

Correct way:'''
arr = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print(arr)

'''
Q2: What is the difference between a = np.array([0, 0, 0]) and a =
np.array([[0, 0, 0]])?

Ans: a is a 1D array with shape (3,), which is a single dimension with 3 elements; while b is a 2D array with shape (1, 3), which is a matrix with 1 row and 3 columns.
'''
a = np.array([0, 0, 0])
b = np.array([[0, 0, 0]])

print(a.shape)
print(b.shape)

'''
Q3: A 3 by 4 by 4 array is created with arr = np.linspace(1, 48,
48).reshape(3, 4, 4). Index or slice this array to obtain the following:

20.0
[ 9. 10. 11. 12.]
[[33. 34. 35. 36.]
 [37. 38. 39. 40.]
 [41. 42. 43. 44.]
 [45. 46. 47. 48.]]
[[ 5.  6.]
 [21. 22.]
 [37. 38.]]
[[36. 35.]
 [40. 39.]
 [44. 43.]
 [48. 47.]]
[[13.  9.  5.  1.]
 [29. 25. 21. 17.]
 [45. 41. 37. 33.]]
[[ 1.  4.]
 [45. 48.]]
[[25. 26. 27. 28.]
 [29. 30. 31. 32.]
 [33. 34. 35. 36.]
 [37. 38. 39. 40.]]
'''
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

val_a = arr[1, 1, 3]
val_b = arr[0, 2, :]
val_c = arr[2, 1:3, :]
val_d = arr[:, 1, :2]
val_e = arr[2, :, 2:]
val_f = arr[:, :, 0]
val_g = arr[:, [0, 3], 0]
val_h = arr[1, :, :]

print("\n(a):", val_a)
print("(b):", val_b)
print("(c):")
print(val_c)
print("(d):")
print(val_d)
print("(e):")
print(val_e)
print("(f):")
print(val_f)
print("(g):")
print(val_g)
print("(h):")
print(val_h)

